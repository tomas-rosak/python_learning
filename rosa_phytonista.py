#!/usr/bin/env python3

print("Rosa phytnonista\n")
print("1 - easy kalkulacka")
print("2 - jak dlouhe mate jmeno")
print("3 - kruh")
print("4 - medium kalkulacka")
print("5 - papousek")
print("6 - zadejte cislo pod nejakou podminkou")
print("7 - porovnavac")
print("8 - privlastnovac")
print("9 - smajlik")
print("10 - zdvojnasobovac")
print("11 - umocnovac")
program = int(input("Zadejte cislo programu: "))

# easy kalkulacka
if program == 1:
    print("Primitivni kalkulacka")
    cislo1 = float(input("Zadejte prvni cislo: "))
    cislo2 = float(input("Zadejte druhe cislo: "))
    print("Soucet:", cislo1 + cislo2)
    print("Rozdil:", cislo1 - cislo2)
    print("Soucin:", cislo1*cislo2)
    print("Podil:", cislo1/cislo2)   

# jak dlouhe mate jmeno
elif program == 2:
    jmeno = input("Napiste vase jmeno: ")
    if 3<=len(jmeno)<=10:
        print("Mate normalni delku slova")
    if len(jmeno)<=2:
        print("Mate opravdu kratke jmeno")
    if len(jmeno)>10:
        print("Mate opravdu dlouhe jmeno")

elif program == 3:
        polomer = float(input("Zadejte polomer kruhu: "))
        obvod = polomer*2*3.14
        obsah = 3.14*polomer**2
        print("Obvod:",obvod)
        print("Obsah:",obsah)
elif program == 4:
    print("!Kalkulacka!\n")
    cislo1 = float(input("Zadejte prvni cislo: "))
    cislo2 = float(input("Zadejte druhe cislo: "))
    print("")
    print("1 - scitani")
    print("2 - odecitani")
    print("3 - nasobeni")
    print("4 - deleni\n")
    operace = float(input("Cislo operace: "))
    if operace == 1:
        print(cislo1 + cislo2)
    elif operace == 2:
        print(cislo1 - cislo2)
    elif operace == 3:
        print(cislo1*cislo2)
    elif operace == 4:
        print(cislo1/cislo2)
    else:
        print("Spatna volba!")
elif program == 5:
    print("Ahoj ja jsem papousek, rad opakuji")
    slovo = input("Rekni mi neco! ")
    print(slovo,"a jeste jednou",slovo)
elif program == 6:
    cislo1 = input("Od: ")
    cislo2 = input("Do: ")
    cislo3 = int(input("Zadejte cislo od" + " " + cislo1 + " " + 
                   "do" + " " + cislo2 + ": "))
    if((int(cislo1)<=cislo3) and (int(cislo2)>=cislo3)):
        print("Spravne")
    else:
        print("Spatne")

elif program == 7:
    cislo1 = input("Od: ")
    cislo2 = input("Do: ")
    cislo3 = int(input("Zadejte cislo od" + " " + cislo1 + " " + 
                   "do" + " " + cislo2 + ": "))
    if(int(cislo1)<=cislo3<=int(cislo2)):
        print("Spravne")
    else:
        print("Spatne")
elif program == 8:
    jmeno = str(input("Ahoj jak se jmenujes? "))s
    vlastnost = str(input("Jaky jsi? "))
    print(jmeno,"je",vlastnost)
elif program == 9:
    smajlik = input("Napiste vaseho smajlika: ")
    if ((smajlik == ":-)") or (smajlik == ":)")):
        print("Vas smajlik je stastny")
    if ((smajlik == ":-(") or (smajlik == ":(")):
        print("Vas smajlik je smutny")
    else:
        print("Vaseho smajlika neznam, zkuste to prosim znovu")
elif program == 10:
    print("!!Zdvojnasobovac!!")
    cislo = int(input("Jake cislo mam zdvojnasobit? "))
    dvojnasobek = cislo*2
    print("Dvojnasobek vaseho cisla je",dvojnasobek)
elif program == 11:
    cislo1 = float(input("Zadejte cislo k umocneni: "))
    cislo2 = float(input("Kterym cislem ho chcete umocnit? "))
    print(cislo1**cislo2)

