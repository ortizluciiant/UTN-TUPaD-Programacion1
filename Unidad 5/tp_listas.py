#EJERCICIO 1

notas=[8,5,9,4,5,3,5,6,7,1]
print("Notas: ")
for n in notas:
    print (n)


promedio= sum(notas)/10
print(f"\nEl Promedio es: {promedio}")


print(f"\nLa nota maxima es: {max(notas)}")
print (f"La nota minima es: {min(notas)}")

#-------------------------------------------------------------------------------------------------

#EJERCICIO 2

productos=[]

for n in range (5):
   producto= str(input(f"Ingrese el producto numero {n+1}: ")).upper()
   productos.append(producto)

print("\nProductos: ")
for items in (sorted(productos)):
    print (items)

eliminar= str(input("\nDesea eliminar un producto ? si/no:  ")).upper()

if eliminar == "SI":
    prod_eliminar= str(input("Que producto desea eliminar: "))

    if prod_eliminar in (productos):
        productos.remove(prod_eliminar)
        print(f"El producto {prod_eliminar} se elimino correctamente")
        print ("\nLista actualizada:")
        for p in productos:
            print(p)
    else:
        print(f"\nProducto '{prod_eliminar}' no encontrado en la lista.")
elif eliminar == "NO":
    print("\nHasta pronto")

else: print("Error, debe ingresar si o no")

#-------------------------------------------------------------------------------------------------

#EJERCICIO 3:

import random
pares=[]
impares=[]

for i in range (15):
    num= random.randint(1,100)
    if num % 2==0:
        pares.append(num)     
    else:
        impares.append(num)

print("Numeros Pares: ")
for p in pares:
    print(p)
print(f"Total de pares: {len(pares)}")

print("\nNumeros Impares: ")
for i in impares:
    print(i)
print(f"Total de impares: {len(impares)}")

#-------------------------------------------------------------------------------------------------

#EJERCICIO 4:

lista = [1,3,5,3,7,1,9,5,3]
lista_dos = []

for num in lista:
    if num not in lista_dos:  
        lista_dos.append(num)

print("Lista sin repetidos: ")

for l in lista_dos:
    print(l)

#-------------------------------------------------------------------------------------------------

#EJERCICIO 5:

estudiantes = []

for n in range(8):
    alumno = input(f"Ingrese alumno presente {n+1}: ").upper()
    estudiantes.append(alumno)

print("\nLista inicial de estudiantes:")
for e in estudiantes:
    print(e)

while True:
    agregar = input("\n¿Desea agregar algún estudiante? si/no: ").upper()
    if agregar == "SI":
        estudiante_agregado = input("¿Qué estudiante desea agregar?: ").upper()
        estudiantes.append(estudiante_agregado)
        print("\nLista actualizada:")
        for e in estudiantes:
            print(e)
    elif agregar == "NO":
        break
    else:
        print("Error: debe ingresar 'SI' o 'NO'.")


while True:
    eliminar = input("\n¿Desea eliminar algún estudiante? si/no: ").upper()
    if eliminar == "SI":
        estudiante_eliminado = input("¿Qué estudiante desea eliminar?: ").upper()
        if estudiante_eliminado in estudiantes:
            estudiantes.remove(estudiante_eliminado)
            print(f"\n{estudiante_eliminado} fue eliminado.")
            print("Lista actualizada:")
            for e in estudiantes:
                print(e)
        else:
            print(f"{estudiante_eliminado} no se encuentra en la lista.")
    elif eliminar == "NO":
        break
    else:
        print("Error: debe ingresar 'SI' o 'NO'.")

print("\nLista final de estudiantes:")
for e in estudiantes:
    print(e)

#-------------------------------------------------------------------------------------------------

#EJERCICIO 6:

numeros = [1, 2, 3, 4, 5, 6, 7]

ultimo = numeros[-1]

for i in range(len(numeros)-1, 0, -1):
    numeros[i] = numeros[i-1]

numeros[0] = ultimo

print("Lista rotada a la derecha:")
print(numeros)

#-------------------------------------------------------------------------------------------------

#EJERCICIO 7:

temperaturas=[
    [8,16],
    [12,20],
    [13,26],
    [15,29],
    [18,24],
    [20,25],
    [22,28]
]

temp_min=0
temp_max=0

for dia in (temperaturas):
    temp_min+=dia[0]
    temp_max+=dia[1]

