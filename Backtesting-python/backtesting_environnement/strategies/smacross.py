class Strat(Strategy):
    parametre1 = params1  # exemple de valeur par défaut
    parametre2 = params2  # exemple de valeur par défaut

    def init(self):
        # Initialisation des moyennes mobiles simples
        self.sma1 = self.I(SMA, pd.Series(self.data.Close), self.parametre1)
        self.sma2 = self.I(SMA, pd.Series(self.data.Close), self.parametre2)

    def next(self):
        # Croisement des SMA pour les signaux d'achat et de vente
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()





# class Strat(Strategy):
#     def init(self):
#         self.sma1 = self.I(SMA, self.data.Close, 10)
#         self.sma2 = self.I(SMA, self.data.Close, 20)

#     def next(self):
#         if crossover(self.sma1, self.sma2):
#             self.buy()
#         elif crossover(self.sma2, self.sma1):
#             self.sell()

# class SmaCross(Strategy):
#     def init(self):
#         self.sma1 = self.I(SMA, self.data.Close, params1)
#         self.sma2 = self.I(SMA, self.data.Close, params2)

#     def next(self):
#         if crossover(self.sma1, self.sma2):
#             self.buy()
#         elif crossover(self.sma2, self.sma1):
#             self.sell()


