#!/bin/sh
set -e

# Mise à jour des dépendances à chaque boot
sh update.sh

# Lancement du serveur
python main.py

# Ici le dev peut ajouter d'autres commandes