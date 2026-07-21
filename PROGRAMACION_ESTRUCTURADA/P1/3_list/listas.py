import os

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
os.system("cls")

numeros=[23,34]

print(numeros)

lista="["
for i in numeros:
  lista+=f"{i},"
print(f"{lista}]")

lista="["
for i in range(0,len(numeros)):
  lista+=f"{numeros[i]},"
print(f"{lista}]")

lista="["
i=0
while i<len(numeros):
  lista+=f"{numeros[i]},"
  i+=1
print(f"{lista}]")


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

os.system("cls")
palabras=["hola","2023","Lebroncito","UTD","True","UTD"]
print(palabras)
palabra_buscar=input("Dame la palabra a buscar: ")

 #1ER FORMA
if palabra_buscar in palabras:
  print("SI se encontro la palabra en la lista")
else:
  print("NO se encontro la palabra en la lista")  


#2DA FORMA
palabras=["hola","2023","Lebroncito","UTD","True","UTD"]
encontro=False
for i in palabras:
  if i==palabra_buscar:
    encontro=True 
if encontro:
  print("SI se encontro la palabra en la lista")
else:
  print("NO se encontro la palabra en la lista")   

#3er FORMA
palabras=["hola","2023","Lebroncito","UTD","True","UTD"]
encontro=False
for i in range(0,len(palabras)):
  if palabras[i]==palabra_buscar:
    encontro=True 
    
if encontro:
  print("SI se encontro la palabra en la lista")
else:
     print("NO se encontro la palabra en la lista")  

#Ejemplo 3 Añadir elementos a la lista
os.system("cls")
numeros=[]

opc="si"
while opc=="si":
  numeros.append(float(input("Dame un numero entero o decimal: ")))
  opc=input("¿Desear agregar otro numero a las lista (si/no)? ").lower()
  print(numeros)   




#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
os.system("cls")
agenda=[
        ["Carlos","6181234567"],
        ["Alberto","6671234567"],
        ["Martin","6785678923"]
       ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])    

cadena=""
for r in range(0,3):
    for c in range(0,2):
      cadena+=f"{agenda[r][c]}, "
    cadena+="\n"     
print(cadena) 