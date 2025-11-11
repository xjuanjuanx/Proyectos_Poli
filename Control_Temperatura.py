import os
temperatura = []
salir = False
cont = 0
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
                print(f"La temperatura ingresada {temp} supera los 8°C")
                cont +=1
            input("Dato almacenado, Presione una tecla para continuar")
        case 2:
            if (len(temperatura)== 0):
                print("No hay temperturas registradas")
            else:
                for i in range(0,len(temperatura)):
                    print(f"Temperatura #{i+1} es: {temperatura[i]}°C")
                input("Dato almacenado, Presione una tecla para continuar")
        case 3:
            if (len(temperatura)== 0):
                print("No hay Datos para el promedio")
                input("Presione una tecla para continuar")
            else:
                print(f"El promedio de temperaturas es: {round(sum(temperatura)/len(temperatura),2)}°C")
                input("Presione una tecla para continuar")
        case 4:
            print(f"Cantidad de temperaturas que excedieron los 8°: {cont}")
            input("Presione una tecla para continuar")
        case 5:
            print("Hasta luego")
            salir = True
            input("Presione una tecla para continuar")
        case _:
            print("Opcion no valida")
            input("Presione una tecla para continuar")
