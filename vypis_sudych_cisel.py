#!/usr/bin/env python3
print("Program vypise vsechny suda cisla")
maximum = int(input("Do ktere cisla?"))
cislo = 0
while (cislo <= maximum):
    if (cislo % 2 == 0):
        print(cislo)
    cislo = cislo + 1
