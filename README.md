

# 1 **Présentation du Projet AppTicket**

## **1.1 Introduction**

L'objectif du projet **AppTicket**, réalisé dans le cadre de notre **BTS SIO**, est de concevoir et développer une application web de gestion de tickets d'incidents. Cette application vise à améliorer la gestion des demandes d'assistance et à optimiser le suivi des problèmes rencontrés par les utilisateurs.

Le projet repose sur une architecture **Flask** pour la partie backend,  **SQLAlchemy** et **MySql** pour la gestion des données, et une interface web facilitant l'interaction avec les utilisateurs.

## **1.2 Recueil des Besoins**

Avant de lancer l'implémentation, nous avons réalisé un **recueil des besoins** afin d'affiner les exigences du projet. Cette phase a permis de mieux comprendre les attentes des futurs utilisateurs et d'adapter l'architecture de l'application en conséquence.

### **1.2.1 Méthodologie employée**

Nous avons procédé en plusieurs étapes :

-   **Questionnaire en ligne envoyé à des professionnels du secteur** pour identifier les besoins et attentes.
-   **Analyse des processus existants** afin d’identifier les améliorations possibles.
-   **Benchmarking** des solutions existantes pour identifier les bonnes pratiques.
-   **Définition des cas d'utilisation** et formalisation des exigences fonctionnelles et non fonctionnelles.

### **1.2.2 Principaux besoins identifiés**

Suite à cette analyse, nous avons défini les fonctionnalités clés du projet :

1.  **Création et gestion des tickets** avec des statuts clairs (ouvert, en cours, résolu, fermé).
2.  **Authentification et gestion des utilisateurs** avec des rôles distincts (utilisateur, support, administrateur).
3.  **Système de notifications** (email/SMS) pour informer les utilisateurs des mises à jour sur leurs tickets.
4.  **Gestion des priorités et assignation des tickets** aux membres du support.
5.  **Historique et traçabilité** des interventions sur chaque ticket.
6.  **Tableau de bord et statistiques** pour suivre la performance du support.
7.  **API REST** permettant l’intégration avec d’autres systèmes internes.

## **1.3 Conception et Architecture**

Sur la base des besoins recueillis, nous avons conçu une architecture modulaire avec les composants suivants :

### **1.3.1 Architecture technique**

-   **Backend (Flask + SQLAlchemy)** : Gère les routes API, la logique métier et l’accès à la base de données.
-   **Base de données (MySQL)** : Stocke les informations des utilisateurs, tickets, et logs d'activités.
-   **Frontend (HTML/CSS/JS)** : Fournit une interface utilisateur intuitive et ergonomique.
-   **Système de notification (SMTP/SMS)** : Permet d’envoyer des alertes en fonction des actions des utilisateurs.
-   **Authentification sécurisée** avec gestion des rôles et permissions.


## **1.4 Implémentation et Développements**

-  **Phase 1 : Recueil du besoin** et rédaction du cahier des charge
-  **Phase 2 : Mise en place de l’architecture** et création des bases de données.
-   **Phase 3 : Développement des fonctionnalités principales** (gestion des tickets, authentification, notifications).
-   **Phase 4 : Tests unitaires et intégration** pour valider la stabilité de l’application.
-   **Phase 5: Mise en production.**

