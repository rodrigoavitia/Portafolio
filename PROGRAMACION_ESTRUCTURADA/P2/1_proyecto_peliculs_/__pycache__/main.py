"""

Crear un proyecto que permita gestionar peliculas, colocar
un menu de opciones: agregar, borrar, modificar, buscar, limpiar 
una lista de peliculas

1- Utilizar funciones y mandar llamar desde otro archivo(modulo)
2- Utilizar diccionarios para almacenar los atributos (nombre, categoria, clasificacion, genero e idioma) de peliculas.
"""


import peliculas

opcion=True


while opcion:
    peliculas.borrarPantalla()
    print("\n\t ..:::GESTION DE PELICULAS:::.. \n\n\t 1.- Crear \n\t 2.- Borrar \n\t 3.- Mostrar \n\t 4.- Buscar \n\t 5.- Modificar \n\t 6.- Salir ")

    opcion=input("\n\n\t Elige una opcion: ").upper()

    match opcion:
        case "1":
            peliculas.CrearPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case "4":
            peliculas.buscarrCaract()
            peliculas.espereTecla()
        case "5":
            peliculas.modificarPeliculas()
            peliculas.espereTecla()
        case "6":
            print("\n\t\t..:::SALIENDO:::.. \n")
            peliculas.borrarPantalla()
            opcion=False
        case _:
            print("\n\t\t..:::OPCION NO VALIDA:::.. \n")
            peliculas.espereTecla()
            peliculas.borrarPantalla()
            opcion=True
            continue