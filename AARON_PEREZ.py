usuarios = {}

def crear_usuario():
    while True:
        nombre_usuario = input("Ingrese nombre de usuario: ")
        if nombre_usuario in usuarios:
            print ("El nombre de usuario ya existe intente con otro.")
        else:
            break
    while True:
        sexo = input("Ingrese sexo (f/m): ")
        if sexo in ["f", "m"]:
            break
        print ("Debe ingresar (f o m)  solamente, intente de nuevo.")
    
    while True:  
        contraseña = input("Ingrese contraseña (mínimo 8 caracteres, sin espacios): ")
        if len(contraseña) >= 8 and " " not in contraseña:
                break
        print("Contraseña inválida. Debe tener al menos 8 caracteres y no contener espacios.")

    usuarios[nombre_usuario] = {
        "sexo" : sexo,
        "contraseña": contraseña}
    print("Contraseña valida.")
    print("Usuario ingresado con exito!!.")

def buscar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario a buscar: ")
    if nombre_usuario in usuarios:
        print(f"Usuario encontrado: {nombre_usuario}")
        print(f"Sexo: {usuarios[nombre_usuario]["sexo"]}")
        print(f"Contraseña: {usuarios[nombre_usuario]["contraseña"]}")
    else:
        print("Usuario no existe.")

def borrar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario a borrar: ")
    if nombre_usuario in usuarios:
        del usuarios[nombre_usuario]
        print("Usuario eliminado con éxito!.")
    else:
        print("No se pudo eliminar usuario!.")

def menu():
    print("1. Ingresar usuario.")
    print("2. Buscar usuario.")
    print("3. Eliminar usuario.")
    print("4. Salir.")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            crear_usuario()
        case "2":
            buscar_usuario()
        case "3":
            borrar_usuario()
        case "4":
            print ("Programa terminado...")
        case _:
            print ("Ingrese una opcion valida.")



