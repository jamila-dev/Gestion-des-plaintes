
# Gestion-des-plaintes
=======
# Projet ERP - Odoo 17

Ce projet est une infrastructure ERP basée sur **Odoo 17**, déployée via **Docker** pour faciliter le développement et le déploiement. Il inclut un module spécifique pour la **Gestion des Plaintes Internes**.

## 🚀 Technologies Utilisées
- **Odoo 17.0** (Community Edition)
- **PostgreSQL 16** (Base de données)
- **Docker & Docker Compose**

## 📂 Structure du Projet
- `odoo-docker/` : Contient la configuration Docker.
  - `addons/` : Répertoire des modules personnalisés (ex: `tp_gestion_plaintes`).
  - `config/` : Fichiers de configuration Odoo (`odoo.conf`).
  - `odoo-web-data/` : Stockage persistant pour les fichiers, images et sessions.
  - `docker-compose.yml` : Configuration des services Odoo et PostgreSQL.

## 🛠️ Modules Personnalisés
### Gestion des Plaintes Internes (`tp_gestion_plaintes`)
Ce module permet de gérer le cycle de vie des plaintes au sein d'une organisation :
- Création et suivi des plaintes.
- Configuration des catégories de plaintes.
- Génération de rapports PDF.
- Gestion des droits d'accès (Sécurité).

## 📥 Installation et Lancement
1. Assurez-vous que Docker et Docker Compose sont installés.
2. Naviguez vers le dossier `odoo-docker/`.
3. Lancez les containers :
   ```bash
   docker-compose up -d
   ```
4. Accédez à Odoo via `http://localhost:8069`.

## ⚙️ Configuration
Le fichier `docker-compose.yml` est configuré pour monter automatiquement les modules présents dans `./addons` et les données persistantes dans `./odoo-web-data`.
>>>>>>> f55b614 (1er commit)
