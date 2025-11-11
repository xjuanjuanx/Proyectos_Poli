
import os
votoMa = 0
votoMe = 999999
votDes1 = votDes2  = 0
voto1 =voto2 =voto3 = voto4 = 0
estudiantes = []
cantVotos = {}
votDesempate = {}
cont = 0
desempate =[]
while True:
    os.system("cls")
    print("=== SISTEMA DE VOTACIONES ===")

    opc = int(input("1. Votar\n2. Ver Cantidad de votos\n3. Ver ganador o empate\n4. Salir\n"))
    match opc:
        case 1:
            nombre = input("\nIngrese su nombre para iniciar la votacion:\n")
            if nombre in estudiantes:
                print("\nUsted ya voto, No puede volver a votar")
                input("Precione una tecla para continuar")
            else:
                estudiantes.append(nombre)
                print("\n==== CANDIDATOS ====")
                print(f"{nombre} ¿Por cual candidato desea votar?:\n")
                opc2 = input("1. Juan Velez\n2. Sebastian Correa\n3. Laura Carolina\n4. Voto en Blanco\n").strip().lower()
                match opc2:
                    case "1":
                        voto1 += 1
                        print(f"\n{nombre} Gracias por votas")
                        input("Precione una tecla para continuar")
                        cantVotos["Juan Velez"] = voto1
                    case "2":
                        voto2 += 1
                        print(f"\n{nombre} Gracias por votas")
                        input("Precione una tecla para continuar")
                        cantVotos["Sebastian Correa"] = voto2
                    case "3":
                        voto3 += 1
                        print(f"\n{nombre} Gracias por votas")
                        input("Precione una tecla para continuar")
                        cantVotos["Laura Carolina"] = voto3
                    case "4":
                        voto4 += 1
                        print(f"\n{nombre} Gracias por votas")
                        input("Precione una tecla para continuar")
                        cantVotos["Voto en Blanco"] = voto4
                    case _:
                        input("Opcion no valida, Precione una tecla para continuar")
                cont +=1
        case 2:
            print("\n====== Cantidad de votos =======\n")
            for nombre, votos in cantVotos.items():
                print(f"{cont}. {nombre} tiene un total de {votos} votos") 
            input("Precione una tecla para continuar")
        case 3:
            if voto1 > voto2 and voto1 > voto3 and voto1 > voto4:
                print(f"El ganador de las elecciones es Juan velez con una cantidad de votos de {cantVotos.get("Juan Velez")}")
                input("Precione una tecla para continuar")
            elif voto2 > voto1 and voto2 > voto3 and voto3 > voto4:
                print(f"El ganador de las elecciones es Sebastian Correa con una cantidad de votos de {cantVotos.get("Sebastian Correa")}")
                input("Precione una tecla para continuar")
            elif voto3 > voto1 and voto3 > voto2 and voto3 > voto4:
                print(f"El ganador de las elecciones es Laura Carolina con una cantidad de votos de {cantVotos.get("Laura Carolina")}")
                input("Precione una tecla para continuar")
            elif voto4 > voto1 and voto4 > voto2 and voto4 > voto3:
                print(f"Gana el voto en blanco por una cantidad de votos de {cantVotos.get("Voto en Blanco")}")
                input("Precione una tecla para continuar")
            elif voto1 == voto2 or voto2 == voto1:
                print("Hay un empate entre los candidatos Juan Velez y Sebastian Correa")
                print(f"Votos de Juan {cantVotos.get("Juan Velez")}")
                print(f"Votos de Sebastian {cantVotos.get("Sebastian Correa")}")
                input("Precione una tecla para continuar")
                while True:
                    os.system("cls")
                    print("===== Desempate ====")
                    opc3 = int(input(f"1. Votar para desempate\n2. Ver resultados\n3. salir\n"))
                    match opc3:
                        case 1:
                            nombre = input("Ingrese su nombre para inicial la votacion por el desempate").strip().lower()
                            if nombre in desempate:
                                print(f"{nombre}Usted ya voto, No puede volver a votar")
                                input("Precione una tecla para continuar")
                            else:
                                desempate.append(nombre)
                                print(f"{nombre} ¿Por cual candidato desea votar?\n")
                                opc4 = input(f"\n1. Juan Velez\n2 Sebastian Correa\n")
                                match opc4:
                                    case "1":
                                        votDes1 += 1
                                        print(f"{nombre} Gracias por votar")
                                        input("Precione una tecla para continuar")
                                        votDesempate["Juan Velez"] = votDes1
                                    case "2":
                                        votDes2 += 1
                                        print(f"{nombre} Gracias por votar")
                                        input("Precione una tecla para continuar")
                                        votDesempate["Sebastian Correa"] = votDes2
                        case 2:
                            if voto1 > voto2:
                                print(f"El ganador de las elecciones es Juan velez con una cantidad de votos de {votDesempate.get("Juan Velez")}")
                                input("Precione una tecla para continuar")
                            else:
                                print(f"El ganador de las elecciones es Sebastian Correa con una cantidad de votos de {votDesempate.get("Sebastian Correa")}")
                                input("Precione una tecla para continuar")
                        case 3:
                            break
                        case _:
                            input("Opcion no valida, Preciona una tecla para continuar")
            elif voto1 == voto3 or voto3 == voto1:
                print("Hay un empate entre los candidatos Juan Velez y Laura Carolina")
                print(f"Votos de Juan {cantVotos.get("Juan Velez")}")
                print(f"Votos de Laura {cantVotos.get("Laura Carolina")}")
                input("Precione una tecla para continuar")
                while True:
                    os.system("cls")
                    print("===== Desempate ====")
                    opc5 = int(input(f"1. Votar para desempate\n2. Ver resultados\n3. salir\n"))
                    match opc5:
                        case 1:
                            nombre = input("Ingrese su nombre para inicial la votacion por el desempate").strip().lower()
                            if nombre in desempate:
                                print(f"{nombre}Usted ya voto, No puede volver a votar")
                                input("Precione una tecla para continuar")
                            else:
                                desempate.append(nombre)
                                print(f"{nombre} ¿Por cual candidato desea votar?\n")
                                opc6 = input(f"\n1. Juan Velez\n2 Laura Carolina\n")
                                match opc6:
                                    case "1":
                                        votDes1 += 1
                                        print(f"{nombre} Gracias por votar")
                                        input("Precione una tecla para continuar")
                                        votDesempate["Juan Velez"] = votDes1
                                    case "2":
                                        votDes2 += 1
                                        print(f"{nombre} Gracias por votar")
                                        input("Precione una tecla para continuar")
                                        votDesempate["Laura Carolina"] = votDes2
                        case 2:
                            if voto1 > voto2:
                                print(f"El ganador de las elecciones es Juan velez con una cantidad de votos de {votDesempate.get("Juan Velez")}")
                                input("Precione una tecla para continuar")
                            else:
                                print(f"El ganador de las elecciones es Laura Carolina con una cantidad de votos de {votDesempate.get("Laura Carolina")}")
                                input("Precione una tecla para continuar")
                        case 3:
                            break
                        case _:
                            input("Opcion no valida, Preciona una tecla para continuar")
                
            elif voto2 == voto3 or voto3 == voto2:
                print("Hay un empate entre los candidatos Sebastian Correa y Laura Carolina")
                print(f"Votos de Sebastian {cantVotos.get("Sebastian Correa")}")
                print(f"Votos de Carolina {cantVotos.get("Laura Carolina")}")
                input("Precione una tecla para continuar")
                while True:
                    os.system("cls")
                    print("===== Desempate ====")
                    opc3 = int(input(f"1. Votar para desempate\n2. Ver resultados\n3. salir\n"))
                    match opc3:
                        case 1:
                            nombre = input("Ingrese su nombre para inicial la votacion por el desempate").strip().lower()
                            if nombre in desempate:
                                print(f"{nombre}Usted ya voto, No puede volver a votar")
                                input("Precione una tecla para continuar")
                            else:
                                desempate.append(nombre)
                                print(f"{nombre} ¿Por cual candidato desea votar?\n")
                                opc4 = input(f"\n1. Sebastian Correa\n2 Laura Carolina\n")
                                match opc4:
                                    case "1":
                                        votDes1 += 1
                                        print(f"{nombre} Gracias por votar")
                                        input("Precione una tecla para continuar")
                                        votDesempate["Sebastian Correa"] = votDes1
                                    case "2":
                                        votDes2 += 1
                                        print(f"{nombre} Gracias por votar")
                                        input("Precione una tecla para continuar")
                                        votDesempate["Laura Carolina"] = votDes2
                        case 2:
                            if voto1 > voto2:
                                print(f"El ganador de las elecciones es Sebastian Correa con una cantidad de votos de {votDesempate.get("Sebastian Correa")}")
                                input("Precione una tecla para continuar")
                            else:
                                print(f"El ganador de las elecciones es Laura Carolina con una cantidad de votos de {votDesempate.get("Laura Carolina")}")
                                input("Precione una tecla para continuar")
                        case 3:
                            break
                        case _:
                            input("Opcion no valida, Preciona una tecla para continuar")
            
        case 4:
            break 
        case _:
            print("Opcion no valida")

            input("Precione una tecla para continuar")   
