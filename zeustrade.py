from zeuslog import ZeusLog


class ZeusTrade(object):
    def __init__(self, currentPrice, stopLoss=0):
        self.output = ZeusLog()
        self.status = "OPEN"
        self.entryPrice = currentPrice
        self.exitPrice = ""
        self.output.log("Trade opened")

        # calcula stoploss caso exista
        if stopLoss:
            self.stopLoss = currentPrice - stopLoss

    # fecha posicao de trade
    def close(self, currentPrice):
        self.status = "CLOSED"
        self.exitPrice = currentPrice
        self.output.log("Trade closed")

    # calcula tick de posicao
    def tick(self, currentPrice):
        if self.stopLoss:
            if currentPrice < self.stopLoss:
                self.close(currentPrice)

    # mostra posicao de trade
    def showTrade(self):
        tradeStatus = "Entry Price: " + str(self.entryPrice) + " Status: " + str(self.status) + " Exit Price: " + str(
            self.exitPrice)

        if self.status == "CLOSED":
            tradeStatus = tradeStatus + " Profit: "
            if self.exitPrice > self.entryPrice:
                tradeStatus = tradeStatus + "\033[92m"
            else:
                tradeStatus = tradeStatus + "\033[91m"

            tradeStatus = tradeStatus + str(self.exitPrice - self.entryPrice) + "\033[0m"

        self.output.log(tradeStatus)
