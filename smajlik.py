#!/usr/bin/env python3

smajlik = input("Napiste vaseho smajlika: ")
if ((smajlik == ":-)") or (smajlik == ":)")):
    print("Vas smajlik je stastny")
if ((smajlik == ":-(") or (smajlik == ":(")):
    print("Vas smajlik je smutny")
else:
    print("Vaseho smajlika neznam, zkuste to prosim znovu")
