import sys
sys.path.append("/Users/cvonkrogh/Private/github.com/InverseETFSimulator")
import Underlying
import InverseETF
import HistoricalPrices

def main():
    allPricesByBlocksize(250)


def allPrices():

    underlying = Underlying.Underlying("SPY")
    inverseETF = InverseETF.InverseETF(underlying)

    PRICE_LIST_HUGE = HistoricalPrices.SPY['All']

    underlying.setPricelist(PRICE_LIST_HUGE)
    printItWithTitle(underlying, inverseETF, '1950 to present')

    # what exactly is the research of interest here?
    # how about bucketizing 5-year blocks?
    # it should not be rocket science that these things
    #   A) never lose more than initial principal
    #   B) do not provide a predictable hedge
    #   C) lose money in cases of price_a -> price_b -> price_a

def allPricesByBlocksize(blockSize):
    underlying = Underlying.Underlying("SPY")
    inverseETF = InverseETF.InverseETF(underlying)

    PRICE_LIST_HUGE = HistoricalPrices.SPY['All']

    total_slices = len(PRICE_LIST_HUGE) / blockSize

    whoWon = {
        'iETF'     : 0,
        'short'    : 0,
        'tie'      : 0,
        }

    for slice in range(0, total_slices):
        offset = slice * blockSize
        sublist = PRICE_LIST_HUGE[offset:offset+blockSize]
        underlying.setPricelist(sublist)

        shortPnl = underlying.shortPnl()
        pnl = inverseETF.pnl()
        shortYield = underlying.shortPercentageYield()
        ietfyield = inverseETF.percentageYield()

        if shortPnl > pnl:
            whoWon['short'] = whoWon['short'] + 1
        elif pnl > shortPnl:
            whoWon['iETF'] = whoWon['iETF'] + 1
        else:
            whoWon['tie'] = whoWon['tie'] + 1

    print "--------", "blocksize=" + str(blockSize), "--------"
    print "trials:", total_slices
    print "short wins:", whoWon['short']
    print "iETF wins:", whoWon['iETF']
    print "tie:", whoWon['tie']


def main_old():
    underlying = Underlying.Underlying("SPY")
    inverseETF = InverseETF.InverseETF(underlying)

    underlying.setPricelist([100,80,100])
    printIt(underlying, inverseETF)

    #underlying.setPricelist([100,80,100, 80])
    #printIt(underlying, inverseETF)

    underlying.setPricelist(HistoricalPrices.SPY['Mar2015'])
    printIt(underlying, inverseETF)

    underlying.setPricelist(HistoricalPrices.SPY['Feb2015'])
    printItWithTitle(underlying, inverseETF, 'Feb 2015')

    underlying.setPricelist(HistoricalPrices.SPY['Jan2015'])
    printItWithTitle(underlying, inverseETF, 'Jan 2015')

    key='2014'
    underlying.setPricelist(HistoricalPrices.SPY[key])
    printItWithTitle(underlying, inverseETF, key)

    key='2013'
    underlying.setPricelist(HistoricalPrices.SPY[key])
    printItWithTitle(underlying, inverseETF, key)

    pricelist = HistoricalPrices.SPY['2013'] + HistoricalPrices.SPY['2014']
    underlying.setPricelist(pricelist)
    printItWithTitle(underlying, inverseETF, '2013 and 2014')

    key='2000s'
    underlying.setPricelist(HistoricalPrices.SPY[key])
    printItWithTitle(underlying, inverseETF, key)

    underlying.setPricelist(HistoricalPrices.NASDAQ['Mar102kToPresent'])
    printItWithTitle(underlying, inverseETF, 'NASDAQ 5k to now')

    pass

def printItWithTitle(underlying, inverseETF, title):
    print "--------", title, "--------"
    print "PnL (short, IETF) = ", underlying.shortPnl(), inverseETF.pnl()
    print "Yield (short, IETF) = ", underlying.shortPercentageYield(), inverseETF.percentageYield()

def printIt(underlying, inverseETF):
    printItWithTitle(underlying, inverseETF, "")

main()
