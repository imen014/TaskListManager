from TaskManager import TaskManager
from TaskDeleter import TaskDeleter
from TaskUpdater import TaskUpdater



# Exemple d'utilisation de la classe TaskManager
task_manager = TaskManager("make breakfast", "cook", "sahar")
#task_manager.insert_task_in_db()

# Exemple d'utilisation de la classe TaskDeleter
task_deleter = TaskDeleter()
#task_deleter.delete_all_tasks()


# Exemple d'utilisation de la classe TaskUpdater
task_updater = TaskUpdater()
task_updater.update_task(11, "Nouveau Titre", "Nouveau Contenu")