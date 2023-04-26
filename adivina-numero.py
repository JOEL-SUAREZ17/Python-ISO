# Tu adivinas el numero de la maquina
import random
numero=random.randrange(1,101)
intentos=0
jugador=0
while numero != jugador:
    intentos=intentos+1
    jugador=int(input("Introduce un numero entre el 1 y 100:"))
    if (numero<jugador):
        print("El numero es mas pequeño")
    elif (numero>jugador):
        print("El numero es mas grande")
print("Muy bien, lo has acertado. Has necesitado", intentos ,"para acertar")

# La maquina tiene que adivinar el numero que TU le pongas
import random

num=0
intentos=0
ordenador=17
while num != ordenador:
    num=random.randrange(1,101)
    intentos=intentos+1
    if (num<ordenador):
        print("El numero es mas pequeño")
    elif (num>ordenador):
        print("El numero es mas grande")
print("La maquina ha acertaado.Ha necesitado", intentos ,"para acertar")
