import random
import statistics
import csv

#lista de empleados 
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []

#funcion para asignar sueldos aleatorios
def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for i in range(len(trabajadores))]
    print("Sueldos asignados correctamente.")

#funcion para ver las estadisticas
def ver_estadisticas(): 
    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio = statistics.mean(sueldos)
    print(f"Sueldo más alto: ${max_sueldo}")
    print(f"Sueldo más bajo: ${min_sueldo}")
    print(f"Promedio de sueldos: ${promedio}")

#funcion para generar reportes de sueldo
def reporte_sueldos():
    reporte = []
    for i in range(len(trabajadores)):
        reporte.append([trabajadores[i], sueldos[i]])

    print("Nombre empleado | Sueldo base")
    for empleado in reporte:
        print(f"{empleado[0]} | ${empleado[1]}")
    
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo base"])
        writer.writerows(reporte)

    print("Reporte guardado en 'reporte_sueldos.csv'")

#funcion para hacer el menu
def menu():
    while True:
        print("-----Menú-----\n")
        print("1. Asignar sueldos aleatorios.")
        print("2. Ver estadisticas")
        print("3. Reporte de sueldos")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            asignar_sueldos()
        elif opcion == '2':
            ver_estadisticas()
        elif opcion == '3':
            reporte_sueldos()
        elif opcion == '4':
            print("Finalizando el programa... \n Desarrollado por Ismael Oyarzun\n RUT: 19.070.702-4")
            break
        else:
            print("Opcion no válida. Intente de nuevo")
        
menu()