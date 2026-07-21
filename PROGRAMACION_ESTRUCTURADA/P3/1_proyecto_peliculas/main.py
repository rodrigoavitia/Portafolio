import peliculas

opcion=True

while opcion:
   peliculas.borrarpantalla()
   print("\n\t\t\t .::: GESTION DE PELICULAS :::. \n\n\t 1.- Crear \n\t 2.- Borrar \n\t 3.- Mostrar \n\t 4.- Buscar \n\t 5.- Modificar \n\t 6.- Salir")
   opcion=input("\n\t\t Elige una opción: ").upper()

   match opcion:
      case "1":
         peliculas.crearpeliculas()
         peliculas.esperartecla()
      case "2":
         peliculas.borrarpeliculas()
         peliculas.esperartecla()
      case "3":
         peliculas.mostrarpeliculas()
         peliculas.esperartecla()
      case "4":
         peliculas.buscarpeliculas()
         peliculas.esperartecla()
      case "5":
         peliculas.modificarpeliculas()
         peliculas.esperartecla()
      case "6":
         opcion=False
         peliculas.borrarpantalla()
         print("\n\tTerminaste la ejecución del Sistema ... Gracias ...")
      case _:
         opcion=True
         peliculas.esperartecla()
         print("\n\tOpción Invalida vuelva a intentarlo")   

                        

