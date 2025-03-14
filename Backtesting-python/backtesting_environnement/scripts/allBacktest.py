import warnings
warnings.filterwarnings('ignore', category=FutureWarning, module='backtesting')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import asyncio
import concurrent.futures
import multiprocessing
import time

#Faire en sorte de backtester sur fichiers telechargés
#ranger les fichiers
#Faire de l'asynchrone
#Faire des stratégies avec tp et sl
# # Fonction pour télécharger des données historiques
# def download_data(ticker, start_date, end_date):
#     data = yf.download(ticker, start=start_date, end=end_date)
#     data['Date'] = data.index
#     return data

# # Exemple de téléchargement de données
# ticker = 'AAPL'  # Symbole boursier de l'action Apple
# start_date = '2020-01-01'
# end_date = '2023-01-01'

# data = download_data(ticker, start_date, end_date)
# print(data.head())

def read_data_from_csv(filename):
    data = pd.read_csv(filename)
    data['Datetime'] = pd.to_datetime(data['Datetime'])
    data.set_index('Datetime', inplace=True)
    return data

# Exemple de lecture de données à partir d'un fichier CSV local
filename = 'data/1min/BTCUSDT-1m-binance-30K.csv'  # Remplacez par le nom de votre fichier CSV
data = read_data_from_csv(filename)
print(data.head())




#definitions des indicateurs
def RSI(data, period):
    series = pd.Series(data)
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def MACD(data, short_period=12, long_period=26, signal_period=9):
    short_ema = pd.Series(data).ewm(span=short_period, adjust=False).mean()
    long_ema = pd.Series(data).ewm(span=long_period, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    return macd, signal

def EMA(data, period):
    return data.ewm(span=period, adjust=False).mean()

def SMA(data, period):
    return data.rolling(window=period).mean()






# parametres du backtest
params1 = 1
params2 = 1
params3 = 1
step_params1 = 15
step_params2 = 15
step_params3 = 15




# Script de la stratégie
class Strat(Strategy):
    parametre1 = params1
    parametre2 = params2
    parametre3 = params3
    def init(self):
        # Initialisation des indicateurs MACD et Signal
        macd, signal = MACD(self.data.Close, self.parametre1, self.parametre2, self.parametre3)
        self.macd = self.I(lambda: macd)
        self.signal = self.I(lambda: signal)

    def next(self):
        # Si le MACD croise au-dessus du Signal, c'est un signal d'achat
        if crossover(self.macd, self.signal):
            self.buy()
        # Si le MACD croise en-dessous du Signal, c'est un signal de vente
        elif crossover(self.signal, self.macd):
            self.sell()








# Fonction de backtesting modifiée pour afficher le capital de départ, le capital final et le drawdown max
def perform_backtest(data):
    import warnings
    warnings.filterwarnings('ignore', category=UserWarning)

    #change les prametres de la stratégie
    Strat.parametre1 = params1
    Strat.parametre2 = params2
    Strat.parametre3 = params3
    bt = Backtest(data, Strat, cash=10000, commission=.002)
    output = bt.run()
    

    # Extraction des informations
    capital_depart = 10000  # Capital initial donné à l'argument cash lors de la création du Backtest
    capital_final = output['Equity Final [$]']
    drawdown_max = output['Max. Drawdown [%]']

    # Affichage des informations
    # print(f"Capital de départ : {capital_depart}")
    # print(f"Capital final : {capital_final}")
    # print(f"Drawdown maximum : {drawdown_max}%")

    return output
perform_backtest(data)







# boucle de backtest
# Appel de la fonction perform_backtest avec vos données


# result = perform_backtest(data)
best_result = 0
bests_params = [params1, params2]
# capital_final = result['Equity Final [$]']



# #Boucle à deux params
# while params1 < 5:
#     params2 = 1
#     while params2 < 5:
#         result = perform_backtest(data)
#         capital_final = result['Equity Final [$]']

#         if capital_final > best_result:
#             best_result = capital_final
#             bests_params = [params1,  params2]
#         print(Strat.parametre1, Strat.parametre2)
#         params2 = params2 + step_params2
#     params1 = params1 + step_params1

# Boucle à trois params
# def test(limit1, limit2, limit3, step_params, numberStart):
#     global params1, params2, params3, best_result, bests_params, capital_final
#     while params1 < 50:
#         params2 = 1
#         while params2 < 50:
#             params3=numberStart
#             while params3<50:
#                 result = perform_backtest(data)
#                 capital_final = result['Equity Final [$]']

#                 if capital_final > best_result:
#                     best_result = capital_final
#                     bests_params = [params1,  params2, params3]
#                 print(Strat.parametre1, Strat.parametre2, Strat.parametre3)
#                 params3 = params3+step_params
#             params2 = params2 + 1

#         params1 = params1 + 1
        
#     print("les meilleurs parametres sont: ", bests_params, "et le meilleur résultat est: ", best_result)


# # run(10, 20, 30)
# async def run_test():
#     await asyncio.get_event_loop().run_in_executor(None, test)

# def run(limit1, limit2, limit3):
#     global step_params1, step_params2, step_params3

#     # Défini par combien vont évoluer les params
#     step_params = limit3 / 2

#     # Nombre de machines
#     numberMachine = max(limit1, limit2, limit3) / 2

#     # Exécution asynchrone de la fonction test
#     loop = asyncio.get_event_loop()
#     tasks = [asyncio.ensure_future(run_test()) for _ in range(int(numberMachine))]
#     loop.run_until_complete(asyncio.gather(*tasks))
#     loop.close()

# run(5, 5, 5)

def test(limit1, limit2, limit3, step_params, numberStart=1):
    global params1, params2, params3, best_result, bests_params, capital_final
    while params1 < limit1:
        params2 = 1
        while params2 < limit2:
            params3 = numberStart
            while params3 < limit3:
                result = perform_backtest(data)
                capital_final = result['Equity Final [$]']

                if capital_final > best_result:
                    best_result = capital_final
                    bests_params = [params1, params2, params3]
                # print(Strat.parametre1, Strat.parametre2, Strat.parametre3)
                params3 = params3 + step_params
            params2 = params2 + 1
            numberStart += 1
        params1 = params1 + 1
        numberStart = 1
    print("les meilleurs parametres sont: ", bests_params, "et le meilleur resultat est: ", best_result)

test(20, 20, 20, 1, 1)