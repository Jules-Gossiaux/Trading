import multiprocessing
import time

def run_script(script_id, duration):
    print(f"Exécution du script {script_id} dans le processus : {multiprocessing.current_process().name}")
    time.sleep(duration)  # Simule un travail qui prend du temps
    print(duration)
    print(f"Script {script_id} terminé")