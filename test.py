#!/usr/bin/env python3

cislo1 = int(input("Zadej cislo k prevodu: "))
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
pocet_2 = 0
for prvek in str(cislo2):
    pocet += 1
if pocet == 1:
    if cislo1 <= 4:
        if cislo1 <= 3:
            pocet_1 = cislo1 / 1
            print("I" * pocet_1)
        else:
            print("IV")
    elif cislo1 == 5:
        print("V")
    elif cislo1 >= 6:
        if cislo1 <= 8:
            pocet_2 = cislo1 - 5
            print("V" + "I" * pocet_2)
        elif cislo1 == 9:
            print("IX")
elif pocet == 2:
    print("ok")
            

        
                      
