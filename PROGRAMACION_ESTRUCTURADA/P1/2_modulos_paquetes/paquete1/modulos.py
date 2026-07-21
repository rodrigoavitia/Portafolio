# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

import os

def solicitarDatos1():
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    print(f"Soy funcion 1: El nombre es: {nombre} y su telefono es: {tel}")

def solicitarDatos3(nombre,tel):
    nom=nombre
    telefono=tel
    print(f"Soy funcion 3: El nombre es: {nom} y su telefono es: {telefono}")

def solicitarDatos2():
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    return nombre,tel


def solicitarDatos4(nombre,tel):
    nom=nombre
    telefono=tel
    return nom,telefono

def borrarPantalla():
  os.system("clear")

def espereTecla():
  input("... Oprima una tecla para continuar ... ")

def saludar(nombre):
   nom=nombre
   return f"\t¡Hola, bienvenido: {nom}!\n"