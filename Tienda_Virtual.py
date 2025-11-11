
import os
venta = {}
clientes = []
clasificacion = {}
contClasi = {}
gesDirre = {}
gesTel = {}
gesCorreo = {}
gesCiudad = {}
gestion = {}
cont2 = vTotal = cont = contVen = 0
cliPedido = ()
pedidos = []


while True:
    os.system("cls")
    print("    ===== MENU PRINCIPAL =====")
    opc = input(f"Ingrese una opcion\n\
1. Gestion de clientes\n2. Gestionar Pedidos\n3. Informes de ventas\n4. Clasificacion de clientes\n5. Salir\n")
    match opc:
        case "1":
            while True:
                os.system("cls")
                print("===== MENU DE CLIENTES =====")
                print("     Ingrese una opcion")
                opc1 = input(f"\n1. Registrar cliente\n2. Gestionar clientes\n3. Ver clientes registrados\n4. Salir\n")
                match opc1:
                    case "1":
                        documento = input("\nIngrese el documento de identidad del cliente\n")
                        if documento in clientes:
                            print("El cliente ya existe en nuestra base de datos")
                            input("Presione una tecla para continuar")
                        else:
                            nombre = input("\nIngrese el nombre y apellido del cliente:\n").lower()
                            correo = input("\nIngrese el correo del cliente\n").lower()
                            telefono = input("\nIngrese el numero telefonico del cliente\n")
                            direccion = input("\nIngrese la direccion del cliente:\n").lower()
                            ciudad = input("\nIngrese la ciudad del residencia\n").lower()
                            gesDirre[documento] = direccion
                            gesTel[documento] = telefono
                            gesCorreo[documento] = correo
                            gesCiudad[documento] = ciudad
                            gestion[documento] = nombre
                            clientes.append(documento)
                            input("Cliente agregado, Precione una tecla para continuar")

                    case "2":
                        while True:
                            os.system("cls")
                            print("===== GESTION DE CLIENTES =====")
                            documento = input("\nIngrese el documento del cliente a modificar:\n")
                            if documento not in clientes:
                                print("El cliente no existe")
                                input("Precione una tecla para continuar")
                                break
                            else:
                                while True:
                                    os.system("cls")
                                    print("===SUB MENU CLIENTES ===")
                                    print("Que deseas modificar del cliente")
                                    opc2 = input("1. Modificar la direccion\n2. Modificar el telefono\n3. Modificar el correo\n4. Modificar la ciudad\n5. Salir\n")
                                    match opc2:
                                        case "1":
                                            direc = input("\nIngrese la nueva direccion\n").lower()
                                            gesDirre[documento] = direc
                                            input("Direccion Modificada, Precione una tecla para continuar")
                                        case "2":
                                            tel = input("\nIngrese el nuevo telefono\n").lower()
                                            gesTel[documento] = tel
                                            input("Telefono Modificado, Precione una tecla para continuar")
                                        case "3":
                                            correoN = input("\nIngrese el nuevo correo\n").lower()
                                            gesCorreo[documento] = correoN
                                            input("Correo Modificado, Precione una tecla para continuar")
                                        case "4":
                                            ciudadN = input("\nIngrese la nueva ciudad\n").lower()
                                            gesCiudad[documento] = ciudadN
                                        case "5":
                                            break
                                        case _:
                                            input("Opcion no valida, presione una tecla para continuar") 
                    case "3":
                        if (len(clientes) == 0):
                            print("No hay clientes registrados aun")
                            input("Presione una tecla para continuar")
                        else:
                            print("==== CLIENTES REGISTRADOS ====")
                            for docc, nom in gestion.items():
                                print(f"\n**=** Nombre: {nom} Documento: {docc}")
                            input("Precione una tecla para continuar")
                    case "4":
                        break
                    case _:
                        input("Opcion no valida, Precione una tecla para continuar")    
                             
        case "2":
            while True:
                os.system("cls")
                print("==== MENU DE PEDIDOS ====")
                print("    ¿Que desea hacer?")
                opc3 = input(f"\n1. Ingresar un pedido\n2. Pedidos realizados\n3. Salir\n")
                match opc3:
                    case "1":
                        documento = input("\nIngrese el documento del cliente\n")
                        if documento not in clientes:
                            print("El cliente no existe, Porfavor registrelo")
                            input("Precione una tecla para continuar")
                            break
                        else:
                            pedido = input("\n*=* Ingrese el pedido\n").lower()
                            valor = float(input("\n*=* Ingrese el valor del pedido\n"))
                            venta[pedido] = valor
                            contVen += valor
                            cliPedido= (pedido,documento)
                            pedidos.append(cliPedido)
                            if documento in contClasi:
                                contClasi[documento] += 1
                                if contClasi.get(documento) > 1 and contClasi.get(documento) <= 5:
                                    clasificacion[documento] = "Basico"
                                elif contClasi.get(documento) > 5 and contClasi.get(documento) <=10:
                                    clasificacion[documento] = "Plata"
                                elif contClasi.get(documento) > 10 and contClasi.get(documento) <=15:
                                    clasificacion[documento] = "Oro"
                                elif contClasi.get(documento) > 15 and contClasi.get(documento) <=20:
                                    clasificacion[documento] = "Diamante"
                                elif contClasi.get(documento) > 20:
                                    clasificacion[documento] = "Premium"    
                            else:
                                contClasi[documento] = 1
                            input("Pedido registrado, Precione una tecla para continuar")
                    case "2":
                        print("==== Pedidos Realizados ====")
                        for pedido, documento in pedidos:
                            nombre = ""
                            direccion = ""
                            ciudad = ""
                            if documento in gestion:
                                nombre = gestion[documento]
                            if documento in gesDirre:
                                direccion = gesDirre[documento]
                            if documento in gesCiudad:
                                ciudad = gesCiudad[documento]
                                
                            print(f"Cliente: {nombre} pidio: {pedido}")
                            print(f"Para la dirección: {direccion} en la ciudad de: {ciudad}")
                            print("==============================\n")

                        input("Presione una tecla para continuar")
                    case "3":
                        break
                    case _:
                        input("Opcion no valida, Precione una tecla para continuar")
            vTotal += contVen
        case "3":
            if (len(pedidos) == 0):
                print("No hay ventas registradss")
                input("Ingrese una tecla para continuar")
            else:
                print("==== Informes de ventas del dia ====")
                print(f"\nTotal vendido en el dia --(${vTotal:,.2f} COP)--\n")
                input("Precione una tecla para continuar")
        case "4":
            if (len(clasificacion) == 0):  
                print("No existen clientes en ninguna clasificacion")
            print("==== Categoria de clientes ====")
            for docu, clas in clasificacion.items():
                for ced, nom in gestion.items():
                    if docu == ced:
                        print(f"El cliente {nom} es clasificacion {clas}")
            input("Precione una tecla para continuar")
        case "5":
            print("Hasta luego")
            input("presione una tecla para continuar")
            break
        case _: 
            input("Opcion no valida, precione una tecla")
            
            

                            
                        
                    
                    
                            
                            
                        
                            
                

