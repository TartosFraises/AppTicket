# Résumé des Systèmes de Gestion des Incidents et des Demandes de Maintenance

## **Actuel : Signalement des incidents et outils utilisés**
- **Moyens de signalement** : GLPI, appels téléphoniques, tickets, JIRA, Teams.
- **Outils/canaux en place** : GLPI, mails, Office 365 (Teams, Outlook), Slack, Zoom, Google Workspace.
- **Problèmes majeurs** :
  - Limites techniques et coûts.
  - Logs incomplets, difficulté d'assigner un ticket à plusieurs personnes.
  - Multiplicité des systèmes pour les demandes hors ticketing.

## **Volumes et Périodes**
- **Incidents traités/semaine** :
  - 20% traitent 1 à 2 incidents.
  - 30% gèrent 5 à 10 incidents.
  - 20% gèrent 10 à 20 incidents.
  - 30% dépassent les 20 incidents.
- **Périodes de pointe** :
  - Les lundis matins et après-midi.
  - Après les mises à jour, en dehors des vacances scolaires.

---

## **Attentes pour une nouvelle application**
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

## **Préférences utilisateurs**
- **Signalement** : Formulaires en ligne, téléphone avec alertes directes.
- **Suivi des tickets** :
  - Notifications par email/SMS.
  - Statut du ticket, délais, nom du technicien.
  - Fréquence : à chaque changement ou toutes les heures si besoin.
- **Première réponse** : Entre 1 et 2 jours.
- **Matériel utilisé** : PC, tablettes, smartphones.

---

## **Préférences techniciens**
- **Réception des tickets** : Mail (listes de diffusion), dashboard, bots Slack.
- **Catégorisation** :
  - Type (matériel/logiciel), priorité, état actuel.
  - Affectation par service/opérateur avec des délais pour l’acceptation et le traitement.
- **Indicateurs importants** :
  - Volume de tickets traités, temps de résolution, nombre de tickets en retard.
- **Outils additionnels** :
  - Base de connaissances, chat utilisateur/technicien, liaison des tickets.

---

## **Besoins responsables**
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
