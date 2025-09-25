def addVybaveni():
    name = input("Název = ")
    category = input("Kategorie = ")
    pricePerDay = 0
    while (1):
        price = input("Cenu za den = ")
        if (price.isdigit()):
            pricePerDay = int(price)
            break
    vybaveni = {
        "name": name,
        "category": category,
        "pricePerDay": pricePerDay,
        "pujceniPocet": 0,
        "pujceno": False
    }
    return vybaveni

def vypisVybaveni(seznam):
    for i in range(len(seznam)):
        print(f"id: {i}\n    název: {seznam[i]["name"]}\n    kategorie: {seznam[i]["category"]}\n    cena za den: {seznam[i]["pricePerDay"]}\n    pujceno: {seznam[i]["pujceno"]}\n    pocet půjčení: {seznam[i]["pujceniPocet"]}")

def addZakaznik():
    name = input("Jméno = ")
    prijmeni = input("Příjmení = ")
    pujceno = []
    zakaznik = {
        "name": name,
        "prijmeni": prijmeni,
        "pujceno": pujceno
    }
    return zakaznik

def vypisZakazniku(seznam):
    for i in range(len(seznam)):
        print(f"id: {i}\n    jméno: {seznam[i]["name"]} {seznam[i]["prijmeni"]}\n    půjčeno: {len(seznam[i]["pujceno"])}")

def pujceniVybaveni(seznamVybaveni, seznamZakazniku):
    while 1:
        zakaznikIdStr = input("ID zákazníka = ")
        zakaznikId = 0
        if (zakaznikIdStr.isdigit()):
            zakaznikId = int(zakaznikIdStr)
            if (zakaznikId < len(seznamZakazniku)):
                break
    while 1:
        vybaveniIdStr = input("ID vybaveni = ")
        vybaveniId = 0
        if (vybaveniIdStr.isdigit()):
            vybaveniId = int(vybaveniIdStr)
            if (vybaveniId < len(seznamVybaveni)):
                break
    seznamVybaveni[vybaveniId]["pujceniPocet"] += 1
    seznamVybaveni[vybaveniId]["pujceno"] = True
    seznamZakazniku[zakaznikId]["pujceno"].append(vybaveniId)
    print(f"cena za den = {seznamVybaveni[vybaveniId]["pricePerDay"]}")

def vraceniVybaveni(seznamVybaveni, seznamZakazniku):
    while 1:
        zakaznikIdStr = input("ID zákazníka = ")
        zakaznikId = 0
        if (zakaznikIdStr.isdigit()):
            zakaznikId = int(zakaznikIdStr)
            if (zakaznikId < len(seznamZakazniku)):
                break
    while 1:
        vybaveniIdStr = input("ID vybaveni = ")
        vybaveniId = 0
        if (vybaveniIdStr.isdigit()):
            vybaveniId = int(vybaveniIdStr)
            if (vybaveniId < len(seznamVybaveni)):
                break
    seznamVybaveni[vybaveniId]["pujceno"] = False
    seznamZakazniku[zakaznikId]["pujceno"].remove(vybaveniId)

def statistika(seznamVybaveni, seznamZakazniku):
    dostupne = 0
    for i in range(len(seznamVybaveni)):
        if not (seznamVybaveni[i]["pujceno"]):
            dostupne += 1
    print(f"dostupné položky: {dostupne}/{len(seznamVybaveni)}\npočet zákazníků: {len(seznamZakazniku)}")

seznamVybaveni = []
seznamZakazniku = []

while 1:
    command = input("\n\
0: exit\n\
1: přidání vybavení\n\
2: výpis vybavení\n\
3: přidání zákazníka\n\
4: výpis zákazníka\n\
5: půjčit vybavení zákazníkovi\n\
6: vrátit vybavení\n\
7: statistika\n\
>> "
)
    if (command.isdigit()):
        n = int(command)
        if (n == 0):
            break
        elif (n == 1):
            seznamVybaveni.append(addVybaveni())
        elif (n == 2):
            vypisVybaveni(seznamVybaveni)
        elif (n == 3):
            seznamZakazniku.append(addZakaznik())
        elif (n == 4):
            vypisZakazniku(seznamZakazniku)
        elif (n == 5):
            pujceniVybaveni(seznamVybaveni, seznamZakazniku)
        elif (n == 6):
            vraceniVybaveni(seznamVybaveni, seznamZakazniku)
        elif (n == 7):
            statistika(seznamVybaveni, seznamZakazniku)
