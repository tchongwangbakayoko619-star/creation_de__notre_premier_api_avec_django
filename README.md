# Django API Project

Une API RESTful simple créée avec Django pour gérer des produits.

## Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Clonez le dépôt:**
```bash
git clone https://github.com/tchongwangbakayoko619-star/creation_de__notre_premier_api_avec_django.git
cd "création de notre premier api avec django"
```

2. **Créez un environnement virtuel:**
```bash
python -m venv venv
```

3. **Activez l'environnement virtuel:**

Sur Windows:
```bash
venv\Scripts\Activate.ps1
```

Sur macOS/Linux:
```bash
source venv/bin/activate
```

4. **Installez les dépendances:**
```bash
pip install -r requirements.txt
```

5. **Appliquez les migrations:**
```bash
cd backends
python manage.py migrate
```

6. **Démarrez le serveur Django:**
```bash
python manage.py runserver
```

Le serveur sera disponible à `http://localhost:8000`

## Structure du projet

```
.
├── backends/              # Application Django principale
│   ├── api/              # Application API
│   │   ├── models.py     # Modèles de données
│   │   ├── views.py      # Vues API
│   │   ├── urls.py       # Routes API
│   │   └── ...
│   ├── core/             # Configuration du projet
│   │   ├── settings.py   # Configuration Django
│   │   ├── urls.py       # Routes principales
│   │   └── ...
│   ├── manage.py         # Utilitaire de gestion Django
│   └── db.sqlite3        # Base de données
├── client/               # Client pour tester l'API
│   ├── create_product.py # Script de création de produit
│   └── ...
├── venv/                 # Environnement virtuel
├── requirements.txt      # Dépendances du projet
└── README.md            # Ce fichier
```

## Utilisation de l'API

### Créer un produit

Exécutez le script client:
```bash
cd client
python create_product.py
```

### Points de terminaison (Endpoints)

- **GET** `/api/` - Liste/information générale
- **POST** `/api/` - Créer un produit

### Payload exemple

```json
{
    "name": "Product 1",
    "price": 9.99,
    "description": "This is a sample product",
    "created_at": "2024-06-01T12:00:00Z",
    "updated_at": "2024-06-01T12:00:00Z"
}
```

## Technologies utilisées

- **Django 6.0** - Framework web Python
- **SQLite** - Base de données
- **Requests** - Client HTTP Python

## Licence

Ce projet est sous licence MIT.

## Auteur

TCHONGWANG BAKAYOKO
