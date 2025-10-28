#Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas.update({"Naranja": 1200})
precios_frutas.update({"Manzana": 1500})
precios_frutas.update({"Pera": 2300})

print(precios_frutas)
#-----------------------------------------------------------------------------------------------
#Ejercicio 2
precios_frutas["Banana"]= 1330
precios_frutas["Manzana"]= 1700
precios_frutas["Melón"]=2800

print(precios_frutas)
#-----------------------------------------------------------------------------------------------
#Ejercicio 3
for fruta in precios_frutas.keys():
    print(fruta)

#-----------------------------------------------------------------------------------------------
#Ejercicio 4

agenda= {}
print("Agenda telefonica")

for i in range (5):
    nombre= str(input("Ingrese el nombre: "))
    num= int(input("Ingrese su numero telefonico:"))

    agenda.update({ nombre : num})

print("Agenta actualizada")

for nombre, num in agenda.items():
    print(f"{nombre}: {num}")

#--------------------------------------------------------------------------------------------------
#Ejercicio 5

frase=input("Ingrese una frase:")

palabras = [palabra.upper() for palabra in frase.split()]
palabras_unicas= set(palabras)

print(f"Palabras unicas: ", palabras_unicas)

contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print(contador_palabras)

#--------------------------------------------------------------------------------------------------
#Ejercicio 6

alumnos={}

for i in range (3):
    nombre=input(f"Ingrese el nombre del alumno:")
    nota=tuple(float(nota) for nota in input("Ingrese 3 notas separadas por espacio: ").split())

    alumnos[nombre]=nota
    i+=1
print("\nPromedio de los alumnos: ")

for nombre,nota in alumnos.items():
    promedio=sum(nota)/len(nota)
    print(f"{nombre}:{promedio}")

#--------------------------------------------------------------------------------------------------
#Ejercicio 7

parcial1 = {105,104,101,110}
parcial2 = {120,105,110,115}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)
solo_uno = parcial1 ^ parcial2  
print("Aprobaron solo uno de los parciales:", solo_uno)
al_menos_uno = parcial1 | parcial2  
print("Aprobaron al menos un parcial:", al_menos_uno)

#--------------------------------------------------------------------------------------------------
#Ejercicio 8

productos = {
    "paracetamol": 50,
    "ibuprofeno": 30,
    "amoxicilina": 20,
    "omeprazol": 40
}

while True:
    print("\nOpciones: 1-Consultar, 2-Agregar stock, 3-Nuevo producto, 4-Salir")
    opcion = input("Ingrese opción: ")

    if opcion == "1":
        nombre = input("Producto a consultar: ").lower()
        if nombre in productos:
            print(f"Stock de {nombre}: {productos[nombre]}")
        else:
            print(f"El producto {nombre} no existe.")

    elif opcion == "2":
        nombre = input("Producto: ")
        if nombre in productos:
            cantidad = int(input("Cantidad a agregar: "))
            productos[nombre] += cantidad
            print(f"Nuevo stock de {nombre}: {productos[nombre]}")
        else:
            print("El producto no existe.")

    elif opcion == "3":
        nombre = input("Nuevo producto: ").lower()
        if nombre in productos:
            print("El producto ya existe.")
        else:
            cantidad = int(input("Cantidad inicial: "))
            productos[nombre] = cantidad
            print(f"Producto {nombre} agregado con {cantidad} unidades.")

    elif opcion == "4":
        print("Gracias...")
        break

    else:
        print("Opción inválida.")

#-------------------------------------------------------------------------------------------------
#Ejercicio 9

agenda = {
    ("lunes", "10:00"): "Turno con medico clinico",
    ("martes", "15:00"): "Clase de Python",
    ("miércoles", "09:00"): "Estudio de laboratorio"
}

dia = input("Ingrese el día a consultar: ").lower()
hora = input("Ingrese la hora (ej: 10:00): ")
clave = (dia, hora)

if clave in agenda:
    print(f"En {dia} a las {hora} hay: {agenda[clave]}")
else:
    print(f"No hay actividad programada el {dia} a las {hora}.")

#--------------------------------------------------------------------------------------------------
#Ejercicio 10

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario invertido:")
print(capitales)