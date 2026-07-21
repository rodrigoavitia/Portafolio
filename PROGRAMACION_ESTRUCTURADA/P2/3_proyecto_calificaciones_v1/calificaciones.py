def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("Presiona Enter para continuar...")

def menu_principal():
    print("\n\t\t\t📝 Sistema de Calificaciones 📝",
         "\n\t\t\t 1️⃣  Agregar Calificación",
         "\n\t\t\t 2️⃣  Mostrar Calificaciones,",
         " \n\t\t\t 3️⃣  Calcular Promedio",
         "\n\t\t\t 4️⃣  Salir")
    
    opcion = input("\n\t\t\t🟢  Selecciona una opción de 1-4: ")
    return opcion

def agregar_calificacion(lista):
    borrarPantalla()
    print("\n\t\t\t🆕 Agregar Calificaciónes 🆕")
    nombre = input("\n\t\t\tNombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        continua= True
        while continua:
            try:
                cal = float(input(f"Ingrese la calificación {i} de {nombre}: "))
                if cal >= 0 and cal <= 10:
                    calificaciones.append(cal)
                    continua = False
                else:
                    print("\n\t\t\tLa calificación debe estar entre 0 y 10.")
            except ValueError:
                print("\n\t\t\tEntrada inválida. Por favor, ingrese un valor número.")
    lista.append([nombre] + calificaciones)
    print("\n\t\t\tAccion realizada con exito")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("\n\t\t\t👁️ Mostrar Calificaciones 👁️")
    if len(lista) > 0:
        print(f" {'Nombre':<15}{'Calif. 1':<10}{'Calif. 2':<10}{'Calif. 3':<10}")
        print("-" * 90)
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:10}{fila[2]:10}{fila[3]:<10}")
            print("-" * 90)
        cuantos = len(lista)
        print(f"Son {cuantos} alumnos")
    else:
        print("\n\t\t\t No hay calificaciones registradas.")

def calcular_promedio(lista):
    borrarPantalla()
    print("\n\t\t\t📊Promedio de nuevos alumnos 📊")
    if len(lista) > 0:
        print(f"\n\t\t\t {'Nombre':<15}{'Promedio':<10}")
        print("-" * 90)
        promedio_grupal = 0
        for fila in lista:
            nombre = fila[0]
            promedio = sum(fila[1:]) / 3
            print(f"{nombre:<15}{promedio:<10.2f}")
            promedio_grupal += promedio
        print("-" * 90)
        promedio_grupal = promedio_grupal/ len(lista)
        print(f"\n\t\t\tPromedio grupal: {promedio_grupal:.2f}")
    else:
        print("\n\t\t\tNo hay calificaciones registradas.")