```mermaid
gantt
    title GANTT
    dateFormat DD-MM-YYYY
    section Phase 1
        Rédaction et diffusion d’un questionnaire en ligne auprès des professionnels du secteur:a1, 01-10-2024, 2d
        Étude des outils existants et de leurs limites :a2, after a1, 2d
        Recueil des besoins des utilisateurs finaux (employés, techniciens, responsables): a3, after a2, 5d
        Analyse des réponses et identification des fonctionnalités clés:a5, after a3, 1d
        Définition des cas d’utilisation (user stories, scénarios d’utilisation):a6, after a5, 3d
        Rédaction des exigences fonctionnelles et non fonctionnelles:a7, after a6, 3d
        Rédaction du cahier des charges:a8, after a7, 5d
    section Phase 2
        Définition des composants techniques (backend, frontend, base de données, API):b1, after a8, 2d
        Choix des technologies et des frameworks (Flask, SQLAlchemy, MySQL, etc.):b2, after b1, 1d
        Planification de l’infrastructure (hébergement, sécurité, sauvegarde):b3, after b2, 2d
        Mise en place d’un dépôt Git:b4, after b3, 1d
        Identification des entités et relations (tickets, utilisateurs, rôles, logs):b5, after b4, 5d
        Création Modèle Conceptuel de Données:b6, after b5, 5d
        Rédaction des scripts SQL pour la structure initiale de la base.:b7, after b6, 5d
        Installation des outils et dépendances (Python, Flask, SQLAlchemy, etc.).:b8, after b3, 3d
        Configuration de l’environnement de développement (Docker, virtualenv).:b9, after b8, 1d
    section Phase 3
        Création des modèles de base de données (tickets, utilisateurs, rôles):c1, after b6, 5d
        Gestion de l’authentification et des autorisations:c2, after c1, 3d
        Intégration des formulaires de connexion et d’inscription:c3, after c1, 3d
        Mise en place des routes API pour la gestion des tickets:c4, after c2, 10d
        Création et gestion des différents statuts de ticket (ouvert, en cours, fermé):c5, after c3, 3d
        Implémentation du système de notifications (email/SMS):c6, after c5, 10d
        Interface pour la création et le suivi des tickets:c7, after c6, 10d
        Création du tableau de bord utilisateur:c8, after c7, 5d
        Système d’assignation et de priorisation des tickets:c9, after c8, 5d
        Ajout d’une base de connaissances pour l’assistance:c10, after c9, 10d
        Gestion des rapports et statistiques sur les incidents:c11, after c10, 5d
        Automatisation de certaines tâches (relance automatique des tickets non traités):c12, after c11, 5d
    section Phase 4
        Création des tests unitaires pour chaque fonctionnalité clé (pyunit):d1, after c1, 56d
        Vérification de la cohérence des données et du bon fonctionnement des API:d2, after d1, 3d
        Vérification des interactions entre les différents modules:d3, after d2, 3d
        Simulation de scénarios utilisateur et correction des bugs:d4, after d3, 3d
        Tests de performance et optimisation du temps de réponse:d5, after d4, 3d
        Vérification de l’authentification et des autorisations:d6, after d5, 3d
        Analyse des logs et mise en place d’alertes de sécurité:d7, after d6, 3d
    section Phase 5
        Configuration de l’environnement de production (VPS):e1, after d8, 3d
        Mise en place d’une politique de sauvegarde automatique:e2, after e1, 3d
        Déploiement des services backend et frontend:e3, after e2, 3d
        Configuration des domaines et certificats SSL:e4, after e3, 3d
        Mise en place d’un système de surveillance (logs, alertes):e5, after e4, 3d
        Tests finaux avec les utilisateurs et corrections des derniers bugs:e6, after e5, 3d
```

# 2 **Résumé des Systèmes de Gestion des Incidents et des Demandes de Maintenance**

## **2.1 Actuel : Signalement des incidents et outils utilisés**
- **Moyens de signalement** : GLPI, appels téléphoniques, tickets, JIRA, Teams.
- **Outils/canaux en place** : GLPI, mails, Office 365 (Teams, Outlook), Slack, Zoom, Google Workspace.
- **Problèmes majeurs** :
  - Limites techniques et coûts.
  - Logs incomplets, difficulté d'assigner un ticket à plusieurs personnes.
  - Multiplicité des systèmes pour les demandes hors ticketing.

## **2.2 Volumes et Périodes**
- **Incidents traités/semaine** :
  - 20% traitent 1 à 2 incidents.
  - 30% gèrent 5 à 10 incidents.
  - 20% gèrent 10 à 20 incidents.
  - 30% dépassent les 20 incidents.
- **Périodes de pointe** :
  - Les lundis matins et après-midi.
  - Après les mises à jour, en dehors des vacances scolaires.

---

## **2.3 Attentes pour une nouvelle application**
1. **Simplicité d’utilisation** (employés et techniciens).
2. **Fonctionnalités clés** :
   - Suivi détaillé (nouveau, en cours, clos...).
   - Notifications par email, SMS.
   - Gestion des dépendances entre tickets.
3. **Modularité** :
   - Plugins et intégrations (ex : Azure Active Directory, Grafana).
   - Possibilité de lier tickets internes/externes.
4. **Automatisation** : Processus simplifiés et rapides.
5. **Rapports** :
   - Temps de résolution, volumes, problèmes récurrents.
   - Rapports hebdomadaires/mensuels.
6. **Conformité** : Respect du RGPD et des normes internes.

---

## **2.4 Préférences utilisateurs**
- **Signalement** : Formulaires en ligne, téléphone avec alertes directes.
- **Suivi des tickets** :
  - Notifications par email/SMS.
  - Statut du ticket, délais, nom du technicien.
  - Fréquence : à chaque changement ou toutes les heures si besoin.
- **Première réponse** : Entre 1 et 2 jours.
- **Matériel utilisé** : PC, tablettes, smartphones.

---

