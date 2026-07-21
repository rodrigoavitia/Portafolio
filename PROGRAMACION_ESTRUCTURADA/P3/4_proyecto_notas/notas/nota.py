
from conexionBD import *

def crear_nota(usuario_id,titulo,descripcion):
    try:
        cursor.execute("insert into notas (usuario_id,titulo,descripcion,fecha) values(%s,%s,%s,now())",(usuario_id,titulo,descripcion))
        conexion.commit()
        return True           
    except:
        return False
    
    
def mostrar(usuario_id):
    try:
        cursor.execute("select * from notas where usuario_id=%s",(usuario_id,))
        return cursor.fetchall()
    except:       
        return []
    
    
def cambiar(id,titulo,descripcion):
    try:
        cursor.execute("update notas set titulo=%s, descripcion=%s,fecha=now() where id=%s",(titulo,descripcion,id))
        conexion.commit()
        return True
    except:
        return False  
    
    
def borrar(id):
    try:
        cursor.execute("delete from notas where id=%s",(id,))
        conexion.commit()
        return True
    except:
        return False      
    
def buscar(id):
     try:
      cursor.execute("select * from notas where id=%s",(id,))
     except:
         return False