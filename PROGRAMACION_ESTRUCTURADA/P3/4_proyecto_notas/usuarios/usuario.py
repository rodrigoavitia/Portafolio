from conexionBD import *
import datetime
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre,apellidos,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        contrasena=hash_password(contrasena)
        cursor.execute("insert into usuarios (nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s)",(nombre,apellidos,email,contrasena,fecha))
        conexion.commit()
        return True
    except:
        return False
    
def inicio_sesion(email,contrasena):
    try:
       contrasena=hash_password(contrasena)
       cursor.execute("select * from usuarios where email=%s and password=%s",(email,contrasena)) 
       return cursor.fetchone()
    except:
        return []     
