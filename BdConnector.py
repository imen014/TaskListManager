import mysql.connector

class BdConnector:
    def __init__(self):
        self.host = "127.0.0.1"
        self.username = "sahar"
        self.password = "sahar123*"
        self.bdName = "bdtask"
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            # Établir une connexion à la base de données
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.bdName
            )

            # Créer un objet curseur
            self.cursor = self.conn.cursor()
            print("Connexion à la base de données réussie.")

        except mysql.connector.Error as err:
            print(f"Erreur de connexion à la base de données : {err}")

    def close_connection(self):
        # Fermer le curseur et la connexion
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Connexion à la base de données fermée.")

# Exemple d'utilisation de la classe
bd_connector = BdConnector()
bd_connector.connect()

# Utilisez bd_connector.cursor pour exécuter des requêtes SQL

# Fermez la connexion lorsque vous avez terminé
bd_connector.close_connection()
