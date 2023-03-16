import string
cont=input("Introduce una contraseña: ")
if(cont.lower()=="akakinos"):
    print("Contraseña correcta")
    numero=input("Pon un numero: ")
    if numero.isnumeric():
        numero=int(numero)
        if numero>0 and numero <20:
            print("En numero esta entre el 1 y 20")
        else: 
            print("numero fuera de rango")
    else:
        print("No me has puesto un numero")
    print(type(numero))
else :
    print("Contraseña incorrecta")
    print("fin del programa")

