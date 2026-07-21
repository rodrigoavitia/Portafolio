"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero
  en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("cls")

paises=["Mexico", "Brasil", "Canada", "España"]


pais1={
    "nombre": "Mexico",
    "capital": "CDMX",
    "Poblacio": 12000000,
    "idioma":"Español",
    "status":True
    }

pais2={
    "nombre": "Brasil",
    "capital": "Brasilia",
    "Poblacio": 14000000,
    "idioma": "Portugues",
    "status":True
    }

pais2={
    "nombre": "Canada",
    "capital": "Otawua",
    "Poblacio": 10000000,
    "idioma": "Frances, Ingles",
    "status":True
    }

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print (pais1)

for i in pais1:
    print(f"{i}={pais1[i]}")


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#Agregar un dato mas

pais1["Altitud"]=3000
for i in pais1:
    print(f"{i}={pais1[i]}")


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#Modificar valor que ya existe

pais1.update({"Altitud":2500})
for i in pais1:
    print(f"{i}={pais1[i]}")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#QUITAR DATO 

pais1.pop("Altitud")
for i in pais1:
    print(f"{i}={pais1[i]}")

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#QUITAR EL ULTIMO DATO QUE SE INTRODUJO

pais1.popitem()
for i in pais1:
    print(f"{i}={pais1[i]}")

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

