"""
List (Array)
Son colecciones o conjuntos de datos/valores bajo un mismo nombre para acceder 
a los valores se hace un indice numerico.

NOTA: Sus valores si son modificables

La lista es una colección ordenada y modificable. Permite
miembros duplicados.

"""

import os
os.system("cls")

#Funciones mas comunes en las listas

paises=["México","España","Brasil","Canada"]

numero=[23,45,8,24]

varios=["hola",3.1416,True]



#Imprimir el contenido de una lista

print(paises)

print(numero)

print(varios)


print("________________________")
#Recorrer la lista

#Primer forma
for i in paises:
    print(i)

print("________________________")

#Segunda forma
for i in range(0,len(paises)):
    print(paises[i])

print("________________________")
#Ordenar elementos de una lista

paises.sort()
print(paises)

numero.sort()
print(numero)

"""
varios.sort()  
print(varios)

:::NO ES POSIBLE POR QUE HAY DATOS COMBINADOS:::

"""

#dAR VUELTA A UNA LISTA
paises.reverse()
print(paises)
print("________________________")
numero.reverse()
print(numero)


print("________________________")
#AGREGAR, INSERTAR, AÑADIR UN ELEMENTO A UNA LISTA

#Primer forma
paises.append("Honduras")
print(paises)
print("________________________")
#Segunda forma
paises.insert(1,"Honduras")
print(paises)

print("________________________")
paises.sort()
print(paises)
print("________________________")
#Eliminar/Borrar un elemento de una lista
paises.pop(4)
print(paises)
print("________________________")
#Segunda forma
paises.remove("Honduras")
print(paises)
print("________________________")

#Buscar un elemento dentro de la lista
print(paises)
print("________________________")
ans="Brasil" in paises
print(ans)
print("________________________")

#CONTAR NUMERO DE VECES QUE APARECE UN ELEMENTO DENTRO DE UNA LISTA

print(numero)
print("________________________")

cuantos=numero.count(23)
print(cuantos) 

numero.append(23)
cuantos=numero.count(23)
print(cuantos)



#CONOCER LA POSICION/INDICE EN EL QUE SE ENCUENTRA UN ELEMENTO DE LA LISTA 
paises.reverse()
paises.append("Canada")
print(paises)


#TODAS LAS FUNCIONES VAN ACOMPAÑADAS DE PARENTESIS
pos=paises.index("Canada")
print(f"El valor de Canada esta en: {pos}")
cuantos=paises.count("Canada")
print (f"El pais se encontro en la lista: {cuantos} veces")



#UNIR EL CONTENIDO DE UNA LISTA DENTRO DE OTRA
print(numero)
numero2=[100,200]

print(numero2)

#CREAR A PARTIR DE LASS LISTAS 1 Y 2 UNA RESULTANTE Y MOSTRAR EL CONTENIDO DESCENDENTEMENTE
print("AGREGANDO LISTA 2")
numero.extend(numero2)
print(numero)

print("ORDENAR LA LISTA DE FORMA ASCENDENTE")
numero.sort()
print(numero)


print("ORDENAR LA LISTA DE FORMA DESCENDENTE")
numero.reverse()
print(numero)

