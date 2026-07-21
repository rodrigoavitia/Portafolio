import funciones
from notas import nota
from usuarios import usuario
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            # password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\tSe registro el usuario {nombre} {apellidos} correctamente")
            else:
                print(f"\n\t..No fue posible registrar el usuario en este momento, intentalo mas tarde ...")    
            funciones.esperarTecla()



            
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            lista_usuarios=usuario.inicio_sesion(email,password)
            if len(lista_usuarios)>0:
              menu_notas(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2])
            else:
              print(f"\n\tE-mail y/o contraseña incorrectas por favor verifique ....")
              funciones.esperarTecla()    

              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta=nota.crear_nota(usuario_id,titulo,descripcion)
            if respuesta:
                print(f"\n\tSe creo la nota {titulo} con exito")
            else:
                print(f"\n\t..No fue posible crear la nota, intenta mas tarde")    
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print(f"\n\tMostrar las notas")
                print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<15}{'Fecha':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
            else:
                print("\n\t ¡..No hay notas para este usuario")    
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print(f"\n\tMostrar las notas")
                print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<15}{'Fecha':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
                print(f"-"*80)
                resp=input("Deseas modificar alguna nota si/no").lower().strip()
                if resp=="si":
                    print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
                    id = input("\t \t ID de la nota a actualizar: ")
                    titulo = input("\t Nuevo título: ")
                    descripcion = input("\t Nueva descripción: ")
            #Agregar codigo
                    respuesta=nota.cambiar(id,titulo,descripcion)
                    if respuesta:
                        print(f"\n\tSe actualizó la nota {titulo} con exito")
                    else:
                        print(f"\n\t..No fue posible crear la nota, intenta mas tarde") 
                funciones.esperarTecla()                     
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print(f"\n\tMostrar las notas")
                print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<15}{'Fecha':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                     print(f"{fila[0]:<10}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
                     print(f"-"*80)
                     resp=input("Deseas eliminar alguna nota (si/no) ").lower().strip()
                     if resp=="si":
                         print(f"\n \t .:: {nombre} {apellidos}, vamos a eliminar una Nota ::. \n")
                         id = input("\t \t ID de la nota a eliminar: ")
                     if not id.isdigit():
                        print("\n\t El ID debe ser un número entero. Intenta de nuevo.")
                        funciones.esperarTecla()
                        continue
            #Agregar codigo 
                     respuesta=nota.borrar(id)
                     if respuesta:
                        print(f"\n\tSe borró la nota {id} con exito")
                     else:
                        print(f"\n\t..No fue posible eliminar la nota, intenta mas tarde")
                funciones.esperarTecla()           
        elif opcion == '5' or opcion=="BUSCAR":
            if len(lista_notas)>0:
                print(f"\n\tMostrar las notas")
                print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<15}{'Fecha':<15}")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
                print(f"-"*80)
                resp=input("Ingrese el ID de la nota a buscar").lower().strip()
            #Agregar codigo
                resp=nota.buscar(id,)
                if resp:
                    print(f"\n\tNota encontrada: {resp[2]} - {resp[3]}")
                else:
                    print("\n\tNo se encontró la nota con el ID proporcionado.")
                funciones.esperarTecla()                     
        elif opcion == '6' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


