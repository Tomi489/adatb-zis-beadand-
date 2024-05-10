keresztnevekFérfi=["István", "Anna", "Balázs", "Erzsébet", "Dávid", "Katalin", "Gábor", "Mária", "József", "Zsuzsa", "Ákos", "Adrián", "Albert", "András", "Arnold", "Attila", "Béla", "Benjamin", "Bence", "Csaba", "Dániel", "Dominik", "Dénes", "Ede", "Elemér", "Emil", "Erik", "Ernő", "Eszter", "Ferenc", "Gábor", "Gergely", "Gyula", "Gusztáv", "Győző", "Henrik", "Hunor", "István", "Iván", "János", "Jenő", "József", "Kálmán", "Károly", "Kevin", "Kristóf", "László", "Levente", "Loránd", "Máté", "Márton", "Mátyás", "Menyhért", "Miklós", "Milán", "Mózes", "Nádor", "Nimród", "Noel", "Olivér", "Ottó", "Patrik", "Péter", "Richárd", "Roland", "Róbert", "Ruben", "Rudolf", "Sándor", "Sebestyén", "Simeon", "Simon", "Soma", "Szabolcs", "Tamás", "Tibor", "Timóteus", "Titusz", "Tivadar", "Tomi", "Tony", "Traján", "Viktor", "Vince", "Vince", "Zénó", "Zoltán"]
keresztnevekNői=["Anna", "Abigél", "Adrienn", "Agnes", "Alexandra", "Alíz", "Amanda", "Andrea", "Anita", "Aranka", "Beatrix", "Bettina", "Bianka", "Blanka", "Borbála", "Brigitta", "Csilla", "Csenge", "Dóra", "Dorottya", "Emese", "Eszter", "Éva", "Fanni", "Flóra", "Fruzsina", "Gabriella", "Gizella", "Gréta", "Hanna", "Hedvig", "Heléna", "Henrietta", "Hermina", "Ildikó", "Ilona", "Imola", "Ingrid", "Ivett", "Izabella", "Janka", "Johanna", "Júlia", "Jusztina", "Kata", "Katalin", "Kitti", "Kitti", "Lara", "Lejla", "Lili", "Liliána", "Linda", "Luca", "Lilla", "Lívia", "Liz", "Loretta", "Lotti", "Luca", "Magdolna", "Maja", "Mandula", "Márta", "Melinda", "Mercédesz", "Minka", "Mira", "Mónika", "Natasa", "Nóra", "Noémi", "Olívia", "Orsolya", "Patrícia", "Petra", "Réka", "Regina", "Rebeka", "Renáta", "Rita", "Rozália", "Sára", "Szonja", "Szilvia", "Szófia", "Tamara", "Tímea", "Tina", "Tünde", "Veronika", "Vivien", "Zita", "Zsófia"]
vezetéknevek=["Kovács", "Nagy", "Tóth", "Szabó", "Horváth", "Varga", "Kiss", "Molnár", "Németh", "Farkas", "Balogh", "Papp", "Takács", "Juhász", "Lakatos", "Mészáros", "Oláh", "Simon", "Kovács", "Nagy", "Tóth", "Szabó", "Horváth", "Varga", "Kiss", "Molnár", "Németh", "Farkas", "Balogh", "Papp", "Takács", "Juhász", "Lakatos", "Mészáros", "Oláh", "Simon", "Kovács", "Nagy", "Tóth", "Szabó", "Horváth", "Varga", "Kiss", "Molnár", "Németh", "Farkas", "Balogh", "Papp", "Takács", "Juhász", "Lakatos", "Mészáros", "Oláh", "Simon", "Kovács", "Nagy", "Tóth", "Szabó", "Horváth", "Varga", "Kiss", "Molnár", "Németh", "Farkas", "Balogh", "Papp", "Takács", "Juhász", "Lakatos", "Mészáros", "Oláh", "Simon", "Kovács", "Nagy", "Tóth", "Szabó", "Horváth", "Varga", "Kiss", "Molnár", "Németh", "Farkas", "Balogh", "Papp", "Takács", "Juhász", "Lakatos", "Mészáros", "Oláh", "Simon", "Kovács", "Nagy", "Tóth", "Szabó", "Horváth", "Varga", "Kiss", "Molnár", "Német"]
irányítószámok=[1011, 1021, 1031, 1041, 1051, 1061, 1071, 1081, 1091, 1111, 1121, 1131, 1141, 1151, 1161, 1171, 1181, 1191, 1201, 1211, 1221, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500]
utcaNevek=["Kossuth Lajos", "Petőfi Sándor", "Ady Endre", "Arany János", "Jókai Mór", "Vörösmarty Mihály", "Móricz Zsigmond", "Széchenyi István", "Babits Mihály", "Kisfaludy Károly", "Kazinczy Ferenc", "Kodály Zoltán", "Bartók Béla", "Liszt Ferenc", "Erkel Ferenc"]
szakok=["informatika", "műszaki informatika", "gazdaságinformatika", "közgazdaságtan", "közgazdász", "mérnök", "műszaki menedzser"]
import json
import random
import string
import datetime
import os

