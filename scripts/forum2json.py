#!/bin/env python3

"""
Nom du script:
    forum2json.py

Synopsis:
    python chemin/vers/forums2json.py [--help] [--jsonfile VALUE] --forum VALUE  [--append]

Description:
    Ce script récupère les données "essentielles" des forums de la plateforme SALOME se trouvant dans un répetoire pour les placer dans un fichier JSON.

Options:
    --help
        Affiche cette aide et quitte.

    --jsonfile
        Le nom du chemin vers le fichier JSON.
        Exemple: "chemin/vers/fichier.json"
        Par défaut, il s'agit de "./forum.json".
    --forum
        Le nom du chemin vers le répertoire du forum à utiliser.

    --append
        Indique que les données des forums seront ajoutées au fichier JSON, et ils n'écraseront donc pas les données existantes. Si le fichier JSON n'existe pas, il sera créé.

Dépendances: argparse, os, sys, transformers, forum

Auteurs: Nabil GHODBANE et Kelvin LEFORT

Date: 20/08/2024
"""

import argparse
import os
import sys
from transformers import pipeline

# Ajouter le répertoire parent du package 'forum' au PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'packages'))

from forum import get_forum_data, get_page_informations, set_forum_data_2_json

def print_help():
    print(__doc__)
    sys.exit(0)

def get_arguments():
    """
    get_arguments - Récupère les arguments donnés avant l'éxécution du script
    
    Sortie:
        args (argparse.Namespace): Les arguments donnés avant l'éxécution du script
    
    Exemple:
        args = get_arguments()
    """
    
    # Créer le parseur
    parser = argparse.ArgumentParser(add_help=False)
    
    # Ajouter l'option --help
    parser.add_argument('--help', action='store_true')
    
    # Ajouter l'option --json
    parser.add_argument('--jsonfile', type=str)
    
    # Ajouter l'option --append
    parser.add_argument('--append', action='store_true')
    
    # Ajouter l'argument forum
    parser.add_argument('--forum', type=str)
    
    # Analyser les arguments
    args = parser.parse_args()
    
    return args
    
def main():
    """
    main - Fonction principale orchestrant les tâches à effectuer
    """

    # Récupérer les arguments
    args = get_arguments()
    
    # ==================== Gestion des arguments ====================
    if args.help:
        print_help()
    if args.jsonfile is None:
        args.jsonfile = os.path.join(os.getcwd(), 'forum.json')
    if args.forum is None:
        print("Erreur: L'argument --forum est obligatoire") # TODO : À MODIFIER
        sys.exit(0)

    # nombre max de token: max_length=150
    # nombre min de token: min_length=20
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Récupérer les données des forums
    forum_data = get_forum_data(args.forum, summarizer)

    # Écrire les données dans le fichier JSON
    set_forum_data_2_json(forum_data, args.jsonfile, args.append)

if __name__ == "__main__":
    main()
