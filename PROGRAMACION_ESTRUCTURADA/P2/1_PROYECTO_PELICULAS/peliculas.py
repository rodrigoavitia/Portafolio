peliculas=[]

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def espereTecla():
        input("\n\t Presione una tecla para continuar...")

def agregarPeliculas():
    borrarPantalla()
    pelicula = input("\n\t\t\t\t ..:::AGREGAR PELICULA:::.. \n\n\t Ingrese el nombre de la pelicula: ")
    peliculas.append(pelicula.upper().strip())
    print(f"\n\t Pelicula '{pelicula}' agregada exitosamente.")
    print(F"\n\t Buen dia :)")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t\t\t\t ..:::MOSTRAR PELICULAS:::.. \n")
    for i in range(len(peliculas)):
        print(f"{i+1} : {peliculas[i]}")
    else:
        print("\n\t No hay peliculas en el sistema.")

def borrarPeliculas():
    pelicula = input("\n\t\t\t\t ..:::BORRAR PELICULA:::.. \n\n\t Ingrese el nombre de la pelicula a borrar: ")
    pelicula = pelicula.upper().strip()
    respuesta= "SI"
    if respuesta == "SI":
        encontro=0
        input(f"\n\t ¿Esta seguro de borrar la pelicula '{pelicula}'? (Si/No): ").lower().strip()
        if pelicula in peliculas:
            peliculas.remove(pelicula)
        print(f"\n\t Pelicula '{pelicula}' borrada exitosamente.")
        encontro+=1
        print(f"se eliminaron {encontro} veces")
    else:
        print(f"\n\t La pelicula '{pelicula}' no se encuentra en la lista.")



def limpiarPeliculas():
    borrarPantalla()
    print("\n\t ..::BORRAR TOODAS LAS PELICULAS::..")
    resp = input("¿Esta seguro de borrar TODAS las peliculas?(Si/No): ").lower().strip()
    if resp == "Si":
        peliculas.clear()
        print("\n\t\t La operación se realizo con exito...")


def buscarPeliculas():
    borrarPantalla()
    print("\n\t .::Buscar Peliculas::." )
    peliculas_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    if not(peliculas_buscar in peliculas):
        print("#### La pelicula que ingreso no esta en el sistema #####")
    else:
        encontro=0
        for i in range(0,len(peliculas)):
            if peliculas_buscar==peliculas[i]:
                print (f"\n\t La pelicula {peliculas_buscar} se encontro en el casillero: {i+1} ")
                encontro+=1
                print(f"\n #### Tenemos {encontro} pelicula(s) con este titulo #####")
            

def modificarPeliculas():
    borrarPantalla()
    print("\n\t .:: MODIFICAR PELICULAS ::.")
    pelicula_buscar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print("\n\t\t No se encuentra la pelicula en el sistema...")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                resp=input("¿Deseas actualizar la pelicula? (SI/NO): ").lower().strip()
                if resp=="si":
                    peliculas[i]=input("\n Introduzca el nuevo nombre de la pelicula: ").upper().strip()
                    encontro+=1
                    print("\n\t\t Se realizo con exito la operacion ")
        print(f"\n Se modifico {encontro} pelicula(s) con este titulo...")  
