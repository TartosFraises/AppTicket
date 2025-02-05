from sqlalchemy import Column, Enum, Integer, String
from run import db  # Importer db depuis le fichier principal où il est initialisé

class User(db.Model):
    __tablename__ = 'Users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    hashpassword = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    role = db.Column(db.Enum('user', 'technician', 'admin', name='user_roles'), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
