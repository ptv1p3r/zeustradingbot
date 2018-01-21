from zeuschart import ZeusChart
from zeusstrategy import ZeusStrategy
from zeuscandlestick import ZeusCandlestick
import time

def main():

    chart = ZeusChart('ETH-EUR', 10)

    strategy = ZeusStrategy()

    candlesticks = []
    developingCandlestick = ZeusCandlestick()

    while True:
        developingCandlestick.tick(chart.getCurrentPrice())

        if developingCandlestick.isClosed():
            candlesticks.append(developingCandlestick)
            strategy.tick(developingCandlestick)
            developingCandlestick = ZeusCandlestick()

        time.sleep(int(10))


if __name__ == "__main__":
    main()
