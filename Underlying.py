class Underlying:
    def __init__(self, ticker):
        self._ticker = ticker

    # you can put in just a list or anything which overrides __getitem__
    def setPricelist(self, pricelist):
        self._pricelist = pricelist
    def getPricelist(self):
        return self._pricelist
    
    def percentageYield(self):
        return float(self.pnl()) / self._pricelist[0]

    def pnl(self):
        length = len(self._pricelist)
        initialValue = self._pricelist[0]
        finalValue = self._pricelist[length-1]
        pnl = finalValue - initialValue
        return pnl

    def shortPercentageYield(self):
        return self.percentageYield() * -1

    def shortPnl(self):
        return self.pnl() * -1

    pass