os.remove(r'C:\Users\tomir\Documents\adatbázis beadandó\hallgatók.json')
os.remove(r'C:\Users\tomir\Documents\adatbázis beadandó\szakok.json') 
print("fájlok törölve")

def randomDate():
    start_date = datetime.date(1980, 1, 1)
    end_date = datetime.date(2000, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def nevGenerator():
    vezetéknév=random.choice(vezetéknevek)
    nem=random.choice(["férfi", "nő"])
    if nem=="férfi":
        keresztnév=random.choice(keresztnevekFérfi)
    else:
        keresztnév=random.choice(keresztnevekNői)
    return vezetéknév, keresztnév

def címGenerator():
    irányítószám=random.choice(irányítószámok)
    utca=random.choice(utcaNevek)
    házszám=random.randint(1, 100)
    return irányítószám, utca, házszám

def emailGenerator(vezetéknév, keresztnév):
    domain=random.choice(["gmail.com", "yahoo.com", "freemail.hu", "citromail.hu", "hotmail.com", "freemail.hu", "freemail.hu"])
    return vezetéknév.lower()+"."+keresztnév.lower()+"@"+domain

def jelszóGenerator():
    jelszó=""
    for i in range(10):
        jelszó+=random.choice(string.ascii_letters+string.digits)
    return jelszó

def telefonGenerator():
    return "+36"+str(random.randint(100000000, 999999999))

hallgatokszama=[0,0,0,0,0,0,0]
hallgatoklista=[]

def hallgatóGenerator():
    vezetéknév, keresztnév=nevGenerator()
    hallgatoklista.append(vezetéknév+" "+keresztnév)
    irányítószám, utca, házszám=címGenerator()
    email=emailGenerator(vezetéknév, keresztnév)
    jelszó=jelszóGenerator()
    születésiDátum=datumGenerátor(1990, 2004)
    szak=random.choice(szakok)
    for i in range(7):
        if szak==szakok[i]:
            hallgatokszama[i]+=1
    telefon=telefonGenerator()
    hallgató={"vezetéknév": vezetéknév, "keresztnév": keresztnév, "irányítószám": irányítószám, "utca": utca, "házszám": házszám, "email": email, "jelszó": jelszó, "születésiDátum": str(születésiDátum), "szak": szak, "telefon": telefon}
    return hallgató

def datumGenerátor(tól, ig):
    start_date = datetime.date(tól, 1, 1)
    end_date = datetime.date(ig, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

hallgatók=[]
for i in range(1000):
    hallgatók.append(hallgatóGenerator())
with open(r'C:\Users\tomir\Documents\adatbázis beadandó\hallgatók.json', "w") as f:
    json.dump(hallgatók, f, indent=4)


#szakok generálása

leírások=["Az informatika a jövő", "A műszaki informatika a jövő", "A gazdaságinformatika a jövő", "A közgazdaságtan a jövő", "A közgazdász a jövő", "Az mérnök a Jövő", "A műszaki menedzser a jövő"]
def szakGenerator(szakokszama):
    i=int(szakokszama)
    szakok=["informatika", "műszaki informatika", "gazdaságinformatika", "közgazdaságtan", "közgazdász", "mérnök", "műszaki menedzser"]
    név=szakok[i]
    leírás=szakok[i]
    szakfelelős=nevGenerator()
    Tanszékvezető=nevGenerator()
    Dékán=nevGenerator()
    hallgatokszam=hallgatokszama[i]
    elérhetőség=telefonGenerator()
    email=emailGenerator(szakfelelős[0], szakfelelős[1])
    szak={"név": név, "leírás": leírás, "szakfelelős": szakfelelős, "Tanszékvezető": Tanszékvezető, "Dékán": Dékán, "hallgatokszam": hallgatokszam, "elérhetőség": elérhetőség, "email": email}
    return szak

szakok=[]
for i in range(7):
    szakok.append(szakGenerator(i))
with open(r'C:\Users\tomir\Documents\adatbázis beadandó\szakok.json', "w") as f:
    json.dump(szakok, f, indent=4)

def diákszervezetgenerátor(diákszervezetszáma, hallgatóklista):
    diákszervezetek=["Hallgatói Önkormányzat", "Hallgatói Képviselet", "Hallgatói Szövetség", "Hallgatói Hálózat", "Hallgatói Unió", "Hallgatói Tanács", "Hallgatói Testület"]
    név=diákszervezetek[diákszervezetszáma]
    teremszám=random.randint(1, 100)
    vezető=nevGenerator()
    elérhetőség=telefonGenerator()
    email=emailGenerator(vezető[0], vezető[1])
    tagok=[]
    db=random.randint(20, 50)
    for i in range(db):
        tag=random.choice(hallgatóklista)
        tagok.append(tag)
    diákszervezet={"név": név, "vezető": vezető, "elérhetőség": elérhetőség, "email": email, "teremszám": teremszám, "tagok": tagok}
    return diákszervezet, tagok

def programgenerátor(tagok):
    programok=["szakmai nap", "szakmai kirándulás", "szakmai előadás", "szakmai workshop", "szakmai konferencia", "szakmai verseny", "szakmai vetélkedő", "szakmai találkozó", "szakmai fórum", "szakmai bemutató"]
    leírás=["A program célja a szakmai ismeretek bővítése", "A program célja a szakmai kapcsolatok erősítése", "A program célja a szakmai kapcsolatok bővítése", "A program célja a szakmai kapcsolatok erősítése", "A program célja a szakmai kapcsolatok bővítése", "A program célja a szakmai kapcsolatok erősítése", "A program célja a szakmai kapcsolatok bővítése", "A program célja a szakmai kapcsolatok erősítése", "A program célja a szakmai kapcsolatok bővítése", "A program célja a szakmai kapcsolatok erősítése"]
    név=random.choice(programok)
    leír=leírás[random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
    időpont=datumGenerátor(2023, 2024)
    szervező=nevGenerator()
    elérhetőség=telefonGenerator()
    email=emailGenerator(szervező[0], szervező[1])
    db=random.randint(10, 20)
    részvevők=[]
    for i in range(db):
        tag=random.choice(tagok)
        részvevők.append(tag)
    terem=random.randint(1, 100)
    program={"név": név, "időpont": str(időpont), "szervező": szervező, "elérhetőség": elérhetőség, "email": email, "részvevők": részvevők, "terem": terem, "leírás": leír}
    return program

diákszervezetek=[]
programok=[]
for i in range(7):
    diákszervezet, tagok=diákszervezetgenerátor(i, hallgatoklista)
    diákszervezetek.append(diákszervezet)
    db=random.randint(1, 5)
    for i in range(db):
        program=programgenerátor(tagok)
        programok.append(program)
    

with open(r'C:\Users\tomir\Documents\adatbázis beadandó\diákszervezetek.json', "w") as f:
    json.dump(diákszervezetek, f, indent=4)

with open(r'C:\Users\tomir\Documents\adatbázis beadandó\programok.json', "w") as f:
    json.dump(programok, f, indent=4)

print("adatbázisok generálva")