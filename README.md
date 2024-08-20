# Stage-CEA-ChatBot

Stage-CEA-ChatBot est le rendu de mon stage au CEA. J'ai utilisé le langage Python tout au long du stage.

## Table des matières

- [Informations générales](##informations-générales)
- [Installation](#installation)
- [Usage](#usage)
- [Structure](#structure)
- [Explication](#explication)
- [À Faire](#à-faire)
- [Auteur](#auteur)

## Informations générales

- **Date de création**: 26 juin 2024
- **Auteur**: Kelvin LEFORT
- **Sujet**: Explorer les possibilités de mettre en place un bot IA local, entraîné pour répondre aux questions autour de la plateforme SALOME
- **Version**: 1.0.0
- **Nom du système d'exploitation utilisé pendant le stage**: Ubuntu 22.04.4 LTS

## Installation

Avant de commencer les installations, je tiens à préciser que l'environnement virtuel Python devra rester activé tout au long de l'utilisation du projet. Il pourra être désactivé seulement quand vous souhaitez arrêter d'utiliser mon projet.

Voici les étapes à suivre pour installer un environnement virtuel Python :

1. Créez (si ce n'est pas déjà fait) un répertoire `envs` dans le répertoire personnel : `mkdir $HOME/envs`
2. Déplacez-vous dans ce répertoire : `cd $HOME/envs`
3. Installez l'environnement virtuel Python dans ce répertoire : `python -m venv stage-cea-chatbot`

Voici les étapes à suivre pour activer/désactiver l'environnement :

1. Pour activer l'environnement (à effectuer une seule fois au début de chaque session quand vous souhaitez utiliser mon projet) : `source $HOME/envs/stage-cea-chatbot/bin/activate`
2. Pour désactiver l'environnement (à réaliser seulement lorsque vous souhaitez arrêter d'utiliser mon projet) : `deactivate`

Voici l'étape à suivre pour installer les dépendances nécessaires :

1. Installez toutes les dépendances nécessaires à partir du fichier `requirements.txt` : `pip install -r requirements.txt`

Voici les étapes à suivre pour installer Jupyter dans l'environnement :

1. Installez Jupyter dans l'environnement : `pip install jupyter`
2. Vérifiez que Jupyter est bien installé dans l'environnement : `which jupyter`

Voici l'étape à suivre pour installer IPython Kernel for Jupyter dans l'environnement :

1. Installez IPython Kernel for Jupyter dans l'environnement : `pip install ipykernel`

Voici l'étape à suivre pour installer un noyau IPython (kernel) pour Jupyter Notebook avec un nom personnalisé et un affichage spécifique :

1. Tapez la commande suivante : `python -m ipykernel install --user --name=stage-cea-chatbot --display-name "Python (stage-cea-chatbot)"`

## Usage

Pour lancer JupyterLab (pour exécuter/éditer les fichiers NOTEBOOK), tapez la commande suivante : `jupyter lab`

L'exécution d'un script Python dépend des arguments et options qu'il attend. Deux options sont possibles :

- Le script n'attend aucuns arguments et aucunes options. Il suffit dans ce cas de taper la commande : `python script_path_name`
- Le script attend un/des argument(s) et/ou une/des option(s). Le cas échéant, pour trouver les informations nécessaires à l'exécution du script, tapez la commande : `python script_path_name --help`

## Structure

Pour mieux travailler, j'ai structuré intelligemment mon répertoire de travail. Voici l'explication de cette structure :

- **`data/`**: Contient tous les fichiers de données (JSON et JSON Lines).
- **`models/`**: Contient les sauvegardes des modèles.
- **`notebooks`**: Contient tous les fichiers NOTEBOOK réalisés/utilisés pendant le stage.
- **`packages`**: Contient les packages Python créés et développés durant le stage.
- **`scripts`**: Contient tous les scripts Python réalisés/utilisés pendant le stage.

## Explication

Donnons à présent une explication détaillée de chaque fichier :

## À Faire

Je n'ai malheureusement pas eu le temps de tout accomplir. Voici une liste exhaustive de ce qui resterait à faire :

- Rédiger un rapport

## Auteur

- **Kelvin LEFORT** - *Stagiaire* - [dovinzo](https://github.com/dovinzo)
