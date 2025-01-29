import sys
import os

# Ajouter le chemin du projet pour permettre l'importation des modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import MagicMock, patch
from app.utils.mysqlconnector import MySqlConnector

class TestMySqlConnector(unittest.TestCase):
    def setUp(self):
        # Initialisation de l'objet MySqlConnector avec des valeurs fictives
        self.db = MySqlConnector("localhost", "test_db", "test_user", "test_password")
        # Mock de la session SQLAlchemy pour éviter d'utiliser une vraie base de données
        self.db.session = MagicMock()

    def test_user_exist(self):
        # Simule qu'un utilisateur existe dans la base de données
        self.db.session.query().filter_by().first.return_value = MagicMock()
        self.assertTrue(self.db.userExist("testuser"))

    @patch("app.utils.mysqlconnector.logging")
    def test_add_user(self, mock_logging):
        # Simule qu'un utilisateur n'existe pas encore
        self.db.userExist = MagicMock(return_value=False)
        self.assertTrue(self.db.addUser("newuser", "hash", "email", "role", "phone"))

    def test_get_user_hash(self):
        # Simule la récupération du mot de passe haché d'un utilisateur
        mock_user = MagicMock(password="hashed_pass")
        self.db.session.query().filter_by().first.return_value = mock_user
        self.assertEqual(self.db.get_user_hash("testuser"), "hashed_pass")

if __name__ == "__main__":
    unittest.main()
