#!/usr/bin/env python3
pokracovat = True
while pokracovat:
    print("1 - do rimskych")
    print("2 - do arabskych")
    volba = input("Zadejte cislo prevodu: ")
    if volba == "1":
        cislo1 = int(input("Zadej cislo k prevodu (1-3999): "))
        pocet = 0
        """
        I = 1
        V = 5 
        X = 10 
        L = 50 
        C = 100
        D = 500 
        M = 1000
        """
        cislo2 = 0
        cislo2 = cislo1
        pocet_1 = 0
        for prvek in str(cislo2):
            pocet += 1
        if pocet == 1:
            if cislo1 <= 4:
                if cislo1 <= 3:
                    pocet_1 = cislo1 / 1
                    print("I" * int(pocet_1))
                else:
                    print("IV")
            elif cislo1 == 5:
                print("V")
            elif cislo1 >= 6:
                if cislo1 <= 8:
                    pocet_1 = cislo1 - 5
                    print("V" + "I" * pocet_1)
                elif cislo1 == 9:
                    print("IX")
        elif pocet == 2:
            desitka_list = []
            for prvek in str(cislo2):
                desitka_list.append(prvek)
            desitka = desitka_list[0] 
            if int(desitka) <= 4:
                if int(desitka) <= 3:
                    pocet_1 = int(desitka) / 1
                    cislo_desitka = "X" * int(pocet_1)
                else:
                    cislo_desitka = "XL"
            elif int(desitka) == 5:
                cislo_desitka = "L"
            elif int(desitka) >= 6:
                if int(desitka) <= 8:
                    pocet_1 = int(desitka) - 5
                    cislo_desitka = "L" + "X" * int(pocet_1)
                elif int(desitka) == 9:
                    cislo_desitka = "XC"
            jednotky_list = []
            for prvek in str(cislo2):
                jednotky_list.append(prvek)
            jednotka = jednotky_list[1]
            if 0 < int(jednotka) <= 4:
                if int(jednotka) <= 3:
                    pocet_1 = int(jednotka) / 1
                    cislo_jednotka = ("I" * int(pocet_1))
                else:
                    cislo_jednotka = ("IV")
            elif int(jednotka) == 0:
                cislo_jednotka = ""
            elif int(jednotka) == 5:
                cislo_jednotka = ("V")
            elif int(jednotka) >= 6:
                if int(jednotka) <= 8:
                    pocet_1 = int(jednotka) - 5
                    cislo_jednotka = ("V" + "I" * pocet_1)
                elif int(jednotka) == 9:
                    cislo_jednotka = ("IX")
            else:
                cislo_jednotka = ""
            print(cislo_desitka + cislo_jednotka)
        elif pocet == 3:
            stovka_list = []
            for prvek in str(cislo2):
                stovka_list.append(prvek)
            stovka = stovka_list[0]
            if int(stovka) == 0:
                cislo_stovka = ""
            elif int(stovka) <= 4:
                if int(stovka) <= 3:
                    pocet_1 = int(stovka)/1
                    cislo_stovka = "C" * int(pocet_1)
                else:
                    cislo_stovka = "CD"
            elif int(stovka) == 5:
                cislo_stovka = "D"
            elif int(stovka) >= 6:
                if int(stovka) <= 8:
                    pocet_1 = int(stovka) - 5
                    cislo_stovka = "D" + "C" * pocet_1
                else:
                    cislo_stovka = "CM"
            desitka = stovka_list[1] 
            if int(desitka) <= 4:
                if int(desitka) <= 3:
                    pocet_1 = int(desitka) / 1
                    cislo_desitka = "X" * int(pocet_1)
                else:
                    cislo_desitka = "XL"
            elif int(desitka) == 5:
                cislo_desitka = "L"
            elif int(desitka) >= 6:
                if int(desitka) <= 8:
                    pocet_1 = int(desitka) - 5
                    cislo_desitka = "L" + "X" * int(pocet_1)
                elif int(desitka) == 9:
                    cislo_desitka = "XC"
            jednotka = stovka_list[2]
            if 0 < int(jednotka) <= 4:
                if int(jednotka) <= 3:
                    pocet_1 = int(jednotka) / 1
                    cislo_jednotka = ("I" * int(pocet_1))
                else:
                    cislo_jednotka = ("IV")
            elif int(jednotka) == 0:
                cislo_jednotka = ""
            elif int(jednotka) == 5:
                cislo_jednotka = ("V")
            elif int(jednotka) >= 6:
                if int(jednotka) <= 8:
                    pocet_1 = int(jednotka) - 5
                    cislo_jednotka = ("V" + "I" * pocet_1)
                elif int(jednotka) == 9:
                    cislo_jednotka = ("IX")
            else:
                cislo_jednotka = ""
            print(cislo_stovka + cislo_desitka + cislo_jednotka)
        elif pocet == 4:
            if cislo1 <= 3999:
                tisic_list = []
                for prvek in str(cislo2):
                    tisic_list.append(prvek)
                tisic = tisic_list[0]
                if int(tisic) == 0:
                    cislo_tisic = ""
                elif int(tisic) <= 4:
                    if int(tisic) <=3:
                        pocet_1 = int(tisic) / 1
                        cislo_tisic = "M" * int(pocet_1)
            stovka = tisic_list[1]
            if int(stovka) == 0:
                cislo_stovka = ""
            if int(stovka) <= 3:
                    pocet_1 = int(stovka)/1
                    cislo_stovka = "C" * int(pocet_1)
            elif int(stovka) == 4:
                cislo_stovka == "CD"
            elif int(stovka) == 5:
                cislo_stovka = "D"
            elif int(stovka) >= 6:
                if int(stovka) <= 8:
                    pocet_1 = int(stovka) - 5
                    cislo_stovka = "D" + "C" * pocet_1
                else:
                    cislo_stovka = "CM"
            desitka = tisic_list[2] 
            if int(desitka) <= 4:
                if int(desitka) <= 3:
                    pocet_1 = int(desitka) / 1
                    cislo_desitka = "X" * int(pocet_1)
                else:
                    cislo_desitka = "XL"
            elif int(desitka) == 5:
                cislo_desitka = "L"
            elif int(desitka) >= 6:
                if int(desitka) <= 8:
                    pocet_1 = int(desitka) - 5
                    cislo_desitka = "L" + "X" * int(pocet_1)
                elif int(desitka) == 9:
                    cislo_desitka = "XC"
            jednotka = tisic_list[3]
            if 0 < int(jednotka) <= 4:
                if int(jednotka) <= 3:
                    pocet_1 = int(jednotka) / 1
                    cislo_jednotka = ("I" * int(pocet_1))
                else:
                    cislo_jednotka = ("IV")
            elif int(jednotka) == 0:
                cislo_jednotka = ""
            elif int(jednotka) == 5:
                cislo_jednotka = ("V")
            elif int(jednotka) >= 6:
                if int(jednotka) <= 8:
                    pocet_1 = int(jednotka) - 5
                    cislo_jednotka = ("V" + "I" * pocet_1)
                elif int(jednotka) == 9:
                    cislo_jednotka = ("IX")
            else:
                cislo_jednotka = ""
            print(cislo_tisic + cislo_stovka + cislo_desitka + cislo_jednotka)
    elif volba == "2":
        I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
        cislo1 = input("Zadejte cislo k prevodu: ")
        spravne = True
        pocet = 0
        prvky_cisla = [cislo1]
        for prvek in cislo1:
            pocet += 1
        for x in cislo1:
            if spravne:
                if x == "I" or x == "V" or x == "X" or x == "L" or x == "C" or x == "D" or x == "M":
                    spravne = True
                else:
                    spravne = False
        if spravne:
            prvky_cisla = []
            hodnota = []
            mezi_vypocty = []
            for prvek in cislo1:
                if prvek == "I":
                    prvek = 1
                    prvky_cisla.append(prvek)
                    hodnota.append(1)
                elif prvek == "V":
                    prvek = 5
                    prvky_cisla.append(prvek)
                    hodnota.append(5)
                elif prvek == "X":
                    prvek = 10
                    prvky_cisla.append(prvek)
                    hodnota.append(10)
                elif prvek == "L":
                    prvek = 50
                    prvky_cisla.append(prvek)
                    hodnota.append(50)
                elif prvek == "C":
                    prvek = 100
                    prvky_cisla.append(prvek)
                    hodnota.append(100)
                elif prvek == "D":
                    prvek = 500
                    prvky_cisla.append(prvek)
                    hodnota.append(500)
                elif prvek == "M":
                    prvek = 1000
                    prvky_cisla.append(prvek)
                    hodnota.append(1000)
            opakovani = 1
            last = ""
            spravne = True
            for i in prvky_cisla:
                if spravne:
                    if i == last:
                        opakovani += 1
                    else:
                        opakovani = 1
                    last = i
                    if opakovani <= 3:
                        spravne = True
                    else:
                        spravne = False
            if spravne == False:
                print("Nektery prvek je v cisle vice nez 3krat")
            if spravne:
                opakovani = 0
                last = ""
                po = ""
                x = 1
                for i in hodnota:
                    if i == last:
                        i = i + last
                        mezi_vypocty.append(i)
                    elif opakovani >= 1:
                        if (i != last and po != i) or x == -1:
                            mezi_vypocty.append(i)
                    elif opakovani == 0:
                        if pocet == 1:
                           mezi_vypocty.append(i) 
                        else:
                            po = hodnota[1]
                            if i != po:
                                mezi_vypocty.append(i)   
                    else:
                        print("nekde nastala chyba kurva")
                    last = i
                    opakovani += 1
                    if pocet > x + 1:
                        x += 1
                        po = hodnota[x]
                    else:
                        x = -1
                hodnota = mezi_vypocty
                pocet = 0
                mezi_vypocty = []
                for prvek in hodnota:
                    pocet += 1
                last = 0
                opakovani = 0
                po = ""
                x = 1
                for i in hodnota:
                    if i == last / 2:
                        i = i + last
                        mezi_vypocty.append(i)
                    elif opakovani >= 1: 
                        if (i / 2 != po and i / 2 != last) or x == -1:
                            mezi_vypocty.append(i)
                    elif opakovani == 0:
                        if pocet == 1:
                            mezi_vypocty.append(i)
                        else:
                            po = hodnota[1]
                            if i != po * 2:
                                mezi_vypocty.append(i)         
                    last = i
                    opakovani += 1
                    if pocet > x + 1:
                        x += 1
                        po = hodnota[x]
                    else:
                        x = -1
                hodnota = mezi_vypocty 
    else:
        print("Zadali jste spatne cislo")
#I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
