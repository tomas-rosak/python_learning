#!/usr/bin/env python

jmeno = input("Napiste vase jmeno: ")
if 3<=len(jmeno)<=10:
    print("Mate normalni delku slova")
if len(jmeno)<=2:
    print("Mate opravdu kratke jmeno")
if len(jmeno)>10:
    print("Mate opravdu dlouhe jmeno")
