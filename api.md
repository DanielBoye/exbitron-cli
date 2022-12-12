# API Keys

### For brukere som har en registrert konto, hopp til [steg 2](#2-generer-api-nøkkler)

## 1. Lag en bruker

Først skal vi registrere en konto på Exbitron, slik at vi kan sende, handle og motta krypto. Men i vårt tilfelle trenger vi det til API-en

Åpne nettsiden og klikk på den røde "Registrer"-knappen øverst til høyre. Du kan også lime inn https://www.exbitron.com/signup i nettleseren din. Fyll inn e-posten din og velg et passord. Bekreft dette passordet og kryss av for vilkårene for bruk. Utfør deretter kapittelet og klikk på den gule "Registrer-knappen".

![sign-up](https://user-images.githubusercontent.com/83395536/166160687-85e302bb-f146-4d73-9c5a-9d377bfebb8b.png)

Du vil da motta en bekreftelses-e-post, så gå over til innboksen din. Dobbeltsjekk at e-posten kommer fra info@exbitron.com, og klikk på den blå "Bekreft"-knappen. Logg på med e-post og passord.

## 2. Generer API nøkkler

Klikk på "Profile knappen på hjemmeskjermen" eller gå til [exbitron.com/profile](exbitron.com/profile)

![profil-knapp](https://cdn.discordapp.com/attachments/994252098571079740/1051239811404529674/image.png)

Du vil nå se oversikten av profilen din. Trykk så på "API Keys" under den hvite Profile knappen

![profil-api](https://cdn.discordapp.com/attachments/994252098571079740/1051240908147933204/image.png)

Klikk så på den grå "Create new" knappen og skriv inn sikkerhetskoden ifra appen.

Du vil så få nøklene dine slik.

![api-keys](https://cdn.discordapp.com/attachments/994252098571079740/1051241973295616071/image.png)

## 3. Rediger cli.py

Kopier dine Access Keys og Secret Keys, og sett de inn i .env filen eller sett enviroment variables i ditt OS.

Eksempel:

```
ACCESS_KEY=fe12eb8b793dbbc9
SECRET_KEY=82f57fe6471b7f0e2bc665f97e41a7
```

---

Og nå er du klar for å bruke dem!
