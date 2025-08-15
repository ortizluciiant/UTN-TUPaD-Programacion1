#Ejercicio 1
print("Hola Mundo!")

#Fin Algoritmo

#Ejercicio 2

nombre=input("Ingrese su nombre: ")
saludo= f"Hola {nombre}"
print(saludo)

#Fin Algoritmo

#Ejercicio 3
nombre= input("Ingrese nombre: ")
apellido= input("Ingrese su apellido: ")
edad= input("Ingrese su edad: ")
residencia=input("Ingrese su lugar de residencia: ")

print(F"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Fin Algoritmo

#Ejercicio 4

radio=int(input("Ingrese el radio del circulo: "))
pi= 3.14159
area= pi*radio*radio
perimetro= 2*pi*radio

print(f"El area del circulo es {area} y su perimetro es {perimetro}")

#Fin Algoritmo

#Ejercicio 5
segundos=int(input("Ingrese los segundos: "))
valor_hora= int(60)
horas_totales= int(segundos//valor_hora)

print(f"{segundos} segundos equivale a {horas_totales} horas")

#Fin Algoritmo
      
#Ejercicio 6
numero=int(input("Ingrese un numero: "))
print(f"La tabla del {numero} es: ")

#Fin Algoritmo

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")  

 #Fin Algoritmo

#Ejercicio 7
print("Ingrese dos numeros distintos de cero: " )
numero_uno=int(input("Primer numero: "))
numero_dos=int(input("Segundo numero: "))

if numero_uno == 0 or numero_dos == 0 : 
  print("ERROR: Ambos numeros deben ser distintos de cero ")
else:
  
 print("Suma: ", numero_uno+numero_dos) 
 print("Division: ", numero_uno/numero_dos)
 print("Multiplicacion: ",numero_uno*numero_dos)
 print("Resta: ",numero_uno-numero_dos)

 #Fin Algoritmo

#Ejercicio 8
altura=float(input("Ingrese su altura en metros: "))
peso=int(input("Ingrese su peso en Kg: "))
imc=peso / (altura*altura)

print("IMC:",(round(imc,2)))

#Fin Algoritmo

#Ejercicio 9
celsius=float(input("Ingrese los grados celsius: "))
print("Fahrenheit: ", (9/5 * celsius)+32)

#Fin Algoritmo

#Ejercicio 10
numero_uno=int(input("Ingrese el primer numero: "))
numero_dos=int(input("Ingrese el segundo numero: "))
numero_tres=int(input("Ingrese el tercer numero: "))

promedio= ((numero_uno+numero_dos+numero_tres)/3)

print("El promedio es: ", round(promedio, 1 ))

#Fin Algoritmo