promedio_min=round((temp_min/len(temperaturas)),1)
promedio_max=round(temp_max/len(temperaturas),1)

print(f"\nEl promedio de la minima es {promedio_min} y el promedio de la maxima temperatura es {promedio_max} ")

mayor_temp=-1
dia=-1

for i in range(7):
    amplitud= temperaturas[i][1]-temperaturas[i][0]
    if amplitud > mayor_temp:
        mayor_temp=amplitud
        dia=i+1

print(f"La mayor amplitud fue {mayor_temp} y se dio en el dia {dia}")

#-------------------------------------------------------------------------------------------------

#EJERCICIO 8

estudiantes= ["ANA", "JUAN", "MARCOS","MICAELA", "MARTIN"]
materia=["PROGRAMACION", "MATEMATICA", "AYSO"]
notas = [
    [7, 8, 8],   
    [9, 6, 9],   
    [5, 7, 5],   
    [8, 9, 4],   
    [6, 7, 7]    
]
mayor_promedio = 0
materia_mayor = ""
for i in range(len(estudiantes)):
    promedio= sum(notas[i])/len(notas[i])
    print (f"{estudiantes[i]}: {round((promedio),1)}")

alumno=len(estudiantes)
asignatura=len(materia)

for p in range (asignatura):
    suma=0
    for i in range (alumno):
        suma+=notas[i][p]
        promedio_final=suma/alumno

    if promedio_final > mayor_promedio:
        mayor_promedio = promedio_final
        materia_mayor = materia[p]

print("\nMateria con mayor promedio:")    
print(f"{materia_mayor}: {round(mayor_promedio,1)}")

#-------------------------------------------------------------------------------------------------

#EJERCICIO 9

tateti= [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

jugadas=0

while jugadas < 9:

    for fila in tateti:
        print(" ".join(fila))
    print()

    jugador=str(input("Elija una opcion: X / O: ")).upper()
    fila=int(input("Ingrese fila:"))-1
    columna=int(input("Ingrese columna:"))-1

    if tateti[fila][columna] == "-":
        tateti[fila][columna] = jugador

    else: print("Casilla ocupada, intente de nuevo.")

    ganador = None

    for i in range(3):
        if tateti[i][0] == tateti[i][1] == tateti[i][2] != "-":
            ganador = tateti[i][0]

    for i in range(3):
        if tateti[0][i] == tateti[1][i] == tateti[2][i] != "-":
            ganador = tateti[0][i]

   
    if tateti[0][0] == tateti[1][1] == tateti[2][2] != "-":
        ganador = tateti[0][0]

    if tateti[0][2] == tateti[1][1] == tateti[2][0] != "-":
        ganador = tateti[0][2]

   
    if ganador:
        for fila in tateti:
            print(" ".join(fila))
            jugadas=9
    print(f"\n¡El ganador es {ganador}!")

for columna in tateti:
    print(" ".join(columna))

    jugadas+=1

#-------------------------------------------------------------------------------------------------

#EJERCICIO 10
ventas = [
    [8, 3, 5, 4, 2, 3, 6],  
    [2, 2, 5, 4, 3, 1, 7],   
    [3, 2, 5, 3, 4, 6, 2],   
    [2, 7, 5, 4, 3, 4, 8]   
]

productos = ["MANZANA", "BANANA", "PERA", "DURAZNO"]
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

total_producto = []
for i in range(len(productos)):
    total = sum(ventas[i])
    total_producto.append(total)

print("El total vendido por cada producto es:")
for p in range(len(productos)):
    print(f"{productos[p]}: {total_producto[p]}")

mayor_venta = []
for c in range(len(dias)):
    total = 0
    for i in range(len(productos)):
        total += ventas[i][c]
    mayor_venta.append(total)

maximo_ventas = mayor_venta[0]
dia_max = 0
for i in range(len(mayor_venta)):
    if mayor_venta[i] > maximo_ventas:
        maximo_ventas = mayor_venta[i]
        dia_max = i

print(f"\nDía con mayores ventas totales: {dias[dia_max]} ({maximo_ventas} ventas)")

venta_max = total_producto[0]
max_producto = 0
for i in range(len(total_producto)):
    if total_producto[i] > venta_max:
        venta_max = total_producto[i]
        max_producto = i

print(f"Producto más vendido en la semana: {productos[max_producto]} ({venta_max} ventas)")
