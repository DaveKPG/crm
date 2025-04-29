CRM
 CRM est une application web conçue pour aider les entreprises à gérer efficacement leurs relations clients. Développée avec Django, elle permet de créer, lire, mettre à jour et supprimer (CRUD) des informations clients de manière intuitive et sécurisée.

🚀 Fonctionnalités
🔐 Authentification utilisateur (connexion / déconnexion)

👤 Gestion des clients : création, modification, suppression

🗂️ Vue d’ensemble de tous les clients

🔎 Recherche et filtrage des données clients

📈 Interface simple, responsive et prête à l’emploi

🛠️ Technologies utilisées
Python 3

Django

SQLite3 (par défaut)

HTML/CSS (Bootstrap) pour l’interface

⚙️ Installation
Clone le dépôt :

bash
Copier
Modifier
git clone https://github.com/tonpseudo/notes-crm.git
cd notes-crm
Crée un environnement virtuel (optionnel mais recommandé) :

bash
Copier
Modifier
python -m venv venv
source venv/bin/activate  # sous Windows : venv\Scripts\activate
Installe les dépendances :

bash
Copier
Modifier
pip install -r requirements.txt
Applique les migrations :

bash
Copier
Modifier
python manage.py migrate
Lance le serveur :

bash
Copier
Modifier
python manage.py runserver
Accède à l’app via : http://localhost:8000

