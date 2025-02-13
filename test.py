# import du module mysql.connector
from mysql.connector import connect, DatabaseError, InterfaceError
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

# connexion à une base MySql [dbpersonnes]
# l'identité de l'utilisateur est (admpersonnes,nobody)
USER = DB_USER
PWD = DB_PASSWORD
HOST = DB_HOST
DATABASE = DB_NAME

# c'est parti
connexion = None
try:
    print("Connexion au SGBD MySQL en cours...")
    # connexion
    connexion = connect(host=HOST, user=USER, password=PWD, database=DATABASE)
    # suivi
    print(
        f"Connexion MySQL réussie à la base database={DATABASE}, host={HOST} sous l'identité user={USER}, passwd={PWD}")
except (InterfaceError, DatabaseError) as erreur:
    # on affiche l'erreur
    print(f"L'erreur suivante s'est produite : {erreur}")
finally:
    # on ferme la connexion si elle a été ouverte
    if connexion:
        connexion.close()