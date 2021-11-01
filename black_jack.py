#!/usr/bin/env python
import random
import os
pokracovat_program = True
print("Black Jack\n")
name_hrac1 = input("Hrac 1 prezdivka: ")
name_hrac2 = input("Hrac 2 prezdivka: ")
while pokracovat_program:
    pouzite_karty = list()
    blacklist = list()
    opakovani = 1
    last = 0
    soucet1 = 0
    soucet2 = 0
    hrac1 = True
    hrac2 = False
    pokracovat_hra = True
    while pokracovat_hra:
        while hrac1:
            if soucet1 <= 21:
                print(name_hrac1,":")
                input("Stisknete ENTER k vytahnuti karty: ")
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
                    print(name_hrac1, "si vytahl", karta1,"\n")
                    print("Soucet hracu:")
                    print(name_hrac1,":", soucet1)
                    print(name_hrac2,":", soucet2,"\n")
                    odpoved_hrac2 = input("Chce si " + name_hrac2 + " liznout kartu y/n: ")
                    spatnaodpoved1 = True
                    if odpoved_hrac2 == "y" or odpoved_hrac2 == "Y":
                        hrac2 = True
                        hrac1 = False
                    elif odpoved_hrac2 == "n" or odpoved_hrac2 == "N":
                        hrac2 = False
                    else:
                        print("Zadali jste neplatnou volbu")
                    if hrac2 == False:
                        odpoved_hrac1 = input("Chce si " + name_hrac1 + " liznout kartu y/n: ")
                        if odpoved_hrac1 == "y" or odpoved_hrac1 == "Y":
                            hrac1 = True
                            hrac2 = False
                        elif odpoved_hrac1 == "n" or odpoved_hrac1 == "N":
                            hrac1 = False
                            hrac2 = False
                        else:
                            print("Zadali jste neplatnou volbu")
                else:
                    print(name_hrac1, "prekrocil 21")
                    hrac1 = False
                    hrac2 = False
                    if soucet2 < 21:
                        odpoved_hrac2 = input("Chce si " + name_hrac2 + " liznout kartu y/n: ")
                        if odpoved_hrac2 == "y" or odpoved_hrac2 == "Y":
                            hrac1 = False
                            hrac2 = True
                        elif odpoved_hrac2 == "n" or odpoved_hrac2 == "N":
                            hrac1 = False
                            hrac2 = False
                        else:
                            print("Zadali jste neplatnou volbu")
        while hrac2:
            if soucet2 <= 21:
                print(name_hrac2,":")
                input("Stisknete ENTER k vytahnuti karty: ")
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
                    print(name_hrac2, "si vytahl", karta2,"\n")
                    print("Soucet hracu:")
                    print(name_hrac1,":", soucet1)
                    print(name_hrac2,":", soucet2)
                    odpoved_hrac1 = input("Chce si " + name_hrac1 + " liznout kartu y/n: ")
                    spatna_odpoved2 = True
                    if odpoved_hrac1 == "y" or odpoved_hrac1 == "Y":
                        hrac1 = True
                        hrac2 = False
                    elif odpoved_hrac1 == "n" or odpoved_hrac1 == "N":
                        hrac1 = False
                    else:
                        print("Zadali jste neplatnou volbu")
                    if hrac1 == False:
                        odpoved_hrac2 = input("Chce si " + name_hrac2 + " liznout kartu y/n: ")
                        if odpoved_hrac2 == "y" or odpoved_hrac2 == "Y":
                            hrac1 = False
                            hrac2 = True
                        elif odpoved_hrac2 == "n" or odpoved_hrac2 == "N":
                            hrac1 = False
                            hrac2 = False
                        else:
                            print("Zadali jste neplatnou volbu") 
                elif soucet2 > 21 :
                    print(name_hrac2, "prekrocil 21") 
                    hrac2 = False
                    hrac1 = False
                    if soucet1 < 21:
                        odpoved_hrac1 = input("Chce si " + name_hrac1 + " liznout kartu y/n: ")
                        if odpoved_hrac1 == "y" or odpoved_hrac1 == "Y":
                            hrac1 = True
                            hrac2 = False
                        elif odpoved_hrac1 == "n" or odpoved_hrac1 == "N":
                            hrac1 = False
                            hrac2 = False
                        else:
                            print("Zadali jste neplatnou volbu")
        if (hrac1 == False and hrac2 == False):              #zacatek vyhodnoceni
            if (soucet1 <= 21 and soucet2 <= 21):
                if soucet1 > soucet2:
                    print(name_hrac1, "vyhral")
                elif soucet1 < soucet2:
                    print(name_hrac2, "vyhral")
                elif soucet1 == soucet2:
                    print("Nastala remiza")
                else:
                    print("Nekde nastala chyba") 
            elif (soucet1 <= 21 and soucet2 > 21):
                print(name_hrac1, "vyhral")
            elif (soucet2 <= 21 and soucet1 > 21):
                print(name_hrac2, "vyhral")
            elif (soucet1 == 21 and soucet2 == 21):
                print("Remiza")
            elif (soucet1 > 21 and soucet2 > 21):
                if soucet1 < soucet2:
                    print("Vyhral", name_hrac1)
                elif soucet2 < soucet1:
                    print("Vyhral", name_hrac2)
                else:
                    print("Nekde nastala chyba")
            odpoved_program = input("Chcete dat novou hru y/n: ")
            if odpoved_program == "y" or odpoved_program == "Y":
                pokracovat_program = True
                pokracovat_hra = False
            elif odpoved_program == "n" or odpoved_program == "N":
                pokracovat_program = False
                pokracovat_hra = False                           #konec vyhodnoceni                 

