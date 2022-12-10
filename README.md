# Exbitron CLI

Command line interface til nettstedet [Exbitron](https://www.exbitron.com/)

# Innhold

- [Setup og kjør](#setup-og-kjør)
- [Kommandoer](#kommandoer)
- [Bidragsytere]()
- [Lisens]()

# Setup og kjør 

1. Klon dette prosjektet  `git clone git@github.com:danielboye/exbitron-cli.git`
2. Følg [API]() guiden til å skaffe deg API keys ifra Exbitron
3. Kjør `python cli.py`

# Kommandoer

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

```shell
Spread til btc er på: 2.44 %
```

### Andre
- `kontakt` - Kontaktinformasjon til forfatteren.

# Bidragsytere

## Pull Request

Følgende bidragsytere har enten vært med på å starte dette prosjektet, har bidratt
kode, aktivt vedlikeholder den (inkludert dokumentasjon), eller på andre måter
være fantastiske bidragsytere til dette prosjektet. **Vi vil gjerne bruke et øyeblikk på å gjenkjenne dem.**

[<img src="https://github.com/danielboye.png?size=72" alt="danielboye" width="72">](https://github.com/danielboye)
