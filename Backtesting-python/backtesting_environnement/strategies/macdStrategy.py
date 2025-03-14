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
