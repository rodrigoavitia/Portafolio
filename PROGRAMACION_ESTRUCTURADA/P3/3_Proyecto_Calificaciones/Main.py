
import os
import Calificaciones

def main(): 
    opcion = True
    while opcion:
        Calificaciones.borrarPantalla()
        opcion = Calificaciones.menu_principal()

        match opcion:
            case "1":
                Calificaciones.agregar_calificacion()
                Calificaciones.esperarTecla()
            case "2":
                Calificaciones.mostrar_calificaciones()
                Calificaciones.esperarTecla()
            case "3":
                Calificaciones.calcular_promedio()
                Calificaciones.esperarTecla()
            case "4":
                print("\n\t\t\t\t🎉 Terminaste la ejecución del programa. Gracias por usarlo 🎉")
                Calificaciones.esperarTecla()
                Calificaciones.borrarPantalla()
                opcion = False
            case _:
                print("\n\t\t\t\t❌ Opción inválida, vuelva a intentarlo ❌\n")
                Calificaciones.esperarTecla()
                opcion = True

if __name__ == "__main__":
    main()
