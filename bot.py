import exbitron
import hashlib, hmac
import requests
from requests.auth import AuthBase
import json
import math
import time
import sys


cg = CoinGeckoAPI()

# Written by @DanielBoye

# Sette default API keys. Må bli endret selv i python filen
client = exbitron.Client(
    access_key = "",
    secret_key = "",
)

# Alle valg til spørsmål om API keys
ja_valg = {'ja', 'JA', 'Ja', 'jA', 'y', 'Y', 'yes', 'Yes', ''}
nei_valg = {'nei', 'Nei', 'no', 'NO', 'No', 'n', 'N'}


# For loading bar
items = list(range(0, 57))
l = len(items)

# Spør om du vil bruke default API keys
while True:
    api_spørsmål = input("\nVil du bruke default API keys? (Y/n) ")
    if api_spørsmål in nei_valg:
        # Spør etter Exbitron API keys
        print("\nSkriv inn dine Exbitron API keys")
        access_key_input = input("\nAccess key: ")
        secret_key_input = input("\nSecret key ")
        
        # Lagrer keysene inn i exbitron clienten
        client = exbitron.Client(
            access_key = access_key_input,
            secret_key = secret_key_input,
        )
        # Litt for debugging, men bare viser at lagringen ble utført
        print("Utført!")
        break
    
    if api_spørsmål in ja_valg:
        break
        # Valge break her siden hvis svaret er ja hopper den bare til neste steg
 
# Funksjon for den falske laster inn baren        
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    
    if iteration == total: 
        print()
print("\n")
printProgressBar(0, l, prefix = 'Loading API:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Rediger tiden for hvor rask den burde lastes inn
    time.sleep(0.0005)
    # Oppdaterer baren 
    printProgressBar(i + 1, l, prefix = 'Loading API:', suffix = 'Complete', length = 50)

# Total value av wallet

btcprice = cg.get_price(ids='hive,steem',vs_currencies='btc')

print(btcprice)


# Hente verdier ifra wallet som oversikt
def oversikt():
    xkr_oversikt = client.get("/api/v2/peatio/account/balances/xkr")
    btc_oversikt = client.get("/api/v2/peatio/account/balances/btc")
    usdt_oversikt = client.get("/api/v2/peatio/account/balances/usdt")
    # TODO
    # Lage en ordreoversikt med hvor mange ordre som er aktive
    #ordre_oversikt = client.get("/api/v2/peatio/market/orders/")
    print("Wallet oversikt:")
    print(f"XKR = {(xkr_oversikt['balance'])}")
    print(f"BTC = {(btc_oversikt['balance'])}")
    print(f"USDT = {(usdt_oversikt['balance'])}")
    #print("Aktive ordre:")
    #print(ordre_oversikt)
print("\nVelkommen tilbake\n")
oversikt()