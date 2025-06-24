usuarios = {}

def crear_usuario():
    sexo = input("Ingrese sexo (f/m): ")
    
    nombre_usuario = input("Ingrese nombre de usuario: ")
       
    contraseña = input("Ingrese contraseña (mínimo 8 caracteres, sin espacios): ")
    if len(contraseña) < 8 or " "  in contraseña:
        print("Contraseña inválida. Debe tener al menos 8 caracteres y no contener espacios.")
        return

    usuarios[nombre_usuario] = {
        "sexo" : sexo,
        "contraseña": contraseña}
    print("Usuario creado.")

def buscar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario a buscar: ")
    if nombre_usuario in usuarios:
        print(f"Usuario encontrado: {nombre_usuario}")
        print(f"Sexo: {usuarios[nombre_usuario]["sexo"]}")
    else:
        print("Usuario no existe.")

def borrar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario a borrar: ")
    if nombre_usuario in usuarios:
        del usuarios[nombre_usuario]
        print("Usuario borrado.")
    else:
        print("Usuario no existe.")

def menu():
    print("1. Crear un usuario.")
    print("2. Buscar un usuario.")
    print("3. Borrar un usuario.")
    print("4. Salir del programa.")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_usuario()
    elif opcion == "2":
        buscar_usuario()
    elif opcion == "3":
        borrar_usuario()
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("OPCION NO VALIDA.")



