titulos=[]
ejemplares=[]
opcion=0
cantidad=0


while opcion != 7:
    print ("\n*****************************************************")
    print ("************BIENVENIDO A LA LIBRERIA*****************")
    print ("*****************************************************")
    print ("\nSeleccione una de las siguientes opciones:")
    print ("\n1 para ingresar libros en cantidades")
    print ("2 para mostrar el titulos de libros ")
    print ("3 para consultar la disponibilidad ")
    print ("4 para listar agotados ")
    print ("5 para agregar un nuevo libro ")
    print ("6 para actualizar ejemplares ")
    print ("7 para salir ")

    opcion=int(input("\nIngrese una opcion: "))
       
    if opcion==1:
        num=input("Ingrese la cantidad de libros: ")
        while not num.isdigit() or int(num) < 0:
            print("Error: debe ingresar un número entero válido mayor o igual a cero.")
            num=input("Ingrese la cantidad de libros: ")
        num=int(num)

        for i in range (num):
            titulo=str(input(f"Ingrese el nombre del titulo {i+1}: ")).upper()
            while titulo.strip() == "":
                print("Error: debe ingresar un Titulo valido (no vacio).")
                titulo=str(input(f"Ingrese el nombre del titulo {i+1}: ")).upper()
            titulo=titulo.strip()
            titulos.append(titulo)

            cant_ejemp = input(f"Ingrese la cantidad de ejemplares de '{titulo}': ")

            while not cant_ejemp.isdigit() or int(cant_ejemp) < 1:
                print("Error: debe ingresar un número entero válido mayor o igual a cero.")
                cant_ejemp = input(f"Ingrese la cantidad de ejemplares de '{titulo}': ")

            ejemplares.append(int(cant_ejemp))

        cantidad+=num
        print("\nLa libreria fue actualizada con exito.")

    elif opcion == 2:
        print("\n\nLista de libros:")

        for i in range (cantidad):
            print(f"{titulos[i]}: {ejemplares[i]}")

    elif opcion == 3:
        titulo=str(input("Ingrese el nombre del libro: ")).upper()
        
        encontrado=False
        for i in range (cantidad):
            if titulos[i]== titulo:
                print(f"Hay {ejemplares[i]} ejemplares")
                encontrado=True
                i=cantidad
        if encontrado==False:
            print("Titulo no encontrado")

    elif opcion == 4:
        print("Los sieguientes titulos no cuentan con ejemplares: ")
        encontrado=False
        for i in range(cantidad):
            if int(ejemplares[i])==0:
                print(titulos[i])
                faltante=True
    
    elif opcion == 5:
        titulo=str(input(f"Ingrese el nombre del titulo: ")).upper()
        while titulo.strip() == "":
                print("Error: debe ingresar un Titulo valido (no vacio).")
                titulo=str(input(f"Ingrese el nombre del titulo: ")).upper()

        titulos.append(titulo.strip())   

        cant_ejemp = input(f"Ingrese la cantidad de ejemplares de '{titulo}': ")

        while not cant_ejemp.isdigit() or int(cant_ejemp) < 0:
            print("Error: debe ingresar un número entero válido mayor o igual a cero.")
            cant_ejemp = input(f"Ingrese la cantidad de ejemplares de '{titulo}': ")

        ejemplares.append(int(cant_ejemp))

        cantidad+=1

        print ("\nTitulo ingresado con exito")

    elif opcion == 6:
        titulo=str(input("Ingrese el nombre del libro: "))
        titulo=titulo.upper()
        
        encontrado=False
        for i in range (cantidad):
            if titulos[i]== titulo:
                print(f"Hay {ejemplares[i]} ejemplar/es")
                encontrado=True
                if ejemplares[i]>0:
                    movimiento= str(input("Ingrese D para Devolucion, P para Prestamo o cualquiera para Cancelar: ")).lower()
                    if movimiento=="d":
                        ejemplares[i]+=1
                        print(f"Ahora hay {ejemplares[i]} ejemplar/es") 
                    elif movimiento=="p":
                        ejemplares[i]-=1
                        print(f"Ahora hay {ejemplares[i]} ejemplar/es") 
                else: 
                    movimiento= str(input("Ingrese D para Devolucion o cualquiera para Cancelar: ")).lower()
                    if movimiento=="d":
                        ejemplares[i]+=1
                        print(f"Ahora hay {ejemplares[i]} ejemplar/es") 
                if movimiento!='d' and movimiento!='p' or movimiento!='d' and ejemplares[i]==0:
                    print("Operacion cancelada.")

            i=cantidad
        if encontrado==False:
            print("Titulo no encontrado")

    elif opcion == 7:
        print("Gracias por utilizar nuestra libreria, hasta luego!")
    
    else:
        print("\n¡¡¡Opcion incorrecta!!!\n")

        
 


