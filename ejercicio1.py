"""
Caso 1: Control de Temperatura en una Bodega
Una bodega de alimentos perecederos requiere un sistema que verifique las temperaturas registradas cada hora. Si alguna supera los 8°C, se debe alertar al supervisor.
Objetivos:
•	Leer datos (estructura secuencial).
•	Usar condicional para validar límites.
•	Usar listas para almacenar lecturas.
Retos:
•	Mostrar todas las temperaturas.
•	Calcular promedio.
•	Mostrar cuántas excedieron el límite.

Estructuras usadas: listas, secuencias, condicionales

"""
import os
temperatura = []
salir = False
cont = 0
tempA = 0
tempB = 99999
while not salir:
    os.system("cls")
    print("===== MENUS PRINCIPAL =====")
    print("1. Ingresar Temperaturas\n2. Mostrar Temperaturas\n3. Promedio de temperaturas\n4. Mostrar cuantas excedieron Limite\n5. Salir\n")
    opc = int(input("Ingrese una opcion:\n"))
    
    match opc:
        case 1:
            temp = float(input("\nIngrese la temperatura actual:\n"))
            temperatura.append(temp)
            if temp > 8.0:
                print(f"!!!ALERTA!!!.... La temperatura ingresada {temp} supera los 8°C")
                cont +=1
            input("Dato almacenado, Precione una tecla para continuar")
        case 2:
            if (len(temperatura)== 0):
                print("No hay temperturas registradas")
            else:
                for i in range(0,len(temperatura)):
                    print(f"Temperatura #{i+1} es: {temperatura[i]}°C")
                input("Dato almacenado, Precione una tecla para continuar")
        case 3:
            if (len(temperatura)== 0):
                print("No hay Datos para el promedio")
                input("Precione una tecla para continuar")
            else:
                print(f"El promedio de temperaturas es: {round(sum(temperatura)/len(temperatura),2)}°C")
                input("Precione una tecla para continuar")
        case 4:
            print(f"Cantidad de temperaturas que excedieron los 8°: {cont}")
            input("Precione una tecla para continuar")
        case 5:
            print("Hasta luego")
            salir = True
            input("Precione una tecla para continuar")
        case _:
            print("Opcion no valida")
            input("Precione una tecla para continuar")