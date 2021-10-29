#!/usr/bin/env python

rovnice = input("Zadejte rovnici: ")

cislo1 = rovnice.split()[0]
znaminko2 = rovnice.split()[1]
cislo2 = rovnice.split()[2]
cislo3 = rovnice.split()[4]
znaminko4 = rovnice.split()[5]
cislo4 = rovnice.split()[6]
cislo1_x = False
znaminko2_plus = False
znaminko2_minus = False
cislo2_x = False
cislo3_x = False
znaminko4_plus = False
znaminko4_minus = False
cislo4_x = False
znaminko2_minus_premena = False
znaminko2_plus_premena = False
znaminko4_minus_premena = False
znaminko4_plus_premena = False

for promenna_x in cislo1:
    if promenna_x in "x":
        cislo1_x = True
for promenna_x in cislo2:
    if promenna_x in "x":
        cislo2_x = True
for promenna_x in cislo3:
    if promenna_x in "x":
        cislo3_x = True
for promenna_x in cislo4:
    if promenna_x in "x":
        cislo4_x = True
for promenna_znaminko in rovnice.split()[1]:
    if promenna_znaminko in "+":
        znaminko2_plus = True
    elif promenna_znaminko in "-":
        znaminko2_minus = True 
for promenna_znaminko in rovnice.split()[5]:
    if promenna_znaminko in "+":
        znaminko4_plus = True
    elif promenna_znaminko in "-":
        znaminko4_minus = True 
        
if cislo1_x == False:
    znaminko1 = "-"
if cislo2_x == False:
    if znaminko2_plus == True:
        znaminko2_plus = False
        znaminko2_minus_premena = True
    if znaminko2_minus == True:
        znaminko2_minus = False
        znaminko2_plus_premena = True
if cislo3_x == False:
    znaminko3 = "+"
if cislo4_x == True:
    if znaminko4_plus == True:
        znaminko4_plus = False
        znaminko4_minus_premena = True
    if znaminko4_minus == True:
        znaminko4_minus = False
        znaminko4_plus_premena = True
          
if znaminko2_plus_premena:
    znaminko2 = "+"
if znaminko2_minus_premena:
    znaminko2 = "-"
if znaminko4_plus_premena:
    znaminko4= "+"
if znaminko4_minus_premena:
    znaminko4 = "-"   

"""
if cislo1_x == True:
    print("+")
else:
    print(znaminko1)   
print(znaminko2)
if cislo3_x == True:
    print("-")
else:
    print(znaminko3)
print(znaminko4)
"""
var cislo11
cislo22 = "0"
cislo33 = "0"
cislo44 = "0"

if cislo1_x is True:
    cislo11 = cislo1
if cislo2_x is True:
    cislo22 = cislo22
if cislo3_x is True:
    cislo33 = cislo33
if cislo4_x is True:
    cislo44 = cislo4  
    

    


















