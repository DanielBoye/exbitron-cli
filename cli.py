import os
import exbitron
import time
from cmd import Cmd

# Written by @DanielBoye

# Sette default API keys. Må bli endret selv i python filen
client = exbitron.Client(
)

# Alle valg til spørsmål om API keys
ja_valg = {'ja', 'JA', 'Ja', 'jA', 'y', 'Y', 'yes', 'Yes', ''}
nei_valg = {'nei', 'Nei', 'no', 'NO', 'No', 'n', 'N'}

# For loading bar
items = list(range(0, 57))
l = len(items)

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
    # https://patorjk.com/software/taag/#p=display&h=2&v=3&f=Slant&t=EXBITRON%20API%20CLI
    intro = """
    _______  __ ____  ______________  ____  _   __   ___    ____  ____   ________    ____
   / ____/ |/ // __ )/  _/_  __/ __ \/ __ \/ | / /  /   |  / __ \/  _/  / ____/ /   /  _/
  / __/  |   // __  |/ /  / / / /_/ / / / /  |/ /  / /| | / /_/ // /   / /   / /    / /  
 / /___ /   |/ /_/ // /  / / / _, _/ /_/ / /|  /  / ___ |/ ____// /   / /___/ /____/ /   
/_____//_/|_/_____/___/ /_/ /_/ |_|\____/_/ |_/  /_/  |_/_/   /___/   \____/_____/___/ 
    
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
    
    # Ask
    def do_ask(self, inp):
        ask_api_request = client.get("/api/v2/peatio/public/markets/" +  inp + "usdt/depth?limit=1")
        crypto_bid = float(ask_api_request['asks'][0][0])
        print(f"\nAsk til {inp}: {crypto_bid}\n")
    def help_ask(self):
        print("\nPrinter ut ask prisen av et valgfritt par")
        print("\nFor å printe ut ask prisen, skriv ask {symbol} siden den autovelger paret /usdt\n")
    
    # Bid
    def do_bid(self, inp):
        bid_api_request = client.get("/api/v2/peatio/public/markets/" +  inp + "usdt/depth?limit=1")
        crypto_bid = float(bid_api_request['bids'][0][0])
        print(f"\nBid til {inp}: {crypto_bid}\n")
    def help_bid(self):
        print("\nPrinter ut bid prisen av et valgfritt par")
        print("\nFor å printe ut bid prisen, skriv bid {symbol} siden den autovelger paret /usdt\n")

    # Spread
    def do_spread(self, inp):
        spread_api_request = client.get("/api/v2/peatio/public/markets/" +  inp + "usdt/depth?limit=1")
        ask = float(spread_api_request['asks'][0][0])
        bid = float(spread_api_request['bids'][0][0])
        spread = ask - bid
        print(f"\nSpread til {inp} er på: " + str((round(spread / ask, 4)) * 100) + "%\n")
    def help_spread(self):
        print("\nPrinter ut spread-en i et trading par")
        print("\nSpread-et er satt i prosent og printes ut som prosent\n")


    # Pris
    def do_price(selv, inp):
        special_api_request = client.get("/api/v2/peatio/public/markets/" +  inp + "usdt/trades?limit=1")
        crypto_price = float(special_api_request[0]['price'])
        print(f"\nPrisen til {inp} er {crypto_price}\n")    
    def help_price(self):
        print("\nPrinter ut prisen av et valgfritt par")
        print("\nFor å printe ut prisen av noe, skriv price {symbol} siden den autovelger paret /usdt")
        print("\nPris vises i siste trade på platformen\n")


printProgressBar(0, l, prefix = 'Loading Shell:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Rediger tiden for hvor rask den burde lastes inn
    time.sleep(0.0005)
    # Oppdaterer baren 
    printProgressBar(i + 1, l, prefix = 'Loading API:', suffix = 'Complete', length = 50)


os.system('cls')
exbitron_shell().cmdloop()