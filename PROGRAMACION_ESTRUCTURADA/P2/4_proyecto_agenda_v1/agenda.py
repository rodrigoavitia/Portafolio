def borrarPantalla():
    import os
    os.system('cls')

def esperar_Tecla():
    input("\n\t\t\t\t\t👉 Oprima cualquier tecla para continuar...")

def menu_principal():
    borrarPantalla()
    print("\t\t\t\t 📝.::: Sistema de Gestión de Agenda de Contactos :::. 📝\n")
    print("\t\t\t\t\t 1️⃣  Agregar contacto")
    print("\t\t\t\t\t 2️⃣  Mostrar todos los contactos")
    print("\t\t\t\t\t 3️⃣  Buscar contacto por nombre")
    print("\t\t\t\t\t 4️⃣  Modificar contacto")
    print("\t\t\t\t\t 5️⃣  Eliminar contacto")
    print("\t\t\t\t\t 6️⃣  Salir del programa")
    opcion = input("\n\t\t\t\t\t👉 Elige una opción de (1-4): ")
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t\t\t\t📝 Agregar Contacto")
    nombre = input("\t\t\t\t\t👉 Nombre del contacto: ").upper().strip()
    if nombre in agenda:
        print("\n\t\t\t\t\t❌ El contacto ya existe.")
    else:
        telefono = input("\t\t\t\t\t👉 Teléfono del contacto: ").upper().strip()
        email = input("\t\t\t\t\t👉 Correo electrónico del contacto: ").lower().strip()
        agenda[nombre] =[telefono, email]
        print("\n\t\t\t\t\t✅ Accion realizada con éxito.")

def mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t\t\t\t📂 Mostrar Contactos")
    if not agenda:
        print("\n\t\t\t\t\t❌ No hay contactos en la agenda.")
    else:
        print(f"\n\t\t\t\t\t{'Nombre':<15} {'Teléfono':<15} {'Correo':<10}")
        print(f"-"*60)
        for nombre,datos in agenda.items():
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<10}")
        print(f"-"*60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t\t\t\t🔍 Buscar Contacto")
    if not agenda:
        print("\n\t\t\t\t\t❌ No hay contactos en la agenda.")
    else:
        nombre = input("\t\t\t\t\t👉 Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15} {'Teléfono':<15} {'Correo':<10}")
            print(f"-"*50)
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<10}")
            print(f"-"*50)
            print("\n\t\t\t\t\t✅ Contacto encontrado.")
        else:
            print("\n\t\t\t\t\t❌ El contacto no existe.")

def modificar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t\t\t\t✏️ Modificar Contacto")
    if not agenda:
        print("\n\t\t\t\t\t❌ No hay contactos en la agenda.")
    else:
        nombre = input("\t\t\t\t\t👉 Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print("Valores actuales:")
            print(f"Nombre: {nombre}\n Telefono: {agenda[nombre][0]}\n E-mail: {agenda[nombre][1]}")
            respuesta = input("\t\t\t\t\t👉 ¿Desea modificar el contacto? (Si/No): ").lower().strip()
            if respuesta == "si":
                telefono = input("\t\t\t\t\t👉 Nuevo teléfono del contacto: ").upper().strip()
                email = input("\t\t\t\t\t👉 Nuevo correo electrónico del contacto: ").lower().strip()
                agenda[nombre] = [telefono, email]
                print("\n\t\t\t\t\t✅ Contacto modificado con éxito.")
            else:
                print("\n\t\t\t\t\t❌ Modificación cancelada.")
        else:
            print("\n\t\t\t\t\t❌ El contacto no existe.")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t\t\t\t🗑️ Eliminar Contacto")
    if not agenda:
        print("\n\t\t\t\t\t❌ No hay contactos en la agenda.")
    else:
        nombre = input("\t\t\t\t\t Nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            respuesta = input(f"\t\t\t\t\t ¿Está seguro de eliminar el contacto {nombre}? (Si/No): ").lower().strip()
            if respuesta == "si":
                agenda.pop(nombre)
                print("\n\t\t\t\t\t✅ Contacto eliminado con éxito.")
            else:
                print("\n\t\t\t\t\t❌ Eliminación cancelada.")
        else:
            print("\n\t\t\t\t\t❌ El contacto no existe.")