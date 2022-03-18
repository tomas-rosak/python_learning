cislo = 0
seznam = []
while cislo != "":
    cislo = input("Zadej cislo: ")
    if cislo != "":
        cislo = int(cislo)
        seznam.append(cislo)
seznam = sorted(seznam)
pocet = len(seznam)
if pocet % 2 == 0:
    index1 = pocet / 2
    prostredni1 = seznam[int(index1) - 1]
    prostredni2 = seznam[int(index1)]
    median = (prostredni1 + prostredni2) / 2
else:
    index = pocet / 2 + 0.5 - 1
    median = seznam[int(index)]
print("Median je", median)
for i in seznam:
    print(i, "je od medianu vzdaleno o", (median - i))    
