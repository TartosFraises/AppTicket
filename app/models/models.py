from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    Représente un utilisateur dans la base de données.

    Attributes:
        __tablename__ (str): Nom de la table associée dans la base de données.
        id (int): Identifiant unique de l'utilisateur.
        nom (str): Nom unique de l'utilisateur.
        email (str): Adresse e-mail de l'utilisateur.
    """
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)  # ID unique
    nom = Column(String(255), unique=True, nullable=False)  # Nom unique
    email = Column(String(255), nullable=False)  # Email obligatoire
