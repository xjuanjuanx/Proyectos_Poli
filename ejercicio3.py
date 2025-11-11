"""
Caso 3: Registro de Estudiantes en un Curso
Un curso de programación recibe estudiantes. Se requiere registrar sus nombres, edades y ciudad. Al final, mostrar los mayores de edad y contar cuántos son de cada ciudad.
Objetivos:
•	Leer y almacenar datos con tuplas o diccionarios.
•	Analizar datos por ciudad.
•	Filtrar por condición (mayoría de edad).
Retos:
•	Usar tuplas dentro de listas.
•	Hacer conteo de ciudades usando un diccionario.
Estructuras usadas: listas, tuplas, condicionales, ciclos, diccionarios

"""
import os
estudiantes = []
cantXCiudad = {}
edadM = []
ciudades = []
cont = {}

while True:
    os.system("cls")
    print("=== MENU PRINCIPAL ===")
    opc = int(input("1. Registrar alumno\n2. Ver listado de alumnos\n3. Ver filtro por edad\n4. Ver cantidades por ciudad\n5. SALIR\n"))
    match opc:
        case 1:
            nombre = input("\nIngrese el nombre del alumno (Nombre y Apellido)\n").strip().lower()
            edad = int(input("Ingrese edad del estudiante\n"))
            ciudad = input("Ingrese ciudad donde vive el estudiante:\n").strip().lower()
            
            estudiante = (nombre,edad,ciudad)
            estudiantes.append(estudiante)
            if ciudad in cantXCiudad:
                cantXCiudad[ciudad] +=1
            else:
                cantXCiudad[ciudad] = 1
            if edad > 18:
                alumno = (nombre,edad)
                edadM.append(alumno)
            input("Alumno registrado, Precione una tecla para continuar")
        case 2:
            if (len(estudiantes) == 0):
                print("Aun no hay estudiantes registrados")
                input("Precione una tecla para continuar")
            else:
                print("\n=== DATOS REGISTRADOS ===")
                for datos in estudiantes:
                    print(f"Nombre: {datos[0]}, Edad: {datos[1]}, Ciudad: {datos[2]}")
                input("Precione una tecla para continuar")
        case 3:
            if (len(estudiantes) == 0):
                print("Aun no hay estudiantes registrados")
                input("Precione una tecla para continuar")
            else:
                for item in edadM:
                    print(f"El estudiante {item[0]} tiene {item[1]} años de edad, Por lo tanto es mayor de edad")
                input("Precione una tecla para continuar")
        case 4:
            if (len(estudiantes) == 0):
                print("Aun no hay estudiantes registrados")
                input("Precione una tecla para continuar")
            else:
                for city,cantidad in cantXCiudad.items():
                    print(f"De la ciudad {city} hay registrados {cantidad} de estudiantes")
                input("Precione una tecla para continuar")
        case 5:
            break
        case _:
            print("Opcion no valida")
            input("Precione una tecla para continuar")
