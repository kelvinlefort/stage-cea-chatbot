# Stage-CEA-ChatBot

Stage-CEA-ChatBot est le rendu de mon stage au CEA. J'ai utilisé le langage Python tout au long du stage.

## Table des matières

- [Informations générales](#informations-générales)
- [Dépendances](#dépendances)
- [Installation](#installation)
- [Usage](#usage)
- [Structure](#structure)
- [À Faire](#à-faire)
- [Auteur](#auteur)

## Informations générales

- **Date de création** : 26 juin 2024
- **Auteur** : Kelvin LEFORT
- **Sujet** : Explorer les possibilités de mettre en place un bot IA local, entraîné pour répondre aux questions autour de la plateforme SALOME
- **Version** : 1.0.0
- **Nom du système d'exploitation utilisé pendant le stage** : Ubuntu 22.04.4 LTS

## Dépendances

Voici la liste des dépendances :

- [python3](https://www.python.org/downloads/)
- [python3-venv](https://docs.python.org/3/library/venv.html)
- [pip](https://pypi.org/project/pip/)

## Installation

Avant de commencer les installations, je tiens à préciser que l'environnement virtuel Python devra être activé et le rester tout au long de l'utilisation du projet. Il pourra être désactivé seulement quand vous souhaiterez arrêter d'utiliser mon projet.

#### Cloner le dépôt à partir de Git

```bash
git clone https://github.com/dovinzo/stage-cea-chatbot.git $HOME/stage-cea-chatbot
```

#### Installer un environnement virtuel Python

1. Créez un répertoire `envs` dans le répertoire personnel :
   ```bash
   mkdir -p $HOME/envs
   ```
2. Déplacez-vous dans ce répertoire :
   ```bash
   cd $HOME/envs
   ```
3. Installez l'environnement virtuel Python dans ce répertoire :
   ```bash
   python -m venv stage-cea-chatbot
   ```
   **Note** : Vérifier, en utilisant la commande `ls`, que le sous-répertoire `stage-cea-chatbot` a bien été créé dans le répertoire `$HOME/envs`.

#### Activer l'environnement

1. Pour activer l'environnement :
   ```bash
   source $HOME/envs/stage-cea-chatbot/bin/activate
   ```
   **Note** : Pour vérifier que l'environnement est bien activé, tapez la commande `which python`. Cette commande permet de vérifier quel programme binaire `python` est utilisé lorsqu'on tape la commande `python`. Elle devrait donc retourner le `python` de `$HOME/envs/stage-cea-chatbot/bin/python`.

**Note** : Pour désactiver l'environnement :
   ```bash
   deactivate
   ```

#### Installer les dépendances nécessaires

1. Installez toutes les dépendances nécessaires à partir du fichier `requirements.txt` :
   ```bash
   pip install -r $HOME/stage-cea-chatbot/requirements.txt
   ```

#### Installer Jupyter dans l'environnement

1. Installez Jupyter dans l'environnement :
   ```bash
   pip install jupyter
   ```
   **Note** : Pour vérifier que Jupyter est bien installé dans l'environnement, tapez la commande `which jupyter`. Si le résultat de cette commande n'est pas `$HOME/envs/stage-cea-chatbot/bin/jupyter`, veuillez toujours lancer `$HOME/envs/stage-cea-chatbot/bin/jupyter` au lieu de `jupyter`.

#### Installer IPython Kernel for Jupyter dans l'environnement

1. Installez IPython Kernel for Jupyter dans l'environnement :
   ```bash
   pip install ipykernel
   ```

#### Installer un noyau IPython pour Jupyter Notebook

1. Installez un noyau IPython (kernel) pour Jupyter Notebook avec un nom personnalisé et un affichage spécifique :
   ```bash
   python -m ipykernel install --user --name=stage-cea-chatbot --display-name "Python (stage-cea-chatbot)"
   ```

## Usage

#### Utiliser les fichiers NOTEBOOK

1. Lancez JupyterLab :
   ```bash
   cd $HOME/stage-cea-chatbot && /
   jupyter lab
   ```
   **Note** : Tous les fichiers NOTEBOOK sont contenus dans le répertoire `$HOME/stage-cea-chatbot/notebooks`. Ceux-ci peuvent alors être lancés à partir de JupyterLab.

#### Utiliser les scripts Python

L'exécution d'un script Python dépend des arguments et options qu'il attend. Deux options sont possibles :

- Le script n'attend aucuns arguments et aucunes options. Il suffit dans ce cas de taper la commande :
  ```bash
  python script_path_name
  ```
- Le script attend un/des argument(s) et/ou une/des option(s). Le cas échéant, pour trouver les informations nécessaires à l'exécution du script, tapez la commande :
  ```bash
  python script_path_name --help
  ```

## Structure

Pour mieux travailler, j'ai structuré intelligemment mon répertoire de travail. Voici l'explication de cette structure :

- **`data/`** : Contient tous les fichiers de données (JSON et JSON Lines).
- **`models/`** : Contient les sauvegardes des modèles.
- **`notebooks`** : Contient tous les fichiers NOTEBOOK réalisés/utilisés pendant le stage.
- **`packages`** : Contient les packages Python créés et développés durant le stage.
- **`scripts`** : Contient tous les scripts Python réalisés/utilisés pendant le stage.

## À Faire

Je n'ai malheureusement pas eu le temps de tout accomplir. Voici une liste exhaustive de ce qui resterait à faire :

- Rédiger un rapport

## Auteur

- **Kelvin LEFORT** - *Stagiaire* - [dovinzo](https://github.com/dovinzo)
