import numpy as np


class arbitrageModel:

    def __init__(self, quotenliste, gesamtEinsatz=100):
        self.quotes = np.array(quotenliste)
        self.prob = np.around((1/self.quotes) * 100, 2)
        self.comMarMar = np.sum(self.prob)
        self.gesamtEinsatz = gesamtEinsatz
        self.einsatz = np.around(((self.gesamtEinsatz*self.prob)/self.comMarMar), 2)
        self.profit = 0

    def getProbabilities(self):
        return self.prob

    def getCombinedMarketMargin(self):
        return self.comMarMar

    def arbitrageOpportunity(self):
        if self.comMarMar < 100:
            return True, np.around(100 - self.comMarMar, 2)
        else:
            return False, np.around(100 - self.comMarMar, 2)

    def getProfit(self):
        self.profit = np.around(self.einsatz * self.quotes - self.gesamtEinsatz, 2)
        return self.profit
