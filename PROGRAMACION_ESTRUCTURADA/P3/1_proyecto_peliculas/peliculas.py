import mysql.connector
from mysql.connector import Error

pelicula={}

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None

def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
   input("\n\t ... Oprima cualquier tecla para continuar ...")

def crearpeliculas():
    borrarpantalla()
    conexionbd=conectar()
    if conexionbd is not None:
        print("\n\t .:: Agregar Películas ::.\n")
        pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
        pelicula.update({"categoria":input("Ingresa la categoría: ").upper().strip()})
        pelicula.update({"clasificacion":input("Ingresa la clasificación: ").upper().strip()})
        pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
        pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
        ######## SQL a BD
        cursor=conexionbd.cursor()
        sql="insert into peliculas ( nombre, categoria, clasificacion, genero, idioma) values ( %s, %s, %s, %s, %s)"
        val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
        cursor.execute(sql,val)
        conexionbd.commit()
        print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")
    
def mostrarpeliculas():
    borrarpantalla()
    conexionbd=conectar()
    if conexionbd is not None:
      cursor=conexionbd.cursor()
      sql="select * from peliculas"
      cursor.execute(sql)
      registros=cursor.fetchall()
      print("\n\t .:: Mostrar Películas ::.\n")
      if registros:
        print(f"\n\tMostrar las Peliculas")
        print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
        print(f"-"*80)
        for fila in registros:
          print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print(f"-"*80)  
      else:
        print("\n\t .:: No hay peliculas en el Sistema ::. ")      

def buscarpeliculas():
    borrarpantalla()
    conexionbd=conectar()
    if conexionbd is not None:
      nombre=input("Dame el nombre de la pelicula a buscar: ").upper().strip()
      cursor=conexionbd.cursor()
      sql="select * from peliculas where nombre=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      registros=cursor.fetchall()
      if registros:
        print(f"\n\tMostrar las Peliculas")
        print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
        print(f"-"*80)
        for fila in registros:
          print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print(f"-"*80)  
      else:
        print("\n\t .:: No hay peliculas en el Sistema con ese nombre::. ")    

def borrarpeliculas():
    borrarpantalla()
    conexionbd=conectar()
    if conexionbd is not None:
      nombre=input("Dame el nombre de la pelicula a borrar: ").upper().strip()
      cursor=conexionbd.cursor()
      sql="select * from peliculas where nombre=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      registros=cursor.fetchall()
      if registros:
        print(f"\n\tMostrar las Peliculas")
        print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
        print(f"-"*80)
        for fila in registros:
          print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print(f"-"*80) 
        resp=input(f"¿Deseas borrar la pelicula {nombre}? (Si/No): " ).lower().strip()
        if resp=="si":
           sql="delete from peliculas where nombre=%s"
           val=(nombre,)
           cursor.execute(sql,val)
           conexionbd.commit()
           print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")
      else:
        print("\n\t .:: No hay peliculas en el Sistema con ese nombre::. ")    

def modificarpeliculas():
   borrarpantalla()
   conexionbd=conectar()
   if conexionbd is not None:
      nombre=input("Dame el nombre de la pelicula a modificar:").upper().strip()
      cursor=conexionbd.cursor()
      sql="select * from peliculas where nombre=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      registros=cursor.fetchall()
      if registros:
         print(f"\n\tMostrar las Peliculas")
         print(f"{'ID':<10}{'nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
         print(f"-"*80)
         for fila in registros:
             print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
         print(f"-" * 80)
         resp=input(f"Deseas modificar la pelicula {nombre}? [Si/No]: ").lower().strip()
         if resp == "si":
            nueva_categoria=input("Ingresa la nueva categoría: ").upper().strip()
            nueva_clasificacion=input("Ingresa la nueva clasificación: ").upper().strip()
            nuevo_genero=input("Ingresa el nuevo genero: ").upper().strip()
            nuevo_idioma=input("Ingresa el nuevo idioma: ").upper().strip()
            sql="update peliculas set categoria=%s, clasificacion=%s, genero=%s, idioma=%s where nombre=%s"
            val=(nueva_categoria, nueva_clasificacion, nuevo_genero, nuevo_idioma, nombre)
            cursor.execute(sql,val)
            conexionbd.commit()
            print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")
         elif resp == "no":
            print("\n\t .:: No se modificó la pelicula ::. ")
         else:
            print("\n\t .:: Respuesta no válida ::. ")
      else:
        print("\n\t .:: No hay peliculas en el Sistema con ese nombre::. ")