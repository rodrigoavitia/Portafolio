"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("cls")

"""
paises={"México", "Brasil", "España", "Canada", "Canada"}
print(paises)

varios={True, "UTD", 33, 3.14}
print(varios)


#FUNCIONES U OPERACIONES
paises.add("Mexico")      #AGREGAR UN DATO
print(paises)

paises.pop()
print(paises) 

paises.remove("Mexico")
print (paises)
"""


ans="si"
email=[]
while ans=="si":
    email.append(input("Introduzca su email: "))
    ans=input("¿Desea agregar otro correo? (si/no) ")



email_set=set(email)
print(email_set)


email=list(email_set)
print(email)


