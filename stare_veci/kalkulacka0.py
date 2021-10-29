#!/usr/bin/env python3

print("Kalkulačka\n")
prvni_cislo = int(input("První číslo: "))
operace = str(input("Operace: "))
druhe_cislo = int(input("Druhé číslo: "))
vysledek1 = (prvni_cislo + druhe_cislo)
vysledek2 = (prvni_cislo - druhe_cislo)
vysledek3 = (prvni_cislo*druhe_cislo)
vysledek4 = (prvni_cislo/druhe_cislo)
if operace == "+":
    print("Výsledek:", vysledek1)
elif operace == "-":
    print("Výsledek:", vysledek2)
elif operace == "*":
    print("Výsledek:", vysledek3)
elif operace == ":":
   print("Výsledek:", vysledek4)
else:
    print("Prosím, zkuste to znova")
