#!/usr/bin/env python
#-i velky maly -o vypise string -v vsechny krom toho kde je string -c pocet
import sys
import os


def pismena(text, string):
    text = text.lower()
    string = string.lower()
    return text, string
    

def o(text, string):  
    text = text.split("\n")
    for i in text:
        if string in i:
            print(string) 


def v(text, string):
    text = text.split("\n")
    for i in text:
        if string in i:
            pass
        else:
            print(i)
            
            
def c(text, string):
    count = 0
    text = text.split("\n")
    for i in text:
        if string in i:
            count += 1
    print(count)
    

def print_radek(text, string):
    text = text.split("\n")
    for i in text:
        if string in i:
            print(i)
                                  

def main():
    prikaz = sys.argv[1:]
    index = 0
    for i in prikaz:
        cesta = os.path.exists(i)
        if cesta:
            string = prikaz[index-1]
            break
        index += 1
            
    with open(i, "r") as soubor:
        text = soubor.read()
    
    if "-i" in prikaz:
        text, string = pismena(text, string)
    if "-o" in prikaz:
        o(text, string)
    elif "-v" in prikaz:
        v(text, string)
    elif "-c" in prikaz:     
        c(text, string)
    else:
        print_radek(text, string)
        
main()
