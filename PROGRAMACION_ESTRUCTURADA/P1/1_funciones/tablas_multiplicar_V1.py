'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Con funciones que regrese valor y utilice paremetros

'''
import os
os.system("cls")
#version 1
numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
multi=numero*1
print(f"{numero} x 1 = {multi}")
multi=numero*2
print(f"{numero} x 2 = {multi}")
multi=numero*3
print(f"{numero} x 3 = {multi}")
multi=numero*4
print(f"{numero} x 4 = {multi}")
multi=numero*5
print(f"{numero} x 5 = {multi}")
multi=numero*6
print(f"{numero} x 6 = {multi}")
multi=numero*7
print(f"{numero} x 7 = {multi}")
multi=numero*8
print(f"{numero} x 8 = {multi}")
multi=numero*9
print(f"{numero} x 9 = {multi}")
multi=numero*10
print(f"{numero} x 10 = {multi}")

#version 2
numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
for i in range(1,11):
  multi=numero*i
  print(f"{numero} x {i} = {multi}")

numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
i=1
while i<=10:
  multi=numero*i
  print(f"{numero} x {i} = {multi}") 
  i+=1   



#version 3

def tabla(numero):
   num=numero
   respuesta=""
   for i in range(1,11):
     multi=num*i
     respuesta+=f"\t{num} x {i} = {multi}\n"
   return respuesta  

numero=int(input("Dame el numero de la tabla de multiplicar a calcular: "))
print(f"Tabla de multiplicar del {numero}")
resultado=tabla(numero)
print(f"{resultado}")

