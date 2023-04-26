import msvcrt
from os import system


def pide(nombre):
    numero=""
    while not(numero.isnumeric()):
        print("Vas a poner valor a", nombre)
        numero=input("Introduce un numero")
    return int(numero)

def menu():
    system("cls")
    print("a)Introduce un nombre en la agenda")
    print("b)Busca un nombre")
    print("c)Muestra la agenda")
    print("i)Salir")

def poner_nombre():


def busca_nombre():


else:
    nombre=input(f"La persona {nombre} no esta en la agenda")
    print(f"A=¨{A}")
    print(f"B={B}")
    msvcrt.getch()
    
def muestra_nombre():
    print("A", {A})
    print("B", {B})


#main  
A=B=0
entrada=""
while entrada!="i":
     menu()
     entrada=input("Seleciona una opció: ")
if entrada =="a":
     poner_nombre()
if entrada =="b":
    busca_nombre()
if entrada=="c":
    muestra_nombre()
if entrada=="d":
    print(f"")
if entrada=="e":
    print(f"")
if entrada=="f":
    print(f"")
if entrada=="g":
    print(f"")
    invierte()
    muestra_datos()
if entrada=="h":
     muestra_datos()
if entrada =="i":
    muestra_datos()

