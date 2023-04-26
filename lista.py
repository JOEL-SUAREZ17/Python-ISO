import msvcrt
from os import system
fichero = open("fichero.txt", "r")

def pide():
	numero=""
	while not(numero.isnumeric()):
		numero=input ("Introduce un numero: ")
	return int(numero)	

def menu():
	system("cls")
	print("a) Introducir valor en la lista")
	print("b) Mostrar lista")
	print("c) Recuento de los elementos de la lista")
	print("d) Suma de los elementos de la lista")
	print("e) Calcula la mediana de la lista")
	print("f) Muestra el numero más pequeño")
	print("g) Muestra el numero más grande")
	print("h) Muestra la posición del más pequeño")
	print("i) Muestra la posición del más grande")
	print("j) Guarda los datos")
	print("k) Carga los datos")
	print("q) Salir")

def añadir_elemento():
	lista.append(pide())

def elegir_opcion(opcion):
	if opcion =="a":
		lista.append(pide())
	if opcion =="b":
		muestra_datos()
		msvcrt.getch()
	if opcion=="c":
		print(f"Los elementos de la lista son {cuenta_datos()}")
		msvcrt.getch()
	if opcion=="d":
		print(f"La suma de los elementos de la lista són {suma_elementos()}")
		msvcrt.getch()
	if opcion=="e":
		print(f"La mediana és {mediana_elementos()}")
		msvcrt.getch()
	if opcion =="f":
		print(f"El numero más peqeuño es {menor_elemento()}")
		msvcrt.getch()
	if opcion =="g":
		print(f"El mayor número es {mayor_elemento()}")
		msvcrt.getch()
	if opcion=="h":
		print(f"La posiión del minimo és {pos_min()}")
		msvcrt.getch()
	if opcion=="i":
		print(f"La posicion maxima es {pos_max()}")
		msvcrt.getch()
	if opcion=="j":
		print(f"Datos gardados {guardar_datos()}")
		msvcrt.getch
	if opcion=="k":
		print(f"Datos cargados {cargar_datos()}")
		msvcrt.getch

def muestra_datos():
	for elemento in lista:
		print(elemento)
def cuenta_datos():
		return len(lista)
def suma_elementos():
	suma=0
	for i in lista:
		suma+=i
	return suma
def mediana_elementos():
	return suma_elementos()/cuenta_datos()
def menor_elemento():
	max=lista[0]
	for i in lista:
		if i > max:
			max=i
		return max
def mayor_elemento():
	min=lista[0]
	for i in lista:
		if i < min:
			min=i
		return min
def pos_min():
	numero=min()
	posicio=0
	for i in range(len(lista)):
		if lista[i]>lista[posicio]:
			posicio=i
	return posicio

def pos_max():
	numero=max()
	posicio=0
	for i in range(len(lista)):
		if lista[i]<lista[posicio]:
			posicio=i
	return posicio
def guardar_datos():
	datos=0
	fichero=open("fichero.txt", "w")
	for i in lista:
		fichero.write(str(i)+"\n")
	datos+=1
	return datos
	
def cargar_datos():
	global lista
	lista=[]
	numero=0
	fichero=open("fichero.txt", "r")
	for datos in fichero:
		lista.append(int(datos))
		numero+=1
	return numero


#principal		
lista=[]
entrada=""
while entrada!="q":
	menu()
	entrada=input("Introduce una opcion: ")
	elegir_opcion(entrada)
	