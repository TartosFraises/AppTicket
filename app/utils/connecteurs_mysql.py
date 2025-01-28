from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import User

class MySqlConnector:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def add_user(self, username, password, email, role, phone_number):
        session = self.Session()
        if session.query(User).filter_by(username=username).first():
            return "Utilisateur déjà existant."
        user = User(username=username, password=password, email=email, role=role, phone_number=phone_number)
        session.add(user)
        session.commit()
        session.close()
        return "Utilisateur ajouté avec succès."

    def get_users(self):
        session = self.Session()
        users = session.query(User).all()
        session.close()
        return users
