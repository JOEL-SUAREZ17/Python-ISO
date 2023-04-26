def factorial (numero):
    fact=1
    for i in range(1,numero+1):
        fact=fact*i
    return fact
#main()
num=int(input("Dime que numero quieres el factorial:"))
print(f"El factorial de {num} es :{factorial(num)}")
