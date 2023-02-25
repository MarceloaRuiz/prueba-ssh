def registro():
    nombre_usuario = input("Ingrese nuevo usuario: ")
    password = input("Ingrese nueva contraseña: ")
    base_datos.update({nombre_usuario: password})
    print("Se ha registrado correctamente")
    print(base_datos)


def login(usuario, password, base_datos):
    try:
        if base_datos[usuario] == password:
            print("Usuario logueado.")
    except:
        print("Usuario y/o contraseña incorrectos.")


def grabar():
    archivo = open("BaseDeDatos.txt", "a")
    import json
    from google.colab import drive
    drive.mount("/drive/")
    with open("/content/BaseDeDatos.txt", "a") as file:
        json.dump(base_datos, archivo)
    print("Informacion almacenada.")
    print("Gracias.")


print("Ingrese una opcion:\n1-Ingresar un nuevo usuario.\n2-Ingrese al sistema.\n3-Grabar. \n4-Salir.")
ingreso = -1
base_datos = {}
while ingreso != 4:
    ingreso = int(input("Opcion (1/2/3/4): "))
    if ingreso == 1:  # ingreso nuevo usuario
        registro()
    if ingreso == 2:  # loguin
        usuario = input("Ingrese nm de usuario: ")
        password = input("Ingrese su contraseña: ")
        login(usuario, password, base_datos)
    if ingreso == 3:  # graba los datos en el archivo .txt
        grabar()
    if ingreso == 4:  # sale del sistema
        print("Hasta luego .")


