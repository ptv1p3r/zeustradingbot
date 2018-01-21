import gdax
import ConfigParser
import locale

class ZeusChart(object):
    def __init__(self, pair, period):
        config = ConfigParser.ConfigParser()
        config.read("zeus.ini")
        locale.setlocale(locale.LC_ALL, 'pt_PT.utf8')

        self.conn = gdax.AuthenticatedClient(config.get("auth", "key"), config.get("auth", "secret"), config.get("auth", "passphrase"))
        self.pair = pair
        self.period = period

        self.data = []

    def getCurrentPrice(self):
        listG = self.conn.get_product_ticker(product_id=self.pair)
        # self.data = locale.atof(listG['price'])
        # currentValues = locale.atof(listG['price'])
        lastPairPrice = {}
        # lastPairPrice = currentValues[self.pair]["last"]
        lastPairPrice = locale.atof(listG['price'])

        return lastPairPrice
