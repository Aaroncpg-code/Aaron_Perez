
productos = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "IT", "Intel Core i5", "Nvidia GTX1050"],
    "2175HD": ["lenovo", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
    "fgdxFHD": ["HP", 15.6, "8GB", "DD", "IT", "Intel Core i3", "integrada"],
    "GF75HD": ["Asus", 15.6, "8GB", "DD", "IT", "Intel Core i7","Nvidia GTX1050"],
    "123FHD": ["lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
    "342FHD": ["lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"]
}

stock = {
    "8475HD": [387990,10],
    "2175HD": [327990,4],
    "JjfFHD": [424990,1],
    "fgdxFHD": [664990,21],
    "123FHD": [290890,32],
    "342FHD": [444990,7],
    "GF75HD": [749990,2],
    "UWU131HD": [349990,1],
    "FS1230HD": [249990,0]
}

def StockMarca(marca):
    marca = marca.lower()
    TotalStock = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            if modelo in stock:
                TotalStock += stock[modelo][1]
    print(f"El stock es: {TotalStock}")
def BusquedaPorPrecio(pMin, pMax):
    ListaResultado = []
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if pMin <= precio <= pMax and cantidad > 0 and modelo in productos:
            marca = productos[modelo][0]
            ListaResultado.append(f"{marca}--{modelo}")
    if ListaResultado:
        ListaResultado.sort()
        print(f"Los notebooks entre los precios consultas son:{ListaResultado}")
    else:
        print ("No hay notebooks en ese rango de precios.")
def ActualizarPrecios(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False
    
def menu():
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            marca = input("Ingrese la marca a consultar: ")
            StockMarca(marca)
        case "2":
            while True:
                try:
                    pMin = float(input("Ingrese el precio minimo: "))
                    pMax = float(input("Ingrese el precio maximo: "))
                    break
                except ValueError:
                    pass
            BusquedaPorPrecio(pMin, pMax)
        case "3":
            while True:
                modelo = input("Ingrese el modelo a actualizar: ")
                NuevoPrecio = int(input("Ingrese el precio nuevo: "))
                actualizado = ActualizarPrecios(modelo, NuevoPrecio)
                if actualizado:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
                otroPrecio = input("Desea actualizar otro precio (s,n)?: ").lower()
                if otroPrecio != "s":
                    break
        case "4":
            print ("Programa finalizado.")
            break
        case _:
            print ("Debe seleccionar una opción válida!!")



