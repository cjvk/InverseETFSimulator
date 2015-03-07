class InverseETF:
    def __init__(self, underlying):
        self._underlying = underlying
        self.inversePrices = None

    def pnl(self):
        self.calculate()
        l = len(self.inversePrices)
        initialValue = self.inversePrices[0]
        finalValue = self.inversePrices[l-1]
        pnl = finalValue - initialValue
        return pnl

    def percentageYield(self):
        return float(self.pnl()) / self.inversePrices[0]

    def calculate(self):
        underlyingPrices = self._underlying.getPricelist()

        underlyingPercentages = [None]
        inversePercentages = [None]
        for i in range(1, len(underlyingPrices)):
            previousValue = underlyingPrices[i-1]
            currentValue = underlyingPrices[i]
            pnl = currentValue - previousValue
            percentage = float(pnl) / previousValue
            underlyingPercentages.append(percentage)
            inversePercentages.append(-1 * percentage)

        inversePrices = [underlyingPrices[0]]
        for i in range(1, len(inversePercentages)):
            previousValue = inversePrices[i-1]
            currentValue = float(previousValue) * (1 + inversePercentages[i])
            inversePrices.append(currentValue)

        self.inversePrices = inversePrices
