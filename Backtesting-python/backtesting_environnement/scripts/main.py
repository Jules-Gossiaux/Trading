import multiprocessing
from allBacktest import test

# if __name__ == '__main__':
#     # Nombre de fois que vous voulez exécuter le script
#     num_executions = 5

#     # Créer et démarrer les processus
#     processes = []
#     for i in range(num_executions):
#         # Passer des arguments différents pour chaque exécution
#         process = multiprocessing.Process(target=run_script, args=(i, i+1))
#         processes.append(process)
#         process.start()

#     # Attendre que tous les processus se terminent
#     for process in processes:
#         process.join()

#     print("Tous les processus sont terminés")

if __name__ == '__main__':
    # Nombre de fois que vous voulez exécuter le script
    num_executions = 5

    # Créer et démarrer les processus
    processes = []
    for i in range(num_executions):
        # Passer des arguments différents pour chaque exécution
        process = multiprocessing.Process(target=test, args=(2, 5, 5, 1, i+1))
        processes.append(process)
        process.start()

    # Attendre que tous les processus se terminent
    for process in processes:
        process.join()

    print("Tous les processus sont terminés")