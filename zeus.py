from zeuschart import ZeusChart
from zeusstrategy import ZeusStrategy
from zeuscandlestick import ZeusCandlestick
import time

def main():

    chart = ZeusChart('ETH-EUR', 10) # inicia recolha na gdax

    strategy = ZeusStrategy() # inicia estrategia

    candlesticks = []
    developingCandlestick = ZeusCandlestick() # inicia candlestick de desenvolvimento

    while True:
        developingCandlestick.tick(chart.getCurrentPrice())

        if developingCandlestick.isClosed():
            candlesticks.append(developingCandlestick)
            strategy.tick(developingCandlestick)
            developingCandlestick = ZeusCandlestick()

        time.sleep(int(10)) # espera 10 segundos


if __name__ == "__main__":
    main()
