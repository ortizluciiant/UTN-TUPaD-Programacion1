#EJERCICIO 1

for i in range (0,101):
    print(i)

#FIN EJERCICIO

#EJERCICIO 2

numero = int(input("Ingrese un numero entero: "))
cantidad = str(abs(numero))
contador=0

for _ in cantidad:
    contador+=1

print(f"El número {numero} tiene {contador} caracteres")

#FIN EJERCICIO

#EJERCICIO 4

num1=int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero:"))

suma=0

if num1>num2:
    num1,num2=num2,num1

for i in range ((num1+1),num2 ):
    suma+=i

print(f"La suma de los numeros entre {num1} y {num2} es {suma}")

#FIN EJERCICIO

#EJERCICIO 4

suma=0
num=int(input("Ingrese un numero distinto de cero: (Para finalizar ingrese un 0 ): "))

while num != 0 :
    suma+=num
    num=int(input("Ingrese otro numero distinto de cero: (Para finalizar ingrese un 0 ): "))


print(f"La suma total de los numeros ingresados es: {suma}")

#FIN EJERCICIO

#EJERCICIO 5

import random
numero_adivinar= random.randint(0,9)
intentos=1
num=int(input("Adivine en que numero de 0 al 9 estoy pensando:  "))

while num != numero_adivinar :
    intentos+=1
    num=int(input("Fallaste!! Ingresa otro numero: "))


print(f"Intentos realizados: {intentos}")

#FIN EJERCICIO

#EJERCICIO 6

num=0

for num in range (101,0,-1):
    if num % 2 ==0: 
         print(num)

#FIN EJERCICIO

#EJERCICIO 7

num=int(input("Ingrese un numero positivo: "))

if num < 0 :
    print("Debe ingresar un numero positivo")

elif num == 0:
    print ("No hay numeros para sumar entre 0 y 0")

else:
    suma=0
    for i in range ((num-1),0,-1):
        suma+=i
print (f"La suma entre los numeros 0 y {num} es {suma}")

#FIN EJERCICIO

#EJERCICIO 8

num_positivo = 0
num_negativo = 0
par = 0
impar = 0

num_max = 8
total_ingresados = 0


while total_ingresados < num_max:
    num = int(input(f"Ingrese un número : "))
    
    i = 0
    while i < 1 and num > 0:
        num_positivo += 1
        i += 1
    
    i = 0
    while i < 1 and num < 0:
        num_negativo += 1
        i += 1
   
    i = 0
    while i < 1 and num % 2 == 0:
        par += 1
        i += 1
    

    i = 0
    while i < 1 and num % 2 != 0:
        impar += 1
        i += 1
    
    
    total_ingresados += 1


print(f"La cantidad de números pares es: {par}")
print(f"La cantidad de números impares es: {impar}")
print(f"La cantidad de números positivos es: {num_positivo}")
print(f"La cantidad de números negativos es: {num_negativo}")

#FIN EJERCICIO

#EJERCICIO 9
total = 0
contador = 0
cant_numeros=3

while contador < cant_numeros:
    num = int(input(f"Ingrese el número: "))
    total += num
    contador += 1

media = total / cant_numeros

print(f"La media de los {cant_numeros} números ingresados es: {media}")

#FIN EJERCICIO

#EJERCICIO 10
num = int(input("Ingrese un número: "))
num_original = num
num_invertido = 0

while num > 0:
    digito = num % 10          
    num_invertido = num_invertido * 10 + digito 
    num = num // 10             

print(f"El número {num_original} invertido es: {num_invertido}")

#FIN EJERCICIO

   
