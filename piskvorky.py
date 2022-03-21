def vytvoreni():
    pole = []
    rozmer = int(input("Zadejte rozmer pole: "))
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
    return pole

def hrac1_hra(jmeno1, pole):
    souradnice = input(jmeno1 + ": Zadejte souradnici: ")
    radek = souradnice[0]
    sloupec = souradnice[1]
    pole[int(radek) - 1][int(sloupec) - 1] = "X"
    for i in poles:
        radek = ""
        for j in i:
            radek += " " + str(j)
        print(radek)

def hrac2_hra(jmeno2, pole):
    souradnice = input(jmeno2 + ": Zadejte souradnici: ")
    radek = souradnice[0]
    sloupec = souradnice[1]
    pole[int(radek) - 1][int(sloupec) - 1] = "O"
    for i in pole:
        radek = ""
        for j in i:
            radek += " " + str(j)
        print(radek)
        
def hra(pole, jmeno1, jmeno2):
    while True:
        hrac1_hra(jmeno1, pole)
        hrac2_hra(jmeno2, pole)

def main():
    prezdivka1 = input("Zadejte prezdivku 1. hrace: ")
    prezdivka2 = input("Zadejte prezdivku 2. hrace: ")
    pole = vytvoreni()
    hra(pole, prezdivka1, prezdivka2)


main()
