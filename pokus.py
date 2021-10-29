#!/usr/bin/env python

print("Program na vypocet kvadraticke rovnice")
print("Tvar rovnice: ax^2+bx+c=0")
#neni osetrovano zadani a=0 ani cela cisla, cykly jsou az dal
a = int(input("Zadej koeficient a: "))
b = int(input("Zadej koeficient b: "))
c = int(input("Zadej koeficient c: "))
print("Pocitane hodnoty koeficientu: a=",a," b=",b," c=",c)
D=b**2-(4*a*c)
print("diskriminant je:",D)
#neresim, ze mohou vyjit i komplexni cisla, predpocitam si to dopredu
x1 = (-b + (D**(1/2))) / (2*a)
x2 = (-b - (D**(1/2))) / (2*a)
if (D > 0):
    print("Rovnice ma dva realne koreny")
    print (x1,x2)
elif (D == 0):
    print("Rovnice ma jeden dvojnasobny realny koren")
    print (x1)
else: #misto vypisovani, "ze to nejde" vypisi take spravny vysledek
    print("Mam napsat, ze to nejde...")
    print("Rovnice ma vsak reseni v komplexnich cislech")
    print (x1,x2)
