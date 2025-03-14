class Strat(Strategy):
    parametre1 = params1
    parametre2 = params2
    parametre3 = params3

    def init(self):
        # Initialisation de l'indicateur RSI avec des paramètres
        self.rsi = self.I(RSI, self.data.Close, self.parametre1)

    def next(self):
        # Signaux d'achat et de vente basés sur le RSI
        if self.rsi[-1] > self.parametre2:
            self.sell()
        elif self.rsi[-1] < self.parametre3:
            self.buy()

# class RsiStrategy(Strategy):
#     rsi_period = 14
#     rsi_upper = 70
#     rsi_lower = 30

#     def init(self):
#         # Initialisation de l'indicateur RSI avec des paramètres
#         self.rsi = self.I(RSI, self.data.Close, self.rsi_period)

#     def next(self):
#         # Signaux d'achat et de vente basés sur le RSI
#         if self.rsi[-1] > self.rsi_upper:
#             self.sell()
#         elif self.rsi[-1] < self.rsi_lower:
#             self.buy()




# # Fonction de backtesting modifiée pour afficher le capital de départ, le capital final et le drawdown max
# def perform_backtest(data):
#     import warnings
#     warnings.filterwarnings('ignore', category=UserWarning)

#     #change les prametres de la stratégie
#     RsiStrategy.rsi_period = params1
#     RsiStrategy.rsi_upper = params2
#     bt = Backtest(data, RsiStrategy, cash=10000, commission=.002)
#     output = bt.run()
    

#     # Extraction des informations
#     capital_depart = 10000  # Capital initial donné à l'argument cash lors de la création du Backtest
#     capital_final = output['Equity Final [$]']
#     drawdown_max = output['Max. Drawdown [%]']

#     # Affichage des informations
#     print(f"Capital de départ : {capital_depart}")
#     print(f"Capital final : {capital_final}")
#     print(f"Drawdown maximum : {drawdown_max}%")

#     return output