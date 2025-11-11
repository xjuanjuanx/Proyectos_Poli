"""
Caso 2: Clasificación de Clientes en una Tienda Virtual
La tienda clasifica a sus clientes según sus compras mensuales. Si el monto es mayor a 1.000.000 es “Premium”, si es mayor a 500.000 es “Oro”, de lo contrario es “Básico”.
Objetivos:
•	Almacenar nombre y total comprado de varios clientes.
•	Clasificarlos en una categoría.
Retos:
•	Guardar datos en diccionario con nombre como clave.
•	Mostrar la categoría de cada cliente.
Estructuras usadas: diccionarios, condicionales, listas

"""
import os
clientes = []
ventas = []
categoria = {}

while True:
    os.system("cls")
    print("==== MENU PRINCPIAL ====")
    opc = int(input("Ingrese una opcion:\n1. Registrar una venta\n2. Ver categoria de clientes\n3. Salir\n"))
    match opc:
        case 1: 
            nombre = input("Ingrese el nombre del cliente:\n").lower()
            valor = float(input("Ingrese el valor de lo que llevara:\n"))
            if nombre in clientes:
                indice = clientes.index(nombre)
                nuevo_valor = ventas[(indice)]+valor
                categoria[nombre] = nuevo_valor
                if nuevo_valor > 500000 and valor <= 1000000 :
                    categoria[nombre] = "GOLD"
                elif nuevo_valor > 1000000:
                    categoria[nombre] = "PREMIUM"
                else:
                    categoria[nombre] = "BASICO"
            else:
                clientes.append(nombre)
                ventas.append(valor)
                categoria[nombre] = valor
                if valor > 500000 and valor <= 1000000 :
                    categoria[nombre] = "GOLD"
                elif valor > 1000000:
                    categoria[nombre] = "PREMIUM"
                else:
                    categoria[nombre] = "BASICO"
            input("Datos guardados, Precione una tecla para continuar...")      
        case 2:
            if (len(clientes) == 0):
                print("Aun no hay clientes registrados")
                input("Precione una tecla para continuar...")
            else:
                print(categoria)
                input("Precione una tecla para continuar...")
        case 3:
            break
        case _:
            print("Opcion no valida")
            input("Precione una tecla para continuar...")         
    
