import mysql.connector
from mysql.connector import Error

peliculas=[]

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

pelicula={}

def CrearPeliculas():
    borrarPantalla()
    ConexionBD = Conectar()
    if ConexionBD !=None:
        print ("\n\t\t\t\t ..:::CREAR PELICULA:::.. \n")
        pelicula.update({
            "nombre": input("Ingrese el nombre de la pelicula: "),
            "categoria": input("Ingrese la categoria de la pelicula: "),
            "clasificacion": input("Ingrese la clasificacion de la pelicula: "),
            "genero": input("Ingrese el genero de la pelicula: "),
            "idioma": input("Ingrese el idioma de la pelicula: ")
        })
        cursor = ConexionBD.cursor()
        sql = "insert into peliculas (nombre, categoria, clasificacion, genero, idioma) values (%s, %s, %s, %s, %s)" 
        val = (pelicula ["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"])
        cursor.execute(sql, val)
        ConexionBD.commit()
        print(f"\n\t\t La pelicula se ha creado con exito!!!")
                   
def mostrarPeliculas():
    borrarPantalla()
    print("\n\t\t\t\t ..:::MOSTRAR PELICULAS:::.. \n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i} : {pelicula[i]}")
    else:
        print("\n\t\t No hay peliculas para mostrar en el sistema...")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t\t\t\t ..:::BORRAR PELICULA:::.. \n")
    if len(pelicula) > 0:
        input("¿Que pelicula desea borrar?")
        pelicula.clear()
        print("\n\t\t La operación se realizo con exito...")
    else:
        print("\n\t\t No hay peliculas para borrar en el sistema...")

def espereTecla():
        input("\n\t Presione una tecla para continuar...")

def Conectar():
    try:
        Conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )        
        return Conexion
    except Error as e:
        print(F"El error que se presenta es {e}")
        return None
    




def modificarPeliculas():
    borrarPantalla()
    ConexionBD = Conectar()
    if ConexionBD != None:
        print("\n\t\t\t\t ..:::MODIFICAR PELICULA:::.. \n")
        if len(pelicula) > 0:
            nombre = input("Ingrese el nombre de la pelicula a modificar: ")
            if nombre in pelicula.values():
                pelicula.update({
                    "nombre": input("Ingrese el nuevo nombre de la pelicula: "),
                    "categoria": input("Ingrese la nueva categoria de la pelicula: "),
                    "clasificacion": input("Ingrese la nueva clasificacion de la pelicula: "),
                    "genero": input("Ingrese el nuevo genero de la pelicula: "),
                    "idioma": input("Ingrese el nuevo idioma de la pelicula: ")
                })
                cursor = ConexionBD.cursor()
                sql = "UPDATE peliculas SET nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s WHERE nombre=%s"
                val = (pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"], nombre)
                cursor.execute(sql, val)
                ConexionBD.commit()
                print("\n\t\t La pelicula se ha modificado con exito!!!")
            else:
                print("\n\t\t La pelicula no existe en el sistema...")
        else:
            print("\n\t\t No hay peliculas para modificar en el sistema...")
