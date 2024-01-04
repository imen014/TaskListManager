from BdConnector import BdConnector
import mysql.connector

class TaskDeleter:
    def __init__(self):
        # Utilisation de l'objet BdConnector pour gérer la connexion à la base de données
        self.connector = BdConnector()

    def delete_all_tasks(self):
        try:
            # Connexion à la base de données
            self.connector.connect()

            # Création d'un objet curseur
            cursor = self.connector.cursor

            # Requête pour supprimer toutes les tâches de la table 'task'
            requete = "DELETE FROM task"

            # Exécution de la requête
            cursor.execute(requete)

            # Validation des modifications dans la base de données
            self.connector.conn.commit()

            print("Toutes les tâches ont été supprimées avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression des tâches : {e}")
        finally:
            # Fermeture de la connexion à la base de données
            self.connector.close_connection()


