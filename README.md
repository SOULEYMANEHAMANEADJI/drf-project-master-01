# **Django REST Framework - V1-3005**

Un projet Django REST Framework complet développé en suivant un tutoriel pratique et enrichi avec des ressources supplémentaires pour maîtriser tous les aspects du développement d'API REST avec Django.

## 🎯 **À propos du projet**

Ce projet est le résultat d'un apprentissage approfondi de Django REST Framework, combinant un tutoriel principal avec diverses ressources complémentaires. Il démontre une progression logique des concepts de base aux fonctionnalités avancées avec des exemples pratiques et du code réel.

## 📚 **Concepts couverts**

### **Fondamentaux**
- Introduction aux APIs et REST
- Installation et configuration Django/DRF
- Structure de projet et bonnes pratiques
- Endpoints et routing

### **Modèles et Sérialisation**
- Création de modèles Django
- Sérialisation manuelle vs automatique
- Validation des données
- Relations entre modèles

### **Patterns de vues**
- **Function-Based Views (FBV)** - API Students
- **Class-Based Views (CBV)** - API Employees
- **Mixins** - Réutilisation de code
- **Generics** - Vues prêtes à l'emploi
- **ViewSets** - Approche moderne et flexible

### **Opérations CRUD complètes**
- Création (POST)
- Lecture (GET) - liste et détail
- Mise à jour (PUT/PATCH)
- Suppression (DELETE)

### **Fonctionnalités avancées**
- **Pagination** - Globale et personnalisée
- **Filtrage** - Simple et avancé avec django-filter
- **Recherche** - Recherche textuelle
- **Tri** - Ordonnancement des résultats
- **Relations imbriquées** - Blogs et commentaires

## 🏗️ **Structure du projet**

```
drf-project-master-01/
├── 📁 api/                    # App API principale avec vues centralisées
├── 📁 blogs/                  # App blogs avec système de commentaires
├── 📁 django_rest_main/       # Configuration Django et settings
├── 📁 employees/              # App employés avec ViewSets
├── 📁 students/               # App étudiants avec FBV
├── 📁 venv/                   # Environnement virtuel Python
├── 📄 db.sqlite3             # Base de données SQLite
├── 📄 manage.py               # Script de gestion Django
└── 📄 notes.txt               # Notes de développement
```

## 🛠 **Installation et configuration**

### **Prérequis**
- Python 3.8+
- pip
- Environnement virtuel (inclus)

### **Démarrage rapide**

```bash
# 1. Cloner le projet
git clone 
cd drf-project-master-01

# 2. Activer l'environnement virtuel
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Installer les dépendances
pip install djangorestframework
pip install django-filter
pip install django-schema-viewer

# 4. Configuration base de données
python manage.py makemigrations
python manage.py migrate

# 5. Créer un superutilisateur
python manage.py createsuperuser

# 6. Lancer le serveur
python manage.py runserver
```

## 📚 **APIs disponibles**

### **Students API (Function-Based Views)**
```
GET    /api/students/          # Liste tous les étudiants
POST   /api/students/          # Créer un étudiant
GET    /api/students/{id}/     # Détails d'un étudiant
PUT    /api/students/{id}/     # Modifier un étudiant
DELETE /api/students/{id}/     # Supprimer un étudiant
```

### **Employees API (ViewSets avec pagination)**
```
GET    /api/employees/         # Liste paginée des employés
POST   /api/employees/         # Créer un employé
GET    /api/employees/{id}/    # Détails d'un employé
PUT    /api/employees/{id}/    # Modifier un employé
DELETE /api/employees/{id}/    # Supprimer un employé
```

### **Blogs API (avec recherche et tri)**
```
GET    /api/blogs/             # Liste des blogs (recherche/tri)
POST   /api/blogs/             # Créer un blog
GET    /api/blogs/{id}/        # Détails d'un blog
PUT    /api/blogs/{id}/        # Modifier un blog
DELETE /api/blogs/{id}/        # Supprimer un blog
```

### **Comments API**
```
GET    /api/comments/          # Liste des commentaires
POST   /api/comments/          # Créer un commentaire
GET    /api/comments/{id}/     # Détails d'un commentaire
PUT    /api/comments/{id}/     # Modifier un commentaire
DELETE /api/comments/{id}/     # Supprimer un commentaire
```

## ⚙️ **Configuration DRF**

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 2,
    'DEFAULT_FILTER_BACKENDS': 'django_filters.rest_framework.DjangoFilterBackend'
}
```

## 🔍 **Fonctionnalités de filtrage**

### **Pagination**
- Pagination automatique avec LimitOffset
- Navigation next/previous
- Taille de page configurable

### **Filtrage employés**
```
/api/employees/?designation=Developer
/api/employees/?emp_gender=Male
```

### **Recherche dans les blogs**
```
/api/blogs/?search=django
/api/blogs/?search=rest framework
```

### **Tri**
```
/api/blogs/?ordering=blog_title
/api/blogs/?ordering=-id
```

## 🧪 **Tests et validation**

```bash
# Exécuter tous les tests
python manage.py test

# Tests par application
python manage.py test students
```

## 📖 **Documentation**

- **API navigable** : `http://localhost:8000/api/`
- **Admin Django** : `http://localhost:8000/admin/`
- **Schema viewer** : Disponible avec django-schema-viewer

## 🚀 **Déploiement**

### **Préparation production**
1. Configurer `DEBUG = False`
2. Définir `ALLOWED_HOSTS`
3. Utiliser PostgreSQL en production
4. Configurer les fichiers statiques
5. Variables d'environnement sécurisées

## 💡 **Points d'apprentissage clés**

- **Progression logique** : Des vues simples aux ViewSets avancés
- **Patterns multiples** : Comparaison FBV vs CBV vs ViewSets
- **Fonctionnalités réelles** : Pagination, filtrage, recherche
- **Bonnes pratiques** : Structure de code, sérialisation, validation
- **Évolutivité** : Architecture modulaire et extensible

## 🤝 **Contribution**

Ce projet est ouvert aux améliorations et suggestions. N'hésitez pas à proposer des optimisations ou de nouvelles fonctionnalités.

## Author : SHA
