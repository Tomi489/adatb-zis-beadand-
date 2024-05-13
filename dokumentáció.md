# Adatbázis beadandó

**Készítette Soós Barnabás, Rutai Tamás**
**3. típusú feladat**

# Adatbázis leírása
A beadandó projektünk egy MongoDB NoSQL adatbázis ami egy fiktív egyetem hallgatóit, szakokat, diákszervezeteket, és ezeknek programjait tárolja.
Az egész adatbázis bizonyos sémák szerint random generált, emiatt a hallgatók között lehetnek ismétlődő nevűek, vagy címűek.

## Adatbázis táblák

Az adatbázisban az alábbi táblák találhatóak:

1. Hallgatók

```
{
    "_id":{"$oid":"663e57e5a534031b4f37f093"},
    "vezetéknév":"Simon",
    "keresztnév":"Réka",
    "irányítószám":{"$numberInt":"3400"},
    "utca":"Móricz Zsigmond",
    "házszám":{"$numberInt":"96"},
    "email":"simon.réka@freemail.hu",
    "jelszó":"0QWTfeOZ7f",
    "születésiDátum":"2000-09-30",
    "szak":"közgazdász",
    "telefon":"+36870336937",
}
``` 

2. Szakok

```
{
    "_id":{"$oid":"663e5800a534031b4f37f4a2"},
    "név":"mérnök",
    "szakfelelős":["Oláh","Minka"],
    "Tanszékvezető":["Oláh","Mandula"],
    "Dékán":["Nagy","Adrienn"],
    "hallgatokszam":{"$numberInt":"145"},
    "elérhetőség":"+36329231319",
    "email":"oláh.minka@hotmail.com"
}
```

3. Diákszervezetek

```
{
    "_id":{"$oid":"663e57eda534031b4f37f47e"},
    "név":"Hallgatói Hálózat",
    "vezető":["Balogh","Ivett"],
    "elérhetőség":"+36430437883",
    "email":"balogh.ivett@freemail.hu",
    "teremszám":{"$numberInt":"15"},
    "tagok":["Szabó Vince","Farkas Péter","Lakatos Andrea","Varga Fruzsina","Simon Soma","Farkas Péter",
    "Varga Luca","Oláh Milán","Juhász József","Szabó Johanna","Molnár Szonja","Tóth Mercédesz","Oláh Alíz",
    "Kiss Emil","Simon Abigél","Kiss Simon","Kovács Vince","Lakatos Bettina","Szabó Blanka","Varga Tony","Papp Menyhért"
    ,"Horváth Béla","Tóth Dániel","Balogh István","Kovács Melinda","Németh Szabolcs","Szabó Ivett","Mészáros Andrea",
    "Tóth Erik","Tóth Zita","Juhász Márton","Lakatos Patrik","Kovács Gréta","Mészáros Lejla","Tóth Liliána"]
}
```

4. Programok

```
{
    "_id":{"$oid":"663e57f3a534031b4f37f483"},
    "név":"szakmai verseny",
    "időpont":"2023-03-13",
    "szervező":["Takács","Szilvia"],
    "elérhetőség":"+36409847150",
    "email":"takács.szilvia@freemail.hu",
    "részvevők":["Takács Lili","Oláh Rudolf","Papp Fanni","Németh Traján","Nagy József",
    "Oláh Rudolf","Farkas Gábor","Horváth Blanka","Nagy Luca","Horváth Mózes"],
    "leírás":"A program célja a szakmai kapcsolatok erősítése",
    "diákszervezet":"Hallgatói Önkormányzat"
}     
```
## Kapcsolatok

Az adatbázis táblái összekapcsolhatóak az alábbi kapcsolatok szerint:
-szak.név=hallgató.szak
-diákszervezetek.tagok=hallgató.szak
-programok.résztvevők=hallgató.szak
-diákszervezetek.név=programok.diákszervezet

# Adatbázis létrehozásának leírása

A hallgatóGenerator függvény egy hallgatót reprezentáló szótárt generál véletlenszerű adatok alapján. A szótár a következő mezőket tartalmazza:

    Vezetéknév, keresztnév (nevGenerator)
    Irányítószám, utca, házszám (címGenerator)
    Email (emailGenerator)
    Jelszó (jelszóGenerator)
    Születési dátum (datumGenerátor)
    Szak (random.choice(szakok))
    Hallgatószám frissítése (szakok alapján)
    Telefonszám (telefonGenerator)

A függvény szótárt hoz létre a hallgató adataival, és visszaadja.
Ezt a szótárt utána egy cikluson belül akárhányszor meg lehet ismételni, utána a szótárakat egy listába fűzi össze a program, amit a *json.dump* kóddal kiexportál.
A json file-okat a MongoDB Compass használatával töltöttem fel a cloud-ba.

**Ugyanez a logika alapján készültek el a szakok, diákszervezetek, programok.**

A diákszervezetek, és a programok létrehozásnál figyelembe van véve, hogy a hallgatók közt lévők kerülhessenek diászervezetbe, az abban lévők pedig az általuk rendezett programokba.
