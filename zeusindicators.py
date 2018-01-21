import numpy


class ZeusIndicators(object):
    def __init__(self):
        pass

    # media movel basica
    def movingAverage(self, dataPoints, period):
        if len(dataPoints) > 1:
            return sum(dataPoints[-period:]) / float(len(dataPoints[-period:]))

    def momentum(self, dataPoints, period=14):
        if len(dataPoints) > period -1:
            return dataPoints[-1] * 100 / dataPoints[-period]

    def EMA(self, prices, period):
        x = numpy.asarray(prices)
        weights = None
        weights = numpy.exp(numpy.linspace(-1., 0., period))
        weights /= weights.sum()

        a = numpy.convolve(x, weights, mode='full')[:len(x)]
        a[:period] = a[period]
        return a

    def MACD(self, prices, nslow=26, nfast=12):
        emaslow = self.EMA(prices, nslow)
        emafast = self.EMA(prices, nfast)
        return emaslow, emafast, emafast - emaslow