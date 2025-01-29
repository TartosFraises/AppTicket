from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User
import bcrypt

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
        self.DATABASE_URL = f"mysql+pymysql://{databaseUser}:{databasePassword}@{databaseUrl}/{databaseName}"
        self.engine = create_engine(self.DATABASE_URL)  # Connexion à MySQL
        self.Session = sessionmaker(bind=self.engine)  # Session pour interagir avec la base
        self.session = self.Session()

    def create_tables(self):
        """Crée les tables dans la base de données si elles n'existent pas."""
        Base.metadata.create_all(self.engine)
        print("Tables créées avec succès.")

    def close(self):
        """Ferme la connexion."""
        self.session.close()
        print("Connexion fermée.")

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
        return user.password if user else None

    def addUser(self, username: str, password: str, email: str, role: str, phone_number: str):
        """
        Ajoute un utilisateur dans la table Users.

        Args:
            username (str): Nom de l'utilisateur.
            password (str): Mot de passe à hacher.
            email (str): Adresse email.
            role (str): Rôle de l'utilisateur.
            phone_number (str): Numéro de téléphone.
        """
        if self.userExist(username):
            print(f"L'utilisateur {username} existe déjà.")
            return False

        # Hachage du mot de passe avant stockage
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        new_user = User(username=username, password=hashed_password, email=email, role=role, phone_number=phone_number)
        self.session.add(new_user)
        self.session.commit()
        print(f"Utilisateur {username} ajouté avec succès.")
        return True
