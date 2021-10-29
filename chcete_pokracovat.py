#!/usr/bin/env python

slovo = input("Napiste Python k ukonceni aplikace: ")
pokracovat = True
while pokracovat:
    if slovo == "Python" or slovo == "python":
        print("Zadali jste spravne")
        pokracovat = False
    else:
        pass

