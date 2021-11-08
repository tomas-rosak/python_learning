#!/usr/bin/env python
import random
import os
pokracovat_program = True
print("Black Jack\n")
name_hrac1 = input("Hráč 1 přezdívka: ")
name_hrac2 = input("Hrac 2 přezdívka: ")
while pokracovat_program:
    pouzite_karty = list()
    blacklist = list()
    opakovani = 1
    last = 0
    soucet1 = 0
    soucet2 = 0
    hrac1 = True
    hrac2 = False
    prvni_kolo = True
    spravna_odpoved1 = True
    spravna_odpoved2 = True
    spravna_odpoved3 = True
    spravna_odpoved4 = True
    spravna_odpoved5 = True
    spravna_odpoved6 = True
    spravna_odpoved7 = True
    pokracovat_hra = False
    while prvni_kolo:
        input(name_hrac1 + ": Stiskněte ENTER k vytáhnutí karty: ")
        karta1 = random.randint(1, 10)
        print(name_hrac1, "si vytáhl", karta1,"\n")
        pouzite_karty.append(karta1)
        soucet1 = soucet1 + karta1
        input(name_hrac2 + ": Stiskněte ENTER k vytáhnutí karty: ")
        karta2 = random.randint(1, 10)
        print(name_hrac2, "si vytáhl", karta2,"\n")
        pouzite_karty.append(karta2)
        soucet2 = soucet2 + karta2
        print("Součet hráčů:")
        print(name_hrac1,":", soucet1)
        print(name_hrac2,":", soucet2,"\n")
        while spravna_odpoved1:
            odpoved_hrac1 = input(name_hrac1 + ": Chce si " + name_hrac1 + " líznout kartu y/n: ")
            if odpoved_hrac1 == "y" or odpoved_hrac1 == "Y":
                hrac1 = True
                hrac2 = False
                pokracovat_hra = True
                spravna_odpoved1 = False
                prvni_kolo = False
            elif odpoved_hrac1 == "n" or odpoved_hrac1 == "N":
                hrac1 = False
                spravna_odpoved1 = False
                pokracovat_hra = True
            else:
                print(name_hrac1, ": Zadali jste neplatnou volbu")
                spravna_odpoved = True
        if hrac1 == False:
            while spravna_odpoved2:
                odpoved_hrac2 = input(name_hrac2 + ": Chce si " + name_hrac2 + " líznout kartu y/n: ")
                if odpoved_hrac2 == "y" or odpoved_hrac2 == "Y":
                    hrac1 = False
                    hrac2 = True
                    pokracovat_hra = True
                    spravna_odpoved2 = False
                    prvni_kolo = False
                elif odpoved_hrac2 == "n" or odpoved_hrac2 == "N":
                    hrac1 = False
                    hrac2 = False
                    spravna_odpoved2 = False
                    prvni_kolo = False
                else:
                    print(name_hrac2, ": Zadali jste neplatnou volbu")
                    spravna_odpoved2 = True
    while pokracovat_hra:
        while hrac1:
            if soucet1 <= 21 and soucet2 <= 21:
                karta1 = random.randint(1, 10)
                if karta1 not in blacklist:
                    pouzite_karty.append(karta1)
                    pouzite_karty.sort()
                    for number in pouzite_karty:
                        if number == last:
                            opakovani += 1
                        else:
                            opakovani = 1
                        if opakovani == 4:
                            if number not in blacklist:
                                blacklist.append(last)
                                opakovani = 1
                        last = number
                    soucet1 = soucet1 + karta1
                    print(name_hrac1, "si vytáhl", karta1,"\n")
                    print("Součet hráčů:")
                    print(name_hrac1,":", soucet1)
                    print(name_hrac2,":", soucet2,"\n")
                    if soucet1 <= 21 and soucet2 <= 21:
                        while spravna_odpoved3:
                            odpoved_hrac2 = input(name_hrac2 + ": Chce si " + name_hrac2 + " líznout kartu y/n: ")
                            if odpoved_hrac2 == "y" or odpoved_hrac2 == "Y":
                                hrac2 = True
                                hrac1 = False
                                spravna_odpoved3 = False
                            elif odpoved_hrac2 == "n" or odpoved_hrac2 == "N":
                                hrac2 = False
                                spravna_odpoved3 = False
                            else:
                                print(name_hrac2, ": Zadali jste neplatnou volbu")
                                spravna_odpoved3 = True
                        spravna_odpoved3 = True
                        if hrac2 == False:
                            while spravna_odpoved4:
                                odpoved_hrac1 = input(name_hrac1 + ": Chce si " + name_hrac1 + " líznout kartu y/n: ")
                                if odpoved_hrac1 == "y" or odpoved_hrac1 == "Y":
                                    hrac1 = True
                                    hrac2 = False
                                    spravna_odpoved4 = False
                                elif odpoved_hrac1 == "n" or odpoved_hrac1 == "N":
                                    hrac1 = False
                                    hrac2 = False
                                    spravna_odpoved4 = False
                                else:
                                    print(name_hrac1, ": Zadali jste neplatnou volbu")
                                    spravna_odpoved4 = True
                            spravna_odpoved4 = True
                    else:
                        hrac1 = False
                        hrac2 = False
            else:
                print(name_hrac1, "překročil 21")
                hrac1 = False
                hrac2 = False
        while hrac2:
            if soucet2 <= 21 and soucet1 <= 21:
                karta2 = random.randint(1, 10)
                if karta2 not in blacklist:
                    pouzite_karty.append(karta2)
                    pouzite_karty.sort()
                    for number in pouzite_karty:
                        if number == last:
                            opakovani += 1
                        else:
                            opakovani = 1
                        if opakovani == 4:
                            if number not in blacklist:
                                blacklist.append(last)
                                opakovani = 1
                        last = number
                    soucet2 = karta2 + soucet2
                    print(name_hrac2, "si vytáhl", karta2,"\n")
                    print("Součet hráčů:")
                    print(name_hrac1,":", soucet1)
                    print(name_hrac2,":", soucet2,"\n")
                    if soucet1 <= 21 and soucet2 <= 21:
                        while spravna_odpoved5:
                            odpoved_hrac1 = input(name_hrac1 + ": Chce si " + name_hrac1 + " líznout kartu y/n: ")
                            if odpoved_hrac1 == "y" or odpoved_hrac1 == "Y":
                                hrac1 = True
                                hrac2 = False
                                spravna_odpoved5 = False
                            elif odpoved_hrac1 == "n" or odpoved_hrac1 == "N":
                                hrac1 = False
                                spravna_odpoved5 = False
                            else:
                                print(name_hrac1, ": Zadali jste neplatnou volbu")
                                spravna_odpoved5 = True
                        spravna_odpoved5 = True
                        if hrac1 == False:
                            while spravna_odpoved6:
                                odpoved_hrac2 = input(name_hrac2 + ": Chce si " + name_hrac2 + " líznout kartu y/n: ")
                                if odpoved_hrac2 == "y" or odpoved_hrac2 == "Y":
                                    hrac1 = False
                                    hrac2 = True
                                    spravna_odpoved6 = False
                                elif odpoved_hrac2 == "n" or odpoved_hrac2 == "N":
                                    hrac1 = False
                                    hrac2 = False
                                    spravna_odpoved6 = False
                                else:
                                    print(name_hrac2, ": Zadali jste neplatnou volbu") 
                                    spravna_odpoved6 = True
                            spravna_odpoved6 = True
                    else:
                        hrac1 = False
                        hrac2 = False   
        if (hrac1 == False and hrac2 == False):              #zacatek vyhodnoceni
            if (soucet1 <= 21 and soucet2 <= 21):
                if soucet1 > soucet2:
                    print(name_hrac1, "vyhrál")
                elif soucet1 < soucet2:
                    print(name_hrac2, "vyhrál")
                elif soucet1 == soucet2:
                    print("Nastala remíza")
                else:
                    print("Někde nastala chyba") 
            elif (soucet1 <= 21 and soucet2 > 21):
                print(name_hrac1, "vyhrál")
            elif (soucet2 <= 21 and soucet1 > 21):
                print(name_hrac2, "vyhrál")
            elif (soucet1 == 21 and soucet2 == 21):
                print("Remíza")
            elif (soucet1 > 21 and soucet2 > 21):
                if soucet1 < soucet2:
                    print("Vyhrál", name_hrac1)
                elif soucet2 < soucet1:
                    print("Vyhrál", name_hrac2)
                else:
                    print("Někde nastala chyba")
            while spravna_odpoved7:
                odpoved_program = input("Chcete dát novou hru y/n: ")
                if odpoved_program == "y" or odpoved_program == "Y":
                    pokracovat_program = True
                    pokracovat_hra = False
                    spravna_odpoved7 = False
                elif odpoved_program == "n" or odpoved_program == "N":
                    pokracovat_program = False
                    spravna_odpoved7 = False
                else:
                    print("Zadali jste neplatnou volbu")
                    spravna_odpoved7 = True
                    pokracovat_hra = False                           #konec vyhodnoceni 
