import os
nombreLibro = []
precioLibro = []
cantidadLibros = []
inventario1 = {}
inventario2 = {}

while True:
    os.system("cls")
    print("=== MENU PRINCIPAL ===")
    opc = int(input("1. Registrar en Inventario\n2. Actualizar inventario\n3. Mostrar Inventario\n4. Salir\n"))
    match opc:
        case 1:
            print("\n=== REGISTRO DE LIBROS ===")
            nombre = input("Ingrese el nombre del libro\n").strip().lower()
            precio = float(input("Ingrese el precio del libro\n"))
            cantidad = int(input("Ingrese la cantidad que llego a la bodega\n"))
            if nombre in nombreLibro:
                print("El libro ya existe en el inventario")
                input("Precione una tecla para continuar")
            else:
                nombreLibro.append(nombre)
                precioLibro.append(precio)
                cantidadLibros.append(cantidad)
                inventario1[nombre] = cantidad
                inventario2[nombre] = precio
                input("Libro agregado al sistema, Preciona una tecla para continuar")
        case 2:
            while True:
                os.system("cls")
                print("=== MENU INVENTARIO ===")
                opc2 = int(input("1. Actualizar cantidad de libros\n2. Actualizar precio de libros\n3. Salir\n"))
                match opc2:
                    case 1:
                        nombreN = input("Ingrese el nombre del libro que desea modificar\n").strip().lower()
                        if nombreN in inventario1:
                            cant = int(input("Ingrese una nueva cantidad para el inventario:\n"))
                            inventario1[nombreN] = cant
                            input("Cantidad modificada, Precione una tecla para continuar")
                        else:
                            print("El libro no se encuentra en el sistema, Intente de nuevo")
                            input("Precione una tecla para continuar")
                    case 2:
                        nombreN = input("Ingrese el nombre del libro que desea modificar\n").strip().lower()
                        if nombreN in inventario2:
                            val = int(input("Ingrese un nuevo valor para el inventario:\n"))
                            inventario2[nombreN] = val
                            input("Valor modificado, Precione una tecla para continuar")
                            
                        else:
                            print("El libro no se encuentra en el sistema, Intente de nuevo")
                            input("Precione una tecla para continuar")
                    case 3:
                        break
                    case _:
                        input("Opcion no valida, Precione una tecla para continuar")
        case 3:
            if (len(nombreLibro)== 0):
                print("Aun no hay datos registrados")
                input("Precione una tecla para continuar")
            else:
                for nombre in nombreLibro:
                    prec = ""
                    canti = ""
                    if nombre in inventario1:
                        canti = inventario1[nombre]
                    if nombre in inventario2:
                        prec = inventario2[nombre]

                        print(f"{nombre} tiene un Valor de {prec}, En el inventario hay {canti} libros de este ejemplar")
                input("Precione una tecla para continuar")
        case 4:
            break
        case _:
            input("Opcion no valida, Precione una tecla para continuar")
                    
            
        
            


