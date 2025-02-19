import os
import shutil

def CrearUsuario(dir,nom):
    usuario_dir = os.path.join(dir,nom)
    if not os.path.exists(usuario_dir):
          os.makedirs(usuario_dir)
          lugar_ftp = os.path.join(usuario_dir,"LugarFtp")
          os.makedirs(lugar_ftp)
          print("Usuario creado")
    else:
         print("El usuario ya existe")

def CrearFichero(dir, usuario, fichero, contenido):
     ruta_fichero = os.path.join(dir,usuario,"LugarFtp",fichero)
     fichero = open(ruta_fichero,'w', encoding="utf-8")
     fichero.write(contenido)
     print("fichero creado")

def BorrarDirectorio(dir, usuario):
    usuario_dir = os.path.join(dir,usuario)
    if os.path.exists(usuario_dir):
        shutil.rmtree(usuario_dir)
        print("Usuario borrado")
    else:
         print("El directorio no existe")     

def listarUsuarios(dir):
     listaDirectorio = os.listdir(dir)
     for elemento in listaDirectorio:
          if os.path.isdir(os.path.join(dir,elemento)):
               print(elemento)
                
while True:
    dir_home = os.path.dirname(__file__)
    print("Menu")
    print("1. Crear Usuario")
    print("2. Borrar Usuario")
    print("3. Crear fichero en Usuario")
    print("4. Listar usuarios")
    print("5. Salir")
    opcion = input("Selecciona opciÃ³n:")
    match(opcion):
        case "1":
                nombre_usuario = input("Dime nombre de usuario:")
                CrearUsuario(dir_home, nombre_usuario)
        case "2":
              nombre_usuario = input("Dime nombre de usuario:")
              BorrarDirectorio(dir_home, nombre_usuario)
        case "3":
                nombre_usuario = input("Dime nombre de usuario:")
                nombre_fichero = input("Dime nombre de fichero:")
                contenido = input("Dime contenido:")
                CrearFichero(dir_home, nombre_usuario, nombre_fichero, contenido)
        case "4":
              listarUsuarios(dir_home)
        case "5":
              break
        case _:
            print("Opcion no valida, elige de nuevo")