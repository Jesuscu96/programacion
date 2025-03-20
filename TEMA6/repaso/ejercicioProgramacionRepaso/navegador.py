import os,webbrowser
def navegador():
    archivo="cine.txt"
    ruta=os.getcwd()
    webbrowser.open(ruta + "/" + archivo)
