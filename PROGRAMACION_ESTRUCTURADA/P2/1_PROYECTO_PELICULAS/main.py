"""

Crear un proyecto que permita gestionar peliculas, colocar
un menu de opciones: agregar, borrar, modificar, buscar, limpiar 
una lista de peliculas

1- Utilizar funciones y mandar llamar desde otro archivo(modulo)
2- Utilizar listas para almacenar los nombre de peliculas
"""


import peliculas

opcion=True


while opcion:
    peliculas.borrarPantalla()
    print("\n\t ..:::GESTION DE PELICULAS:::.. \n\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir ")

    opcion=input("\n\n\t Elige una opcion: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.espereTecla()
        case "4":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
        case "6":
            peliculas.limpiarPeliculas()
            peliculas.espereTecla()
        case "7":
            print("\n\t\t..:::SALIENDO:::.. \n")
            peliculas.borrarPantalla()
            opcion=False
        case _:
            print("\n\t\t..:::OPCION NO VALIDA:::.. \n")
            peliculas.espereTecla()
            peliculas.borrarPantalla()
            opcion=True
            continue