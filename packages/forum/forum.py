"""
Nom du module: forum.py

Description: Ce module permet de récupérer/manipuler/modifier les données "essentielles" d'un forum de la plateforme SALOME pour pouvoir ensuite les placer dans un fichier JSON.
             J'entends par "essentielle" :
                     - Une page qui contient au moins deux chaats, c'est-à-dire de manière générale qu'il y a au moins une réponse à la question.

Informations:
	- Chaque forum possède plusieurs pages, identifiées par un nombre entier. Par exemple, dans forum_9, il y a la page numéro 7203642.
	- Chaque page contient un titre et une discussion entre plusieurs personnes. L'objectif de cette discussion est de répondre à la question d'un utilisateur.
	- Voici l'arborescence du fichier JSON qu'on souhaite produire :
	
	        "number" (int) : Le numéro du forum
	        "pages" (list) : La liste de chaque page "essentielle" du forum (dict) :
	                "path" (str) : Le nom du chemin vers la page
	                "number" (int) : Le numéro de la page
	                "title" (str) : Le titre de la page
	                "discussion" (list) : La liste de chaque chat (str) dans la discussion
	                "summary" (list) : La liste correspondant au résumé de la première question

Dépendances: os, re, json, bs4, filecmp

Auteur: Kelvin LEFORT

Date: 20/08/2024
"""

import os
import re
import json
from bs4 import BeautifulSoup
import filecmp

def get_forum_data(forum_directory_path_name, summarizer):
    """
    get_forum_data - Récupère les informations "essentielles" d'un seul forum de la plateforme SALOME.

    Arguments:
        forum_directory_path_name (str): Le nom du chemin vers le répertoire où se trouve les données "essentielles" des forums de la plateforme SALOME.
        summarizer: L'objet permettant de résumer les questions.
    
    Sortie:
        forum_informations (dict): Les informations "essentielles" du forum. Elles ont le format suivant :

            "name" (int) : Le numéro du forum,
            "pages" (list) : La liste de chaque page du forum (dict) :
                    "path" (str) : Le nom du chemin vers la page
                    "number" (int) : Le numéro de la page,
                    "title" (str) : Le titre de la page,
                    "discussion" (list) : La liste de chaque chat (str) dans la discussion.
    
    Exemple:
        pattern = re.compile(r'^\d+$')
        forum_informations = get_forum_informations(9, "/home/projects/stage-cea-chatbot/data/forums/", pattern)
    """

    # Déclarer les informations du forum comme un dictionnaire vide
    forum_informations = {}

    # Écrire le numéro du forum dans le champ "number" de forum_informations
    forum_informations["name"] = forum_directory_path_name

    # Déclarer le champ "pages" de forum_informations comme une liste vide
    forum_informations["pages"] = []

    # Déterminer le nom des sous-répertoires où se trouvent les données de chaque page de ce forum
    pages_number = [name for name in os.listdir(forum_directory_path_name) if os.path.isdir(os.path.join(forum_directory_path_name, name))]

    # ==================== Récupération des informations de chaque page du forum ====================
    for page_number in pages_number:
        print("=> page HTML ", page_number)
        page_informations = get_page_informations(page_number, forum_directory_path_name, summarizer)

        if page_informations:
            # Ajouter les informations de la page en fin de liste de forum_informations["pages"]
            forum_informations["pages"].append(page_informations)
    
    return forum_informations

