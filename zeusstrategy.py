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

        # verifica numero de trades abertas
        for trade in self.trades:
            if trade.status == "OPEN":
                    openTrades.append(trade)

        # se o numero de posicoes abertas for inferior ao numero de trades permitidas
        if len(openTrades) < self.numTrades:
            if self.currentPrice < self.indicators.movingAverage(self.prices, 15):  # se o preco corrente for inferior ao valor da media movel
                self.trades.append(ZeusTrade(self.currentPrice, stopLoss=.0001))  # abre nova posicao

        # verifica as posicoes abertas para fecho
        for trade in openTrades:
            if self.currentPrice > self.indicators.movingAverage(self.prices, 15):  # se o preco corrente for inferior ao valor da media movel
                trade.close(self.currentPrice)  # fecha posicao

    # actualiza posicoes abertas
    def updateOpenTrades(self):
        for trade in self.trades:
            if trade.status == "OPEN":
                trade.tick(self.currentPrice)

    # mostra posicoes
    def showPositions(self):
        for trade in self.trades:
            trade.showTrade()
