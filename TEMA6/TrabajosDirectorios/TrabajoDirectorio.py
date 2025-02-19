import os 
import shutil
try:
    def CrearUsuario(dir, nom):
        usuario_dir = os.path.join(dir, nom)
        if not os.path.exists(usuario_dir):
            os.makedirs(usuario_dir)
            lugar_ftp = os.path.join(usuario_dir, "LugarFtp")
            os.makedirs(lugar_ftp)
            print("Usuario creado.")
        else:
            print("El usuario ya existe.")
            print(usuario_dir)

    def CrearFichero(dir, usuario, fichero, contenido):
        ruta_fichero = os.path.join(dir, usuario, fichero, "LugarFtp")
        fichero = open(ruta_fichero, "w", encoding="utf8")

    def BorrarUsuario(dir, nom_borrar):
        usuario_dir = os.path.join(dir, nom_borrar)
        if  os.path.exists(usuario_dir):
            shutil.rmtree(usuario_dir)
            print("usuario borrado")
        else:
            print("Este usuario no existe o esta mal escrito.")


    def listarUsuarios(dir):
        listaDirectorio = os.listdir(dir)
        for elemento in listaDirectorio:
            if os.path.isdir(os.path.join(dir,elemento)):
                print(elemento)   
except:
    print("j")

while True:
    dir_home = os.path.dirname(__file__)
    print("---Menu---")
    print("1. Crear usuario")
    print("2. Borrar usuario")
    print("3. Crear fichero en Usuario")
    print("4. Lista usuarios")
    print("5. Salir")
    
    opcion = str(input("Seleciona una opción: "))

    match opcion:
        case "1":
            nombre_usuario = input("Dime nombre de usuario: ")
            CrearUsuario(dir_home, nombre_usuario)
        case "2":
            nom_borrar = input("Dime nombre de usuario: ")
            BorrarUsuario(dir_home, nom_borrar)
        case "3":
            nombre_usuario = input("Dime nombre de usuario: ")
            nombre_fichero = input("Dime el nombre de fichero: ")
        case "4":
            print()
        case "5":
            print("Fin del programa")
            break
        case _: 
            print("Introduce bien la opción")