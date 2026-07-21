import os
import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperarTecla():
    input(" ...Oprima cualquier tecla para continuar... ")

def menu_principal():
    print(" .::: SISTEMA DE CALIFICACIONES :::.\n")
    print("  1  ➔  Agregar")
    print("  2  ➔  Mostrar")
    print("  3  ➔  Calcular Promedio")
    print("  4  ➔  Salir\n")
    opcion = input(" Selecciona una opción de 1-4: ").strip()
    return opcion

def agregar_calificacion():
    borrarPantalla()
    print(" .::AGREGAR CALIFICACIONES::. \n")
    nombre = input(" Nombre del alumno: ").upper().strip()
    calificaciones = []
  
    for i in range(1, 4):
        while True:
            try:
                cal = float(input(f" Calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    break
                else:
                    print(" Ingrese un número válido entre 0 y 10 \n")
            except ValueError:
                print(" Ingrese un valor numérico \n")

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO calificaciones (nombre, cal1, cal2, cal3) VALUES (%s, %s, %s, %s)", 
                           (nombre, calificaciones[0], calificaciones[1], calificaciones[2]))              
            conexion.commit()
            print(" Acción realizada con éxito \n")
        except Error as e:
            print(f" Error al guardar: {e}")
        finally:
            cursor.close()
            conexion.close()

def mostrar_calificaciones():
    ancho = 115
    borrarPantalla()
    print(" .::MOSTRAR CALIFICACIONES::. \n")
    conexion = conectar()

    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM calificaciones")
        registros = cursor.fetchall()
        if registros:
            print(f"{'::Nombre::':<15}{'::Calif1::':<12}{'Calif2::':<12}{'::Calif3::':<12}")
            print(("-" * 60).center(ancho))
            for fila in registros:
                print(f"{fila[0]:<15}{fila[1]:<12}{fila[2]:<12}{fila[3]:<12}")
            print(("-" * 60).center(ancho))
            print(f"\n Son {len(registros)} alumnos\n")
        else:
            print(" No hay calificaciones registradas.\n")
        cursor.close()
        conexion.close()

def calcular_promedio():
    borrarPantalla()
    ancho = 90

    print(" .::PROMEDIO DE ALUMNOS::. \n")
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM calificaciones") 
        registros = cursor.fetchall()
        if registros:
            print(f"{'::Nombre::':<15}{'::Promedio::':<12}")
            print(("-" * 32).center(ancho))
            promedio_grupal = 0
            for fila in registros:
                promedio = (fila[1] + fila[2] + fila[3]) / 3
                print(f"{fila[0]:<15}{promedio:<12.2f}")
                promedio_grupal += promedio
            promedio_grupal /= len(registros)
            print(("-" * 32).center(ancho))
            print(f"\nEl promedio General: {promedio_grupal:.2f}\n")
        else:
            print(" No hay calificaciones registradas.\n")
        cursor.close()
        conexion.close()