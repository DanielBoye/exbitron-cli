# Exbitron API CLI

# ![Exbitron](https://cdn.discordapp.com/attachments/994252098571079740/1051226477875691660/image.png)

Command line interface til nettstedet [Exbitron](https://www.exbitron.com/)

# Innhold
- [API dokumentasjon](#api-dokumentasjon)
- [Setup og kjør](#setup-og-kjør)
- [Kommandoer](#kommandoer)
- [Bidra](#bidra)
- [Bidragsytere](#bidragsytere)
- [Lisens]()

# API Dokumentasjon

API-en som er brukt er [Exbitron](https://www.exbitron.com/kb/api.html) sin. All informasjon brukt kommer herifra. For å bygge ut dette produktet er det bare å implementere flere endpoints.

# Setup og kjør 

1. Klon dette prosjektet  `git clone git@github.com:danielboye/exbitron-cli.git`
2. Følg [API](api.md) guiden til å skaffe deg API nøkklene ifra Exbitron som trengs for å koble seg til API-en
3. Kjør `./setup.shy`
4. Kjør `python cli.py`

# Kommandoer

Mer kommandoer kommer etterhvert. Alt kan bli implenentert ifra API-en inn i CLI

### Wallet
- `oversikt` - Meny med oversikt over aktive ordre og wallet.
- `wallet` - Returnerer hva du har i walleten din. 
- `exit` - Lukk programmet.

### Priser

- `price <ticker>` - Prisen av et trading par.
- `ask <ticker>` - Ask prisen i ordreboken til et valgfritt tradingpar.
- `bid <ticker>` - Bid prisen i ordreboken til et valgfritt tradingpar.
- `spread <ticker>` - Spread vises i % på et valgfritt tradingpar.

Eksempel på bruk:


```shell
spread btc
```
Output

```shell
Spread til btc er på: 2.44 %
```

### Andre
- `kontakt` - Kontaktinformasjon til forfatteren.

# TODO

- Få en bedre wallet oversikt 
- Utføre trades 
- Stoppe, lage og redigere live ordere
- Bedre design på å lukke scriptet med ctrl c uten å printe ut "KeyboardInterrupt"
- Mer features ifra API-en
- Skrive prosjektet om til engelsk
- Skrive om programmet til C++ 
- Lage programmet om til en kommando i linux med hjelp av et bash script. Som "neofetch" bare som "exbitron" som launcher clienten 

Store endringer som er kule men vanskelige

- Få trading data representert rett i terminalen som egne "candels"
- Ha et mer persistent program som tar heller å spør deg en gang om nøkklene, og husker dem etter det

# Bidra

## Pull request

Jeg setter pris på alle bidrag enten det er små endringer som dokumentasjon av kildekode til større forbedring av
kode. Den enkleste måten er å lage en gaffel og deretter lage en trekkforespørsel til vår mastergren.

Flere features kommer etterhvert, og det er bare å lage nye "issues" for noe funksjoner dere ønsker, så skal jeg ta en titt på dem

# Bidragsytere

Følgende bidragsytere har enten vært med på å starte dette prosjektet, har bidratt
kode, aktivt vedlikeholder den (inkludert dokumentasjon), eller på andre måter
være fantastiske bidragsytere til dette prosjektet. **Vi vil gjerne bruke et øyeblikk på å gjenkjenne dem.**

[<img src="https://github.com/danielboye.png?size=72" alt="danielboye" width="72">](https://github.com/danielboye)

# Lisens

Lisensen er MIT
