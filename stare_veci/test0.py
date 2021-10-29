#!/usr/bin/env python3

from math import sqrt
print("Vitejte v multicalc.")
print()
print("Nejdrive vyberte kalkulacku.")
nexto = True
while(nexto):
    print("1 - Numericka")
    print("2 - Geometricka")
    print()
    vyber = int(input("Kalkulacka:" ))
    if vyber == 2:
        print("Vybrali jste kalkulacku pro vypocet geometrickych tvaru.")
        print()
        print("Zadejte cislo volby: ")
        print("1 - Kruh - z polomeru vypocita obvod, prumer a plochu.")
        print("2 - Ctverec - ze zadane strany vypocita obvod, plochu a uhlopricku.")
        print("3 - Obdelnik - ze zadanych stran vypocita obvod, plochu a uhlopricku.")
        print()
        oper2 = int(input("volba c.: "))
        if oper2 == 1:
            print()
            r = float(input("Zadej polomer kruhu (cm): "))
            print("Obvod = ", 2*3.14*r, "cm")
            print("Plocha = ", 3.14*r**2, "cm^2")
            print("Prumer = ", 2 * r, "cm")
        elif oper2 == 2:
            print()
            a = float(input("Zadejte stranu ctverce (cm): "))
            print("Obvod = ", 4 * a, "cm")
            print("Plocha = ", a * a, "cm^2")
            print("Uhlopricka = ", a * 1.4142, "cm")
        elif oper2 == 3:
            print()
            a = float(input("Zadejte stranu 'a' obdelniku (cm): "))
            b = float(input("Zadejte stranu 'b' obdelniku (cm): "))
            print("Obvod = ",2 * (a + b), "cm")
            print("Plocha = ",a * b, "cm")
            print("Uhlopricka = ",(sqrt(a**2 + b**2)),"cm")
        else:
            print("Toto neni platna volba!")
    elif vyber == 1:
        print("Vybrali jste numerickou kalkulacku.")
        print()
        c1 = float(input("Zadejte prvni cislo: "))
        c2 = float(input("Zadjete druhe cislo: "))
        print()
        print("Zadejte cislo operace: ")
        print("1 - Scitani")
        print("2 - Odcitani")
        print("3 - Nasobeni")
        print("4 - Deleni")
        print("5 - Umocnovani")
        oper1 = int(input("operace c.: "))
        if oper1 == 1:
            print("Soucet:", c1 + c2)
        elif oper1 == 2:
            print("Rozdil:", c1 - c2)
        elif oper1 == 3:
            print("Soucin:", c1 * c2)
        elif oper1 == 4:
            print("Podil:", c1 / c2)
        elif oper1 == 5:
            print(c1, "na", c2, "je:", c1 ** c2)
        else:
            print("Toto neni platna volba!")
    else:
            print("Toto neni platna volba!")
    none = True
    while(none):
        odp = input("\nDalsi priklad? y / n: ")
        print()
        if (odp == "y" or odp == "Y"):
            none = False
        elif (odp == "n" or odp == "N"):
            none = False
            nexto = False
        else:
            pass
input("\nDekuji za pouziti multicalc.\nAplikaci ukoncite libovolnou klavesou. ")
