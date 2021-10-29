#!/usr/bin/env python
 
cislo1 = input("Od: ")
cislo2 = input("Do: ")
cislo3 = int(input("Zadejte cislo od" + " " + cislo1 + " " + 
                   "do" + " " + cislo2 + ": "))
if((int(cislo1)<=cislo3) and (int(cislo2)>=cislo3)):
    print("Spravne")
else:
    print("Spatne")

