from BdConnector import  BdConnector


class TaskManager:
    def __init__(self, task_title, task_content, task_creator):
        self.task_title = "make breakfast"
        self.task_content = "cook"
        self.task_creator = "sahar"

    def insert_task_in_db(self):
        connector = BdConnector()
        connector.connect()

        # Vous pouvez utiliser connector.cursor pour exécuter des requêtes SQL
        cursor = connector.cursor

        # Exemple d'insertion d'une tâche dans une table fictive 'tasks'
        insert_query = "INSERT INTO task (task_title, task_content, task_creator) VALUES (%s, %s, %s)"
        task_data = (self.task_title, self.task_content, self.task_creator)

        try:
            cursor.execute(insert_query, task_data)
            connector.conn.commit()
            print("Tâche insérée avec succès dans la base de données.")
        except Exception as e:
            print(f"Erreur lors de l'insertion de la tâche : {e}")
        finally:
            connector.close_connection()


