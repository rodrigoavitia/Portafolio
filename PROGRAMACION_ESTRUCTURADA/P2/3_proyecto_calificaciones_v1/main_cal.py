import os
os.system('cls')

#NOTAS:
#1.- Utilizar funciones y mandar llamar desde otro archivo(modulos)
#2.- Utilizar list (bidimencional) para almacenar el nombre del alumno, asi como sus tres calificaciones


import calificaciones

datos = []

def main(): 
    
    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()    
        match opcion:
            case "1":
                calificaciones.agregar_calificacion(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedio(datos)
                calificaciones.esperarTecla()
            case "4":
                opcion=False
                print("\n\t ↩️ Terminaste la ejecucion del programa gracias por usarlo ↩️")
                calificaciones.borrarPantalla()
            case _:
                print("\n\t ❌ Opcion no valida, por favor selecciona una opcion del menu ❌")
                calificaciones.esperarTecla()
                opcion=True

if __name__ == "__main__":
    main()