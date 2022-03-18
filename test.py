def zmena_textu(text):
    text = text.lower()
    text2 = ""
    for i in text:
        text1 = ""
        for x in i:
            if x == "ě":
                x = "e"
            elif x == "č":
                x = "c"
            elif x == "ř":
                x = "r"
            elif x == "ž":
                x = "z"
            elif x == "ý":
                x = "y"
            elif x == "á":
                x = "a"
            elif x == "í":
                x = "i"
            elif x == "é":
                x = "e"
            elif x == "ú" or x == "ů":
                x = "u"
            elif x == "š":
                x = "s"
            text1 = text1 + x
        text2 = text2 + text1
    veta = text2
    return veta
    
veta = input("Zadej vetu: ")
pocet_slov = int(input("Zadejte pocet hledanych slov: "))
slova = []
opakovani = 0
while opakovani < pocet_slov:
    slovo = input("Zadej hledane slovo: ")
    slovo = zmena_textu(slovo)
    slova.append(slovo)
    opakovani += 1
veta = zmena_textu(veta)
for obj in slova:    
    if obj in veta:
        print("Hledane slovo", "'" + str(obj) + "'", "je ve vete")
    else:
        print("Hledane slovo", "'" + str(obj) + "'", "neni ve vete")

    
