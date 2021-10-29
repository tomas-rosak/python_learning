#!/usr/bin/env python

cislo = int(input("Zadejte cislo ke zjisteni: "))
prvocislo = False
if (cislo % 2 == 0):
    prvocislo = True
    print("cislo neni prvocislo") 
elif (cislo % 2 == 1):
    delitel = 3
    while (cislo > delitel):
        if (cislo % delitel == 0):
            prvocislo = True
            break
        delitel = delitel + 2
    if prvocislo:
        print("cislo neni prvocislo") 
    else:
        print("cislo je prvocislo")                     
    
    
    
    
    
    

