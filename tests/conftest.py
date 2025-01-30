import sys
import os

# Ajoute le chemin du projet au sys.path pour éviter les erreurs d'import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User

DATABASE_URL = "mysql+pymysql://root:sTr0ngP@ssw0rd!2025@51.75.25.241:3306/TicketsSupport"

@pytest.fixture(scope="session")
def db_engine():
    """Crée une connexion à la base de données pour les tests."""
    engine = create_engine(DATABASE_URL)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    """Crée une session de base de données isolée pour chaque test."""
    connection = db_engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()
    yield session
    session.close()
    transaction.rollback()
    connection.close()

