from zeuslog import ZeusLog
import time


class ZeusCandlestick(object):
    def __init__(self, period=100, open=None, close=None, high=None, low=None, priceAverage=None):
        self.current = None
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.startTime = time.time()
        self.period = period
        self.output = ZeusLog()
        self.priceAverage = priceAverage

    def tick(self, price):
        self.current = float(price)

        if self.open is None:   #se ainda nao existe um preco de abertura
            self.open = self.current

        if (self.high is None) or (self.current > self.high):  #se o preco high nao existe ou preco maior que o high
            self.high = self.current

        if (self.low is None) or (self.current < self.low):  #se o preco low nao existe ou preco menor que o low
            self.low = self.current

        if time.time() >= (self.startTime + self.period):  #se o timestamp e maior que i tempo inicial mais o periodo de recolha
            self.close = self.current
            self.priceAverage = (self.high + self.low + self.close) / float(3)

        self.output.log("Open: "+str(self.open)+" Close: "+str(self.close)+" High: "+str(self.high)+" Low: "+str(self.low)+" Current: "+str(self.current))

    def isClosed(self):
        if self.close is not None:
            return True
        else:
            return False
