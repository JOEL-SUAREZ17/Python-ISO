import msvcrt
from os import system
system("cls")
print("Piensa un numero del 1 al 100 y pusla una tecla cuando estés listo")
msvcrt.getch()
min=1
max=100
intentos=0
encontrado=True
seguir=False
while seguir:
    intentos+=1
    numero=int((min+max)/2)
    print(f"Es {numero} (s/n)")
    resp=msvcrt.getch().decode("utf-8").lower()
    if resp=="s":
        print("Lo has acertado")
        seguir=False
        encontrado=True
    else:
        resp=input("Es mayor (s/n)")
        if resp=="s":
            min=numero+1
        else:
            max=numero-1
    if min>max:
        print("Me has engañado")
        seguir=False
if encontrado:
    print(f"He necesitado {intentos} intentos")

# a=msvcrt.getch().decode("utf-8").lower()
# print(a)
# print(type(a))
# if a=="s":
#     print("SI")
# else:
#     print("NO")6  
