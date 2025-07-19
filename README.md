# Hello World – Exemple for UNRAID App

Ce dépôt fournit un exemple minimal de microservice Python :
- Lecture d'une config JSON
- Serveur web HTTP affichant un message custom

## Structure du projet
- `config/config.json` : configuration (port, message)
- `main.py` : serveur HTTP principal
- `requirements.txt` : dépendances Python (aucune ici)
- `update.sh` : installation des dépendances (modulable par le dev)
- `start.sh` : script de démarrage du projet

## Utilisation (hors Docker)

```bash
sh update.sh
sh start.sh
```
