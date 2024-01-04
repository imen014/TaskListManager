from BdConnector import BdConnector

class TaskUpdater:
    def __init__(self):
        # Instanciation de la classe BdConnector
        self.connector = BdConnector()

    def update_task(self, task_id, new_title, new_content):
        try:
            # Connexion à la base de données
            self.connector.connect()

            # Récupération de l'objet curseur
            cursor = self.connector.cursor

            # Exemple de requête de mise à jour d'une tâche
            update_query = "UPDATE task SET task_title = %s, task_content = %s WHERE task_id = %s"
            task_data = (new_title, new_content, task_id)

            # Exécution de la requête
            cursor.execute(update_query, task_data)

            # Validation des modifications dans la base de données
            self.connector.conn.commit()

            print("Mise à jour de la tâche réussie.")
        except Exception as e:
            print(f"Erreur lors de la mise à jour de la tâche : {e}")
        finally:
            # Fermeture de la connexion à la base de données
            self.connector.close_connection()

