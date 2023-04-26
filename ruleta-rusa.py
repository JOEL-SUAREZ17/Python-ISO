import random

rondas=0
perdidas=0
ganadas=0

while rondas <3:
    rondas=rondas+1
    persona=int(input("Introduce un numero del 1 al 6: "))
    num=random.randrange(1,6)
    print(num)
if (persona == num):
    print("Has muerto")
    perdidas=perdidas+1
else:
    print("Has ganado, la bala era el numero", num)
    ganadas=ganadas+1
