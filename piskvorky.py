def vytvoreni():
    pole = []
    rozmer = int(input("Zadejte rozmer pole: "))
    rada = int(input("Zadejtte velikost vitezne rady: "))
    radek = []
    for i in range(1, rozmer + 1):
        radek.append(i)
    pole.append(radek)
    for i in range(rozmer):
        radek = []
        for j in range(rozmer):
            radek.append("-")
        pole.append(radek)
    for i in pole:
        radek = ""
        for j in i:
            radek += " " + str(j)
        print(radek)
    return pole, rada

def hrac1_hra(jmeno1, pole):
    dohral = False
    while dohral == False:
        souradnice = input(jmeno1 + ": Zadejte souradnici: ")
        radek = souradnice[0]
        sloupec = souradnice[1]
        if pole[int(radek)][int(sloupec) - 1] != "X" and pole[int(radek)][int(sloupec) - 1] != "O":
            pole[int(radek)][int(sloupec) - 1] = "X"
            for i in pole:
                radek = ""
                for j in i:
                    radek += " " + str(j)
                print(radek)
                dohral = True
        else:
            print("Na teto souradncici je uz policko!")
            dohral = False

def hrac2_hra(jmeno2, pole):
    dohral = False
    while dohral == False:
        souradnice = input(jmeno2 + ": Zadejte souradnici: ")
        radek = souradnice[0]
        sloupec = souradnice[1]
        if pole[int(radek)][int(sloupec) - 1] != "X" and pole[int(radek)][int(sloupec) - 1] != "O":
            pole[int(radek)][int(sloupec) - 1] = "O"
            for i in pole:
                radek = ""
                for j in i:
                    radek += " " + str(j)
                print(radek)
                dohral = True
        else:
            print("Na teto souradncici je uz policko!")
            dohral = False       
        
def hra(pole, jmeno1, jmeno2):
    while True:
        hrac1_hra(jmeno1, pole)
        hrac2_hra(jmeno2, pole)

def main():
    prezdivka1 = input("Zadejte prezdivku 1. hrace: ")
    prezdivka2 = input("Zadejte prezdivku 2. hrace: ")
    pole, rada = vytvoreni()
    hra(pole, prezdivka1, prezdivka2)


main()
