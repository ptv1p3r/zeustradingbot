import gdax
import datetime, time
import ConfigParser
from zeuslog import ZeusLog


config = ConfigParser.ConfigParser()
config.read("zeus.ini")

pair = "BTC_EUR"

auth_client = gdax.AuthenticatedClient(config.get("auth", "key"), config.get("auth", "secret"), config.get("auth", "passphrase"))

accounts = auth_client.get_accounts()

#print(accounts)

#print "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + 'logged'

newLog = ZeusLog()

newLog.log(auth_client.get_product_ticker(product_id='ETH-EUR'))

# class WebsocketClient(gdax.WebsocketClient):
#     def on_open(self):
#         self.url = "wss://ws-feed.gdax.com/"
#         self.products = ["ETH-EUR"]
#         self.message_count = 0
#         # print("Lets count the messages!")
#
#     def on_message(self, msg):
#         self.message_count += 1
#         if 'price' in msg and 'type' in msg:
#             print ("Message type:", msg["type"], "@ {:.3f}".format(float(msg["price"])))
#
#     def on_close(self):
#         print("-- Goodbye! --")
#
#
# wsClient = WebsocketClient()
# wsClient.start()
#
# print(wsClient.url, wsClient.products)
#
# while wsClient.message_count < 500:
#     print ("message_count =", "{} ".format(wsClient.message_count))
#     time.sleep(1)
# wsClient.close()