## **2.5 Préférences techniciens**
- **Réception des tickets** : Mail (listes de diffusion), dashboard, bots Slack.
- **Catégorisation** :
  - Type (matériel/logiciel), priorité, état actuel.
  - Affectation par service/opérateur avec des délais pour l’acceptation et le traitement.
- **Indicateurs importants** :
  - Volume de tickets traités, temps de résolution, nombre de tickets en retard.
- **Outils additionnels** :
  - Base de connaissances, chat utilisateur/technicien, liaison des tickets.

---

## **2.6 Besoins responsables**
- **Rapports souhaités** :
  - Tickets par service, temps moyen de résolution, problèmes récurrents.
  - Fréquence : hebdomadaire (lundi 10h) ou mensuelle.
- **Accès aux données** :
  - Utilisateurs standards : uniquement leurs tickets.
  - Responsables : vision globale et rapports.
- **Base de connaissances** : FAQ, guides, procédures.

---

## **Autres besoins**
- **Déploiement** : Préférences variées (cloud, serveur local).
- **Sauvegardes** :
  - Sauvegarde quotidienne/hebdomadaire (tickets, logs, base de connaissances).
  - Continuité de service pendant les heures de travail.
 
# 3 **Comparaisons des outils existants**

# 4 **Définition des cas d’utilisation**

# 5 **Exigences fonctionnelles et non fonctionnelles**

# 6 **Modèle conceptuel de données**

# Structure du projet

```plaintext

AppTicket/
│
├── app/  # Contient le code source de l'application Flask
│   ├── __init__.py  # Fichier d'initialisation pour l'application Flask
│   ├── config.py  # Configuration de l'application (base de données, environnement, etc.)
│   ├── models/  # Contient les modèles SQLAlchemy
│   │   ├── __init__.py  # Fichier d'initialisation pour les modèles
│   │   ├── user.py  # Modèle pour les utilisateurs
│   │   ├── ticket.py  # Modèle pour les tickets d'incidents
│   │   └── ...  # Autres modèles 
│   ├── routes/  # Contient les routes (endpoints API)
│   │   ├── __init__.py  # Fichier d'initialisation pour les routes
│   │   ├── user_routes.py  # Routes liées aux utilisateurs
│   │   ├── ticket_routes.py  # Routes pour la gestion des tickets
│   │   └── ...  # Autres routes si nécessaires
│   ├── services/  # Contient la logique métier
│   │   ├── __init__.py
│   │   ├── notification_service.py  # Service pour gérer les notifications (email/SMS)
│   │   ├── ticket_service.py  # Logique pour le traitement des tickets
│   │   └── ...  # Autres services si nécessaires
│   ├── templates/  # Contient les templates HTML 
│   │   ├── base.html  # Template de base
│   │   ├── ticket.html  # Page pour visualiser les tickets
│   │   └── ...  # Autres templates
│   ├── static/  # Fichiers statiques (CSS, JS, images)
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   └── ...
│   ├── utils/  # Utilitaires pour le projet
│   │   ├── __init__.py
│   │   ├── MySqlConnector.py  # Configuration et connexion à la base de données
│   │   ├── security.py  # Gestion de la sécurité (chiffrement des mots de passe, etc.)
│   │   └── email.py  # Code pour envoyer des emails
│   └── errors/  # Gestion des erreurs
│       ├── __init__.py
│       ├── handlers.py  # Gestion des erreurs personnalisées
│       └── ...
│
├── tests/  # Contient les tests
│   ├── __init__.py
│   ├── test_user.py  # Tests pour les utilisateurs
│   ├── test_ticket.py  # Tests pour les tickets
│   ├── test_routes.py  # Tests pour les routes APIg
│   └── ...  # Autres fichiers de tests
│
├── docs/  # Documentation du projet
│   ├── README.md  # Documentation principale
│   ├── API.md  # Documentation des endpoints API
│   ├── INSTALL.md  # Instructions d'installation
│   └── ...
├── docker/  # Fichiers liés à la configuration Docker
│   ├── Dockerfile  # Dockerfile pour l'application Flask
│   ├── docker-compose.yml  # Configuration Docker Compose
│   ├── nginx/  # Configuration pour le reverse proxy
│   │   └── nginx.conf
│   └── scripts/  # Scripts utiles pour le container
│       └── entrypoint.sh  # Entrypoint pour initialiser le conteneur
│
├── .env  # Fichier pour les variables d'environnement
├── .gitignore  # Fichiers à ignorer par Git
├── requirements.txt  # Dépendances Python
├── run.py  # Point d'entrée principal de l'application Flask
└── README.md  # Documentation générale du projet
```
