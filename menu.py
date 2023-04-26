import msvcrt
from os import system


def pide(letra):
    numero=""
    while not(numero.isnumeric()):
        print("Vas a poner valor a", letra)
        numero=input("Introduce un numero")
    return int(numero)

def menu():
    print("a)Introduce A")
    print("b)Introduce B")
    print("c)Suma A y B")
    print("d)Resta A y B")
    print("e)Multiplicar A y B")
    print("f)Dividir A y B")
    print("g)Invertir A y B")
    print("h)Ver A y B")
    print("i)Salir")

def muestra_datos():
    print(f"A=¨{A}")
    print(f"B={B}")
    msvcrt.getch()
    
def suma():
    return A+B

def resta():
    return A-B

def multiplica():
    return A*B

def divide():
    return A/B

def invierte():
    global A,B
    c=A
    A=B
    B=c

def muestra():
    print("A", {A})
    print("B", {B})

#main  
A=B=0
entrada=""
while entrada!="i":
     menu()
     entrada=input("Seleciona una opció: ")
if entrada =="a":
     A= pide("a")
if entrada =="b":
     B= pide("B")
if entrada=="c":
    print(f"La suma de  {A}+{B}={suma()}")
if entrada=="d":
    print(f"La resta de  {A}+{B}={resta()}")
if entrada=="e":
    print(f"La multiplicación de {A}*{B}={multiplica()}")
if entrada=="f":
    print(f"La división de  {A}/{B}={divide()}")
if entrada=="g":
    print(f"He invertido A y B")
    invierte()
    muestra_datos()
if entrada=="h":
     muestra_datos()
if entrada =="i":
    muestra_datos()

# suma a+b
# resta a-b
# miltiplicar a*b
# divide a/b
# muestra a y b
# invierte a=b b=a
# salir 

