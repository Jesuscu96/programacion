import os
import shutil

def CrearUsuario(dir,nom):
    usuario_dir=os.path.join(dir,nom)
    if not os.path.exists(usuario_dir):
        os.makedirs(usuario_dir)
        lugar_ftp = os.path.join(usuario_dir,"LugarFtp")
        os.makedirs(lugar_ftp)
        print("Usuario creado")
    else:
        print("El usuario ya existe")


def BorrarDirectorio(dir, usuario):
    usuario_dir = os.path.join(dir, usuario)
    if os.path.exists(usuario_dir):
        shutil.rmtree(usuario_dir)
        print(f"El directorio {usuario_dir} ha sido borrado")
    else:
        print("El directorio no existe")


def CrearFichero(dir,usuario,fichero,contenido):
    ruta_comprobar=os.path.join(dir,usuario,"LugarFtp")
    ruta_fichero=os.path.join(dir,usuario,"LugarFtp",fichero)
    if os.path.exists(ruta_comprobar):
        fichero=open(ruta_fichero,"w",encoding="utf-8")
        fichero.write(contenido)
        fichero.close()
        print("Fichero creado")
    else:
        print("El directorio no existe...")


def ListarUsuarios(dir):
    listaDirectorio=os.listdir(dir)
    for elemento in listaDirectorio:
        if os.path.isdir(os.path.join(dir,elemento)):
            print(elemento)


while True:
    dir_home=os.path.dirname(__file__)
    print("\n---Menu---\n1. Crear Usuario\n2. Borrar Usuario\n3. Crear fichero en Usuario\n4. Listar Usuarios\n5. Salir")
    opcion=input("Selecciona opción: ")
    match opcion:
        case "1":
            nombre_usuario=input("Dime nombre de usuario: ")
            CrearUsuario(dir_home, nombre_usuario)
        case "2":
            nombre_usuario=input("Dime nombre de usuario: ")
            BorrarDirectorio(dir_home, nombre_usuario)
        case "3":
            nombre_usuario=input("Dime nombre de usuario: ")
            nombre_fichero=input("Dime nombre de fichero: ")
            contenido=input("Dime contenido: ")
            CrearFichero(dir_home, nombre_usuario, nombre_fichero, contenido)
        case "4":
            ListarUsuarios(dir_home)
        case "5":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida, elige de nuevo")
