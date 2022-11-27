from sqlite3 import Timestamp
import exbitron
import hashlib, hmac

import json
import math
import time
import sys




# Written by @DanielBoye

# Sette default API keys. Må bli endret selv i python filen
client = exbitron.Client(
    access_key = "",
    secret_key = "",
)


btc_price = client.get("/api/v2/peatio/public/markets/btcusdt/depth?limit=1")
btc_last_trade = client.get("/api/v2/peatio/public/markets/btcusdt/trades?limit=1")

btc_ask = float(btc_price['asks'][0][0])
btc_bid = float(btc_price['bids'][0][0])
btc_price = float(btc_last_trade[0]['price'])

a = (btc_ask - btc_bid)
spread = (a/btc_price) * 100

print(f"Spread er på {round(spread, 2)}%")

print(f"\nBitcoin ask: {btc_ask}")
print(f"\nBitcoins bid: {btc_bid}")
print(f"\nSiste trade var på {btc_price}")




