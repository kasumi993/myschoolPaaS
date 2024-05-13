# Projet MySchoolPass

## Aperçu

MySchoolPass est une plateforme éducative basée sur Django qui utilise Redis pour les mises à jour en temps réel. Ce projet intègre Django Channels et Celery pour une gestion efficace des tâches et des notifications en direct.

## Fonctionnalités

- Mises à jour en temps réel utilisant Redis pub/sub
- Gestion des cours pour les professeurs et les étudiants
- Authentification des utilisateurs et gestion des profils
- Interface d'administration pour la gestion des utilisateurs et des cours

## Prérequis

- Docker
- Docker Compose

## Instructions d'installation

### 1. Cloner le Référentiel

```bash
git clone https://github.com/kasumi993/myschoolPaaS.git
cd myschoolpaas
```

### 2. Démarrer le projet

```bash
docker-compose up --build
```

Le site demarre sur le port 8000 de localhost: http://localhost:8000/

### 3. Utilisateurs par Défaut pour les Tests
Professeur

Nom d'utilisateur : professor

Mot de passe : professor


Étudiant

Nom d'utilisateur : student

Mot de passe : student


### 4. Exécution du Subscriber
Le subscriber pour les messages Redis est automatiquement démarré avec le conteneur Docker.



