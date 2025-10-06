#EJERCICIO 1

def imprimir_hola_mundo ():
    print("Hola Mundo!")

imprimir_hola_mundo()

#----------------------------------------------------------------------------------------------
#EJERCICIO 2

def saludar_usuario(nombre):
    return(f"Hola, {nombre}")

nombre_usuario=input("Ingrese su nombre: ")
saludo=saludar_usuario(nombre_usuario)
print(saludo)

#----------------------------------------------------------------------------------------------
#EJERCICIO 3


def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

print("Hola, ingrese su informacion: ")
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su residencia: ")

informacion_personal(nombre,apellido,edad,residencia)
#----------------------------------------------------------------------------------------------

#EJERCICIO 4

def calcular_area_circulo(radio):
    return 3.1416*radio**2
3.5
def calcular_perimetro_circulo(radio):
    return 2*3.1416*radio


radio=float(input("Ingrese el radio del circulo: "))

print(f"El area del circulo es {round(calcular_area_circulo(radio),2)} y su perimetro es {round(calcular_perimetro_circulo(radio),2)}")
#----------------------------------------------------------------------------------------------
#EJERCICIO 5

def  segundos_a_horas(segundos):
    return segundos/60

segundos=int(input("Ingrese los segundo: "))

print(f"{segundos} segundos, corresponde a {round(segundos_a_horas(segundos),2)} horas ")

#----------------------------------------------------------------------------------------------
#EJERCICIO 6

def tabla_multiplicar(numero):
    for i in range (1,11):
         print(f"{numero} x {i} = {numero * i}")


num=int(input("Ingrese un numero: "))

tabla_multiplicar(num)
#----------------------------------------------------------------------------------------------
#EJERCICIO 7

def operaciones_basicas(a, b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    divicion=a/b
    if b == 0:
        print("Error no se puede dividir por 0 ")
    return (suma,resta,multiplicacion,divicion)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#----------------------------------------------------------------------------------------------
#EJERCICIO 8
def calcular_imc(peso, altura):
    return peso/altura**2

print("IMC")

peso=float(input("Ingrese su peso en Kg: "))
altura=float(input("Ingrese su altura en metros: "))

print(f"Su IMC es {round(calcular_imc(peso,altura),2)}")

#----------------------------------------------------------------------------------------------
#EJERCICIO 9

def  celsius_a_fahrenheit(celsius):
    return (celsius* 9/5) + 32

celsius=float(input("Ingrese los celsius: "))

print(f"{celsius} C equivalen a {celsius_a_fahrenheit(celsius)} F")

#----------------------------------------------------------------------------------------------
#EJERCICIO 10

def calcular_promedio(a, b, c):
    return (a+b+c)/3

num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))

print(f"\nEl promedio de los numeros igresados es: {round(calcular_promedio(num1,num2,num3),1)}")





