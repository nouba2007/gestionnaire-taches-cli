# Gestionnaire de tâches en ligne de commande

## 1. Présentation

Ce projet consiste à développer une application Python permettant
de gérer des tâches depuis une interface en ligne de commande.

Il met en pratique la programmation orientée objet, les structures
de données et les algorithmes de recherche et de tri.

## 2. Fonctionnalités

- Ajouter une tâche.
- Afficher les tâches.
- Modifier une tâche.
- Supprimer une tâche.
- Marquer une tâche comme terminée.
- Rechercher une tâche par mot-clé.
- Trier les tâches par priorité.
- Trier les tâches par date limite.
- Trier les tâches par statut.
- Sauvegarder et charger les données au format JSON.

## 3. Technologies utilisées

- Python 3
- Programmation orientée objet
- Git et GitHub
- JSON
- Pytest

## 4. Structures de données et algorithmes

Les tâches sont stockées dans un dictionnaire Python.
L'identifiant de chaque tâche sert de clé.

La recherche est effectuée manuellement par comparaison
des caractères.

Le tri est réalisé avec l'algorithme Merge Sort.

## 5. Installation

Cloner le dépôt :

git clone https://github.com/Nouba2007/gestionnaire-taches-cli.git

Entrer dans le dossier :

cd gestionnaire-taches-cli

Créer un environnement virtuel :

python3 -m venv .venv

Activer l'environnement :

source .venv/bin/activate

Installer les dépendances :

pip install -r requirements.txt

## 6. Exécution

Lancer le programme :

python3 main.py

## 7. Tests

Exécuter les tests :

pytest -v

## 8. Organisation des fichiers

- task.py : modèle Task.
- task_manager.py : gestion des tâches.
- recherche.py : algorithme de recherche.
- tri.py : algorithme Merge Sort.
- sauvegarde.py : sauvegarde JSON.
- utils.py : fonctions utilitaires.
- main.py : interface en ligne de commande.
- tests/ : tests unitaires.
- data/ : stockage des données.

## 9. Versionnage

Le projet est versionné avec Git et hébergé sur GitHub.
Les fonctionnalités sont développées progressivement avec
des commits réguliers.