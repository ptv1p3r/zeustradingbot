from zeuslog import ZeusLog
from zeusindicators import ZeusIndicators
from zeustrade import ZeusTrade


class ZeusStrategy(object):
    def __init__(self):
        self.output = ZeusLog()
        self.prices = []
        self.closes = []
        self.trades = []
        self.currentPrice = ""
        self.currentClose = ""
        self.numTrades = 1

        self.indicators = ZeusIndicators()

    def tick(self, candlestick):
        self.currentPrice = float(candlestick.priceAverage)
        self.prices.append(self.currentPrice)

        self.output.log("Price: " + str(candlestick.priceAverage) + "\tMoving Average: " + str(self.indicators.movingAverage(self.prices, 15)))

        self.indicators.movingAverage(self.prices, 15)

        self.evaluatePositions()
        self.updateOpenTrades()

        self.showPositions()

    def evaluatePositions(self):
        openTrades = []
        for trade in self.trades:
            if trade.status == "OPEN":
                    openTrades.append(trade)

            if len(openTrades) < self.numTrades:
                if self.currentPrice < self.indicators.movingAverage(self.prices, 15):
                    self.trades.append(ZeusTrade(self.currentPrice, stopLoss=.0001))

            for trade in openTrades:
                if self.currentPrice > self.indicators.movingAverage(self.prices, 15):
                    trade.close(self.currentPrice)

    def updateOpenTrades(self):
        for trade in self.trades:
            if trade.status == "OPEN":
                trade.tick(self.currentPrice)

    def showPositions(self):
        for trade in self.trades:
            trade.showTrade()
