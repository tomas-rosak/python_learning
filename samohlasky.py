#!/usr/bin/env python

slovo = input("Vase slovo: ")
samohlasky = 0
souhlasky = 0
cisla = 0
ostatni = 0
for znak in slovo:
    if znak in "áeéěiíoóuúůyý":
        samohlasky = samohlasky + 1
    elif znak in "bcčdďfghjklmnňpqrřsštťvwxzž":
        souhlasky = souhlasky + 1
    elif znak in "0123456789":
        cisla = cisla + 1
    else:
        ostatni = ostatni + 1
#samohlasky
if (samohlasky == 1):
    print("Vase slovo obsahuje", samohlasky, "samohlasku")
elif ((samohlasky == 2) or ((samohlasky == 3)) or (samohlasky == 4)):
    print("Vase slovo obsahuje", samohlasky, "samohlasky")
else:
    print("Vase slovo obsahuje", samohlasky, "samohlasek")
#souhlasky
if (souhlasky == 1):
    print("Vase slovo obsahuje", souhlasky, "souhlasku")
elif ((souhlasky == 2) or ((souhlasky == 3)) or (souhlasky == 4)):
    print("Vase slovo obsahuje", souhlasky, "souhlasky")
else:
    print("Vase slovo obsahuje", souhlasky, "souhlasky")
#cisla
if (cisla == 1):
    print("Vase slovo obsahuje", cisla, "cislo")
elif ((cisla == 2) or ((cisla == 3)) or (cisla == 4)):
    print("Vase slovo obsahuje", cisla, "cisla")
else:
    print("Vase slovo obsahuje", cisla, "cisel")
#ostatni
if (ostatni == 1):
    print("Vase slovo obsahuje", ostatni, "ostatni znak")
elif ((ostatni == 2) or ((ostatni == 3)) or (ostatni == 4)):
    print("Vase slovo obsahuje", ostatni, "ostatni znaky")
else:
    print("Vase slovo obsahuje", ostatni, "ostatnich znaku")
 


