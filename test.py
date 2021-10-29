#!/usr/bin/env python
import random

pouzite_karty = list()
blacklist = list()
opakovani = 1
last = 0
while True:
    karta = random.randint(1, 3)
    if karta not in blacklist:
        print(karta)
        pouzite_karty.append(karta)
        pouzite_karty.sort()
        print(pouzite_karty)
        for number in pouzite_karty:
            if number == last:
                opakovani += 1
            else:
                opakovani = 1
            if opakovani == 4:
                if number not in blacklist:
                    print("dost")
                    blacklist.append(last)
                    print(blacklist)
                    opakovani = 1
            last = number
        input()
