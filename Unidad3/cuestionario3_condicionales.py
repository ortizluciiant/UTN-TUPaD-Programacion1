#EJERCICIO 1

edad=int(input("Ingrese su edad: "))

if edad > 18 :
    print("Es mayor de edad")
else: 
    print("Es menor de edad")

#FIN DEL ALGORITMO------------------------------------------------------------------------


#EJERCICIO 2

nota=int(input("Ingrese su nota:"))

if nota >= 6 :
    print("Aprobado")

else:
    print("Desaprobado")

#FIN DEL ALGORITMO------------------------------------------------------------------------


#EJERCICIO 3
numero=int(input("Ingrese un numero par: "))

if numero % 2 == 0 :
    print("Es un numero par." )
else:
    print("Por favor ingrese un numero par.") 

#FIN DEL ALGORITMO------------------------------------------------------------------------

#EJERCICIO 4

edad= int(input("Ingrese su edad: "))

if edad < 12:
    print("Categoria: Niño/a")
elif (edad >= 12) and (edad < 18):
    print("Categoria: Adolescente")
elif (edad >= 18) and (edad < 30):
    print("Categoria: Adulta/o Joven")

else:
 print("Categoria: Adulto/a")

#FIN DEL ALGORITMO------------------------------------------------------------------------


#EJERCICIO 5

contra= input("Ingrese la contraseña : ")

if len(contra) >= 8 and len(contra) <= 14 : 
    print ("Ha ingresado una contraseña correcta")

else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#FIN DEL ALGORITMO------------------------------------------------------------------------

#EJERCICIO 6

import random
from statistics import mode, median, mean

numeros_aleatorios= [random.randint(1,100) for i in range (50)]

moda = float(mode(numeros_aleatorios))
mediana = float(median(numeros_aleatorios))
media =float(mean(numeros_aleatorios))

print("Moda:",moda)
print("Mediana:",mediana)
print("Media:",media)

if (media>mediana) and (mediana>moda):
    print("Sesgo positivo")

elif (media < mediana) and (mediana < moda):
    print ("Sesgo negativo ")

elif media== mediana==moda: 
    print("Sin sesgo")
else:
    print("Error")

#FIN DEL ALGORITMO------------------------------------------------------------------------


#EJERCICIO 7

frase= input("Ingrese un frase: ")

if frase[-1].lower() in "aeiou":
    frase+="!"
print(frase)

#FIN DEL ALGORITMO------------------------------------------------------------------------


#EJERCICIO 8

nombre=input("Ingrese su nombre: ")

num=int(input("Elija una opcion 1 , 2 o 3: "))

if num == 1:
    print(nombre.upper())
elif num==2: print(nombre.lower())

elif num==3: print(nombre.title())

else:
    print("Debe elegir un numero del 1 al 3")

#FIN DEL ALGORITMO------------------------------------------------------------------------


#EJERCICIO 9

terremoto= float(input("Ingrese la magnitud del terremoto 1/2/3/4/5/6/7: "))

if terremoto < 3 :
    print("Muy leve, imperceptible")
elif (terremoto >= 3) and (terremoto < 4): print("Leve, ligeramente perceptible.")
elif(terremoto >= 4) and (terremoto < 5 ): print("Moderado, sentido por personas, pero generalmente no causa daños")
elif(terremoto >= 5) and (terremoto < 6): print("Fuerte, puede causar daños en estructuras debiles")
elif(terremoto >= 6) and (terremoto < 7): print("Muy fuerte, puede causar daños significativos")
else:
    print("Extremo, puede causar grandes daños a gran escala")

#FIN DEL ALGORITMO------------------------------------------------------------------------


#EJERCICIO 10


hemisferio= input("Ingrese hemisferio N/S: ").lower()
mes=int(input("Ingrese el mes,(Ejemplo para Enero : 1, para Marzo: 3)  :  "))
dia= int(input("Ingrese dia:  "))


if hemisferio == "n":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("INVIERNO")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("PRIMAVERA")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("VERANO")
    else:
        print("OTOÑO")

elif hemisferio == "s":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("VERANO")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("OTOÑO")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("INVIERNO")
    else:
        print("PRIMAVERA")

else:
    print("Hemisferio inválido")

#FIN DEL ALGORITMO------------------------------------------------------------------------



