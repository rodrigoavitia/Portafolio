
import Agenda

def main():
    opcion = True

    while opcion:
        Agenda.borrarpantalla()
        print("\n\t\t\t .:::GESTIÓN DE CONTACTOS:::.")
        print("\t1.- Agregar contacto")
        print("\t2.- Mostrar todos los contactos")
        print("\t3.- Buscar contacto por nombre")
        print("\t4.- Modificar")
        print("\t5.- Eliminar")
        print("\t6.- SALIR")

        opcion = input("\n\t\t Elige una opción: ").strip()

        if opcion == "1":
            Agenda.agregarcontacto()
            Agenda.esperartecla()
        elif opcion == "2":
            Agenda.mostrarcontactos()
            Agenda.esperartecla()
        elif opcion == "3":
            Agenda.buscarcontacto()
            Agenda.esperartecla()
        elif opcion == "4":
            Agenda.modificarcontacto()
            Agenda.esperartecla()
        elif opcion == "5":
            Agenda.eliminarcontacto()
            Agenda.esperartecla()
        elif opcion == "6":
            print("\n\t\t\t .:::HASTA LUEGO:::.")
            Agenda.esperartecla()
            opcion = False
        else:
            print("\n\t\t\t .:::OPCIÓN INVÁLIDA:::.")
            Agenda.esperartecla()

if __name__ == "__main__":
    main()
