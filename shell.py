import os
import exbitron
import hashlib, hmac
import requests
import json
import math
import time
import sys
from cmd import Cmd

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

btc_price = client.get("/api/v2/peatio/public/markets/btcusdt/depth?limit=1")
btc_last_trade = client.get("/api/v2/peatio/public/markets/btcusdt/trades?limit=1")

# Spør om du vil bruke default API keys
while True:
    api_spørsmål = input("\nVil du bruke default API keys? Hvis du konfigurerte de i filen, si ja (Y/n) ")
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


# All kode for input som blir akseptert i shellet
class exbitron_shell(Cmd):
    prompt = 'exbitron >> '
    intro = """
    _______  __ ____  ______________  ____  _   __     ___    ____  ____     _____ __  __________    __ 
   / ____/ |/ // __ )/  _/_  __/ __ \/ __ \/ | / /    /   |  / __ \/  _/    / ___// / / / ____/ /   / / 
  / __/  |   // __  |/ /  / / / /_/ / / / /  |/ /    / /| | / /_/ // /      \__ \/ /_/ / __/ / /   / /  
 / /___ /   |/ /_/ // /  / / / _, _/ /_/ / /|  /    / ___ |/ ____// /      ___/ / __  / /___/ /___/ /___
/_____//_/|_/_____/___/ /_/ /_/ |_|\____/_/ |_/    /_/  |_/_/   /___/     /____/_/ /_/_____/_____/_____/
    
    \nVelkommen tilbake!\n\nSkriv ? for å få en liste over alle kommandoene til programmet   
    """

    # Alle mulige kommandoer
    
    # Exit
    def do_exit(self, inp):
        print("\nGår ut at av Exbitron API SHELL")
        time.sleep(0.5)
        return True
    def help_exit(self):
        print('Lukke applikasjonen')
    # Tøm skjermen
    def do_clear(self, inp):
        os.system('cls')
    def help_clear(self):
        print("Tømmer terminalskjermen.")
    
    # Oversikt
    def do_oversikt(self, inp):
        xkr_oversikt = client.get("/api/v2/peatio/account/balances/xkr")
        btc_oversikt = client.get("/api/v2/peatio/account/balances/btc")
        usdt_oversikt = client.get("/api/v2/peatio/account/balances/usdt")
        # TODO
        # Lage en ordreoversikt med hvor mange ordre som er aktive
        #ordre_oversikt = client.get("/api/v2/peatio/market/orders/")
        print("\nWallet oversikt:\n")
        time.sleep(0.5)
        print(f"XKR = {(xkr_oversikt['balance'])}")
        time.sleep(0.5)
        print(f"BTC = {(btc_oversikt['balance'])}")
        time.sleep(0.5)
        print(f"USDT = {(usdt_oversikt['balance'])}\n")
        #print("Aktive ordre:")
        #print(ordre_oversikt)

    # Kontaktinformasjon
    def do_kontakt(self, inp):
        print("\nKontaktinformasjon:\n")
        print("https://www.github.com/DanielBoye")
        print("https://www.linkedin.com/in/danielboye\n")
    def help_kontakt(self):
        print("Viser kontaktinformasjon til forfatteren")
    
    def do_ask(self, inp):
        btc_ask = float(btc_price['asks'][0][0])
        print(f"\nBitcoin ask: {btc_ask}")
    def help_ask(self):
        print("Printer ut ask prisen av btc")

    def do_bid(self, inp):
        btc_bid = float(btc_price['bids'][0][0])
        print(f"\nBitcoin bid: {btc_bid}\n")
    def help_ask(self):
        print("Printer ut bid prisen av btc")

    def do_price(self, inp):
        if inp == 'btc':
            btc_price = float(btc_last_trade[0]['price'])
            print(f"\nSiste trade var på {btc_price}\n")
          
        if inp == 'xkr':
            print("xkr")
        
        
    def help_price(self):
        print("Printer ut bid prisen av btc")


    




printProgressBar(0, l, prefix = 'Loading Shell:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Rediger tiden for hvor rask den burde lastes inn
    time.sleep(0.0005)
    # Oppdaterer baren 
    printProgressBar(i + 1, l, prefix = 'Loading API:', suffix = 'Complete', length = 50)


os.system('cls')
exbitron_shell().cmdloop()