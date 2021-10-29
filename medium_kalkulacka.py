#!/usr/bin/env python

pokracovat = True
print("!Kalkulacka!\n")
while pokracovat:
    cislo1 = float(input("Zadejte prvni cislo: "))
    cislo2 = float(input("Zadejte druhe cislo: "))
    print("")
    print("1 - scitani")
    print("2 - odecitani")
    print("3 - nasobeni")
    print("4 - deleni\n")
    operace = float(input("Cislo operace: "))
    if operace == 1:
        print(cislo1 + cislo2)
    elif operace == 2:
        print(cislo1 - cislo2)
    elif operace == 3:
        print(cislo1*cislo2)
    elif operace == 4:
        print(cislo1/cislo2)
    else:
        print("Spatna volba!")
    nezadano = True
    while nezadano:
        odpoved = input("Prejete si pokracovat y/n")
        if odpoved == "Y" or odpoved == "y":
            nezadano = False
        elif odpoved == "N" or odpoved == "n":
            nezadano = False
            pokracovat = False
        else:
            pass
