import exbitron
import hashlib, hmac
import requests
from requests.auth import AuthBase
import json
import math
import time
import sys

client = exbitron.Client(
    access_key = "",
    secret_key = "",
)

ja_valg = {'ja', 'JA', 'Ja', 'jA', 'y', 'Y', 'yes', 'Yes', ''}
nei_valg = {'nei', 'Nei', 'no', 'NO', 'No', 'n', 'N'}



items = list(range(0, 57))
l = len(items)

while True:
    api_spørsmål = input("\nVil du bruke default API keys? (Y/n) ")
    if api_spørsmål in nei_valg:
        print("\nSkriv inn dine Exbitron API keys")
        access_key_input = input("\nAccess key: ")
        secret_key_input = input("\nSecret key ")
        
        client = exbitron.Client(
            access_key = access_key_input,
            secret_key = secret_key_input,
        )
        a = access_key_input
        b = secret_key_input
        print("Utført!")

        break
    if api_spørsmål in ja_valg:
        break
        
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
    # Do stuff...
    time.sleep(0.0005)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Loading API:', suffix = 'Complete', length = 50)

def velkommen_tilbake():
    velkommen = """
#################################
#       Velkommen tilbake!      #
#################################
    """
    print(velkommen)

velkommen_tilbake()



balance = client.get("/api/v2/peatio/account/balances/xkr")
trades = client.get("/api/v2/peatio/market/trades/")


printing = input("Hva vil du printe? ") 
if printing == "balance":
    print(f"Du har {(balance['balance'])} XKR")
if printing == trades:
   print(trades)
