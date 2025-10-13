# 📚 Bibliothèque - Gestionnaire de Livres

Une application de bureau moderne développée en Python avec PyQt6 pour gérer votre collection de livres personnelle.

![Python](https://img.shields.io/badge/python-v13.7+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.9.1-green.svg)


## 🌟 Fonctionnalités

- **Interface graphique moderne** avec PyQt6
- **Gestion complète des livres** : ajout, suppression, modification
- **Stockage local** en format JSON
- **Écran de démarrage** avec splash screen
- **Interface à onglets** pour une navigation intuitive
- **Sauvegarde automatique** des données

## 📁 Structure du Projet

```
bibliotheque/
├── app/
│   ├── data/
│   │   └── book.py              # Modèle de données Book
│   ├── service/
│   │   ├── addBook.py           # Service d'ajout de livres
│   │   ├── fileManager.py       # Gestionnaire de fichiers JSON
│   │   └── modify_book.py       # Service de modification
│   ├── start/
│   │   ├── splash.py            # Écran de démarrage
│   │   └── startup_dialog.py    # Dialogue d'initialisation
│   └── ui/
│       ├── main_window.py       # Fenêtre principale
│       ├── components/
│       │   ├── booktab.py       # Onglet de gestion des livres
│       │   ├── menubar.py       # Barre de menu
│       │   └── navigationBar.py # Barre de navigation
│       └── window/
│           └── setting.py       # Fenêtre des paramètres
├── ressources/
│   └── images/                  # Ressources graphiques
├── main.py                      # Point d'entrée de l'application
├── config.py                    # Configuration de l'application
├── data.json                    # Base de données JSON des livres
└── requirements.txt             # Dépendances Python
```

## 🚀 Installation

### Prérequis

- Python 3.13.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation des dépendances

1. **Clonez le repository** :
```bash
git clone https://github.com/Clement-Szewczyk/bibliotheque.git
cd bibliotheque
```

2. **Créez un environnement virtuel** (recommandé) :
```bash
python -m venv env
```

3. **Activez l'environnement virtuel** :
   - **Windows** :
   ```bash
   env\Scripts\activate
   ```
   - **Linux/macOS** :
   ```bash
   source env/bin/activate
   ```

4. **Installez les dépendances** :
```bash
pip install -r requirements.txt
```

## 💻 Utilisation

### Démarrage de l'application

```bash
python main.py
```

### Fonctionnalités principales

1. **Ajout d'un livre** :
   - Utilisez le menu ou les boutons d'interface
   - Remplissez les informations : titre, auteur, genre, année, ISBN
   - Marquez comme "à vendre" si nécessaire

2. **Gestion des livres** :
   - Visualisez tous vos livres dans l'onglet principal
   - Supprimez ou modifiez les entrées existantes
   - Les données sont sauvegardées automatiquement

3. **Stockage des données** :
   - Les livres sont stockés dans `data.json`
   - Sauvegarde automatique à chaque modification
   - Format JSON lisible et portable

## 🛠️ Développement

### Architecture

L'application suit une architecture modulaire :

- **`app/data/`** : Modèles de données (classe Book)
- **`app/service/`** : Services métier (gestion fichiers, CRUD)
- **`app/ui/`** : Interface utilisateur (fenêtres et composants)
- **`app/start/`** : Séquence de démarrage

### Modèle de données

La classe `Book` contient les attributs suivants :
- `id` : Identifiant unique auto-généré
- `title` : Titre du livre
- `author` : Auteur
- `genre` : Genre littéraire
- `year` : Année de publication
- `isbn` : Numéro ISBN
- `sale` : Statut de vente (boolean)


## 📦 Dépendances

Les principales dépendances incluent :

- **PyQt6** (6.9.1) : Framework d'interface graphique

Voir `requirements.txt` pour la liste complète.

## 🐛 Problèmes connus

- Les modifications de livres sont en cours de développement
- Interface de recherche avancée à implémenter
- Style et thème personnalisables à venir

## 👨‍💻 Auteur

**Clement Szewczyk**
- GitHub: [@Clement-Szewczyk](https://github.com/Clement-Szewczyk)
