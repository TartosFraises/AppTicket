from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

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

    def userExist(self, user_name: str) -> bool:
        """
        Vérifie si un utilisateur existe dans la table User.

        Args:
            user_name (str): Nom de l'utilisateur.

        Returns:
            bool: True si l'utilisateur existe, False sinon.
        """
        return self.session.query(User).filter_by(nom=user_name).first() is not None

    def addUser(self, user_name: str, email: str):
        """
        Ajoute un utilisateur dans la table User.

        Args:
            user_name (str): Nom de l'utilisateur.
            email (str): Adresse email.
        """
        # Vérifie si l'utilisateur existe déjà
        if self.userExist(user_name):
            print(f"L'utilisateur {user_name} existe déjà.")
            return

        # Crée un nouvel utilisateur
        new_user = User(nom=user_name, email=email)
        self.session.add(new_user)  # Ajoute à la session
        self.session.commit()  # Sauvegarde dans la base
        print(f"Utilisateur {user_name} ajouté avec succès.")
