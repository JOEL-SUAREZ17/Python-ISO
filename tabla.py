#creamos una tabla de multiplicar
numero=int(input("Pon un numero: "))
i=1
j=1
while j<=10:
    while i<=10:
        print(i, "x" ,j, "=" ,j*i)
        i=i+1
    j=j+1
    print("------------------")
    i=1

    