def get_page_informations(page_number, forum_directory_path_name, summarizer):
    """
    get_page_informations - Récupère les informations "essentielles" d'une seule page d'un seul forum de la plateforme SALOME.

    Arguments:
        page_number (int): Le numéro de la page.
        forum_directory_path_name (str): Le nom du chemin vers le répertoire où se trouve les données "essentielles" du forum.
        summarizer: L'objet permettant de résumer les questions.
    
    Sortie:
        page_informations (dict):
            - S'il y a au moins une réponse à la question : Les informations "essentielles" de la page. Elles ont le format suivant :

                "path" (str) : Le nom du chemin vers la page
                "number" (int) : Le numéro de la page,
                "title" (str) : Le titre de la page,
                "discussion" (list) : La liste de chaque chat (str) dans la discussion.
                
            - S'il n'y a pas de réponse(s) à la question : {}

    Exemple:
        page_informations = get_page_informations(7203642, "/home/projects/stage-cea-chatbot/data/forums/forum_9/")
    """

    # Déclarer les informations de la page comme un dictionnaire vide
    page_informations = {}
    
    # Déterminer le chemin vers le répertoire où se trouve les données de cette page
    page_directory_path_name = os.path.join(forum_directory_path_name, page_number)
    
    # Déterminer le nom de tous les fichiers HTML du répertoire page_directory
    html_files_name = [f for f in os.listdir(page_directory_path_name) if f.endswith('.html')]

    # Garder un seul de ces fichiers et récupérer son chemin
    html_file_path_name = os.path.join(page_directory_path_name, html_files_name[0])
    
    # Écrire le nom du chemin vers la page HTML dans le champ "path" de page_informations
    page_informations["path"] = html_file_path_name

    # Utiliser le package BeautifulSoup
    with open(html_file_path_name, "r") as f:
        doc = BeautifulSoup(f, "html.parser")
    
    # Écrire le numéro de la page dans le champ "number" de page_informations
    page_informations["number"] = page_number

    # Écrire le titre de la page dans le champ "title" de page_informations
    page_informations["title"] = doc.title.string

    # Écrire la discussion ayant lieu dans la page comme une liste de str dans le champ "discussion" de page_informations
    page_informations["discussion"] = [chat.get_text(strip=True) for chat in doc.find_all('div', class_="boardCommentContent")]
    
    if len(page_informations["discussion"]) <= 1:
        page_informations = {}
    else:
        try:
            text = page_informations["discussion"][0]
            _length=len(text.split())
            _min_length=_length if _length <  20  else  20
            _max_length=_length if _length < 150  else 150
            print("min length = {} max length = {} length = {}".format(_min_length, _max_length, _length))
            page_informations["summary"] = summarizer(text, min_length=_min_length, max_length=_max_length)
        except:
            page_informations["summary"] = "FATAL: Exception raised while calling pipeline"
    return page_informations

def set_forum_data_2_json(forum_data, json_file_path_name, append):
    """
    set_forum_data_2_json - Écrit les données des forums dans un fichier JSON.

    Arguments:
        forum_data (dict): Les données des forums (voir la fonction get_forum_data pour le format).
        json_file_path_name (str): Le nom du chemin vers le fichier JSON.
        append (bool): Indique que les données des forums seront ajoutées au fichier JSON, et ils n'écraseront donc pas les données existantes. Si le fichier JSON n'existe pas, il sera créé.
    
    Exemple:
        forum_data = get_forum_data("/home/projects/stage-cea-chatbot/data/forums/")
        set_forum_data_2_json(forum_data, "/home/projects/stage-cea-chatbot/data/json/forums.json", True)
    """
    
    if append:
        # Vérifier si le fichier existe
        if os.path.exists(json_file_path_name):
            # Lire les données existantes du fichier JSON
            with open(json_file_path_name, 'r') as file:
                existing_forum_data = json.load(file)
        else:
            # Initialiser les données si le fichier n'existe pas
            existing_forum_data = {"forums": []}
        for forum_informations in forum_data["forums"]:
            forum_found = False
            for existing_forum_informations in existing_forum_data["forums"]:
                if forum_informations["number"] == existing_forum_informations["number"]:
                    forum_found = True
                    break
            if not forum_found:
                existing_forum_data["forums"].append(forum_informations)
            else:
                for page_informations in forum_informations["pages"]:
                    if page_informations["number"] not in [existing_page_informations["number"] for existing_page_informations in existing_forum_informations["pages"]]:
                        existing_forum_informations["pages"].append(page_informations)
    else:
        existing_forum_data = forum_data

    with open(json_file_path_name, 'w', encoding='utf-8') as file:
        json.dump(existing_forum_data, file, ensure_ascii=False, indent=4)
