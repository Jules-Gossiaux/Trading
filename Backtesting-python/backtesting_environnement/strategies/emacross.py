class Strat(Strategy):
    parametre1 = params1  # exemple de valeur par défaut
    parametre2 = params2  # exemple de valeur par défaut

    def init(self):
        # Initialisation des moyennes mobiles exponentielles
        self.ema1 = self.I(EMA, pd.Series(self.data.Close), self.parametre1)
        self.ema2 = self.I(EMA, pd.Series(self.data.Close), self.parametre2)

    def next(self):
        # Croisement des EMA pour les signaux d'achat et de vente
        if crossover(self.ema1, self.ema2):
            self.buy()
        elif crossover(self.ema2, self.ema1):
            self.sell()


# class EmaCross(Strategy):
#     def init(self):
#         # Initialisation des moyennes mobiles exponentielles
#         self.ema1 = self.I(pd.Series.ewm, self.data.Close, span=10).mean()
#         self.ema2 = self.I(pd.Series.ewm, self.data.Close, span=20).mean()

#     def next(self):
#         # Croisement des EMA pour les signaux d'achat et de vente
#         if crossover(self.ema1, self.ema2):
#             self.buy()
#         elif crossover(self.ema2, self.ema1):
#             self.sell()
