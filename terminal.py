import os

"""
os.path.isfile(path
if os.path.isdir

# zápis do souboru
with open("soubor.txt", "w", encoding="utf-8") as f:
    f.write("První řádek\n")
    f.write("Tento text je na druhém řádku\n")
    f.write("A do třetice.\n")
print("Do souboru bylo zapsáno.")

# připsání textu do existujícího souboru
with open("soubor.txt", "a", encoding="utf-8") as f:
    f.write("Připsaný řádek")
print("Do souboru bylo připsáno.")

# výpis obsahu souboru
print("Vypisuji soubor:")

with open("soubor.txt", "r", encoding="utf-8") as f:
    for radek in f.readlines():
        print(radek.strip()) # Odstraníme "\n"
"""


def rozpoznani_prikazu(prikaz):  
    prikaz = prikaz.split(" ")
    druh = 0
    try:
        if prikaz[0] == "cd":
            druh = 1
        elif prikaz[0] == "pwd":
            druh = 2
    except:
        pass
    return druh

"""
def vyvolani(prikaz):
    if prikaz == 1:
        adresa, adresar, adresa_minuly, adresar_minuly = cd(adresa, adresar, prikaz1, adresa_minuly, adresar_minuly)
    elif prikaz == 2:
        pwd(adresar)        
"""

def pwd(adresar):
    print(adresar)

def cd(adresa, adresar, prikaz1, adresa_minuly, adresar_minuly):
    prikaz1 = prikaz1.split(" ")
    if len(prikaz1) == 1:
        adresar = "/home/tom/"
        adresa = "$"    
    elif prikaz1[1] != "..": 
        adresar_minuly, adresa_minuly = adresar, adresa
        adresar += prikaz1[1]
        adresa = adresar [9:]
    else:
        adresa, adresar = adresa_minuly, adresar_minuly
    return adresa, adresar, adresa_minuly, adresar_minuly
    
def main():
    adresa = "$"
    adresar = "/home/tom/"
    adresa_minuly, adresar_minuly = "$", "/home/tom/"
    while True:
        prikaz = input("tom@tomt430:~" +adresa + " ")
        prikaz1 = prikaz
        prikaz = rozpoznani_prikazu(prikaz) 
        if prikaz == 1:
            adresa, adresar, adresa_minuly, adresar_minuly = cd(adresa, adresar, prikaz1, adresa_minuly, adresar_minuly)
        elif prikaz == 2:
            pwd(adresar)
            
            
        
main()
