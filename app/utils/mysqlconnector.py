import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User

import os
from dotenv import load_dotenv

load_dotenv()

databaseUser = os.getenv('DB_USER')
databasePassword = os.getenv('DB_PASSWORD')
databaseName = os.getenv('DB_NAME')
databaseUrl = os.getenv('DB_URL')

# Configuration du logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class MySqlConnector:
    """
    Classe pour gérer la connexion à MySQL et les interactions avec les utilisateurs.
    """

    def __init__(self, databaseUrl, databaseName, databaseUser, databasePassword):
        """
        Initialise la connexion à MySQL.

        Args:
            databaseUrl (str): Adresse du serveur MySQL.
            databaseName (str): Nom de la base de données.
            databaseUser (str): Nom d'utilisateur MySQL.
            databasePassword (str): Mot de passe MySQL.
        """
        self.DATABASE_URL = f"mysql+pymysql://{databaseUser}:{databasePassword}@localhost/{databaseName}"
        self.engine = create_engine(self.DATABASE_URL)  # Connexion à MySQL
        self.Session = sessionmaker(bind=self.engine)  # Session pour interagir avec la base
        self.session = self.Session()

    def create_tables(self):
        """Crée les tables dans la base de données si elles n'existent pas."""
        Base.metadata.create_all(self.engine)
        logging.info("Tables créées avec succès.")

    def close(self):
        """Ferme la connexion."""
        self.session.close()
        logging.info("Connexion fermée.")

    def userExist(self, username: str) -> bool:
        """
        Vérifie si un utilisateur existe dans la table Users.

        Args:
            username (str): Nom de l'utilisateur.

        Returns:
            bool: True si l'utilisateur existe, False sinon.
        """
        return self.session.query(User).filter_by(username=username).first() is not None

    def get_user_hash(self, username: str) -> str:
        """
        Récupère le hash du mot de passe d'un utilisateur.

        Args:
            username (str): Nom de l'utilisateur.

        Returns:
            str: Hash du mot de passe ou None si l'utilisateur n'existe pas.
        """
        user = self.session.query(User).filter_by(username=username).first()
        return user.hashpassword if user else None  # Correction ici (hashpassword au lieu de password)

    def addUser(self, username: str, hashed_password: str, email: str, role: str, phone_number: str):
        """
        Ajoute un utilisateur dans la table Users.

        Args:
            username (str): Nom de l'utilisateur.
            hashed_password (str): Mot de passe déjà haché.
            email (str): Adresse email.
            role (str): Rôle de l'utilisateur.
            phone_number (str): Numéro de téléphone.
        """
        if self.userExist(username):
            logging.warning(f"L'utilisateur {username} existe déjà.")
            return False

        new_user = User(username=username, hashpassword=hashed_password, email=email, role=role, phone_number=phone_number)
        
        try:
            self.session.add(new_user)
            self.session.commit()
            logging.info(f"Utilisateur {username} ajouté avec succès.")
            return True
        except Exception as e:
            self.session.rollback()  # Évite une transaction bloquée en cas d'erreur
            logging.error(f"Erreur lors de l'ajout de l'utilisateur {username}: {e}")
            return False