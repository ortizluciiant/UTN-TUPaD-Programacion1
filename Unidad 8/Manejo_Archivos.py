archivo = 'productos.txt'
stock = []


with open(archivo, "a", encoding="utf-8") as f:
    pass 


with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if linea == "":
            continue  
        partes_stock = linea.split(",")
        if len(partes_stock) == 3:
            nombre = partes_stock[0].strip()
            precio = float(partes_stock[1].strip())
            cantidad = int(partes_stock[2].strip())
            stock.append({
                "NOMBRE": nombre,
                "PRECIO": precio,
                "CANTIDAD": cantidad
            })
        

print("\nContenido del stock:")
if not stock:
    print("No hay productos cargados.")
else:
    for producto in stock:
        print(f"Producto: {producto['NOMBRE']} | Precio: ${producto['PRECIO']} | Cantidad: {producto['CANTIDAD']}")


while True:
    agregar = input("\n¿Querés agregar un nuevo producto? (s/n): ").lower()
    if agregar == "s":
        nombre = input("Nombre: ").strip()
        precio = float(input("Precio: ").strip())
        cantidad = int(input("Cantidad: ").strip())

        nuevo = {"NOMBRE": nombre, "PRECIO": precio, "CANTIDAD": cantidad}
        stock.append(nuevo)

 
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(f"{nombre},{precio},{cantidad}\n")

        print("Producto agregado correctamente.")
    elif agregar == "n":
        break
    else:
        print("Opción no válida. Ingresá 's' o 'n'.")


buscar = input("\nIngresá el nombre de un producto para buscar: ").strip()
encontrado = False

for producto in stock:
    if producto["NOMBRE"].lower() == buscar.lower():
        print(f"\nProducto encontrado:")
        print(f"Nombre: {producto['NOMBRE']}")
        print(f"Precio: ${producto['PRECIO']}")
        print(f"Cantidad: {producto['CANTIDAD']}")
        encontrado = True
        break

if not encontrado:
    print("\nProducto no encontrado.")

with open(archivo, "w", encoding="utf-8") as f:
    for producto in stock:
        f.write(f"{producto['NOMBRE']},{producto['PRECIO']},{producto['CANTIDAD']}\n")
