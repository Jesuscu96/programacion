import tkinter as tk
from tkinter import ttk 
import sys 
import os

class Aplicacion:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Registro del alumno")
        self.label1=tk.Label(self.ventana,text="Registro del Alumno:")
        self.label1.grid(column=0, row=0)
        self.nombrelabel=tk.Label(self.ventana, text="Nombre")
        self.nombrelabel.grid(column=0, row=1)
        self.nombre=tk.Entry(self.ventana)
        self.nombre.grid(column=1, row=1)
        self.apellidoslabel=tk.Label(self.ventana, text="Apellidos")
        self.apellidoslabel.grid(column=0,row=2)
        self.apellidos=tk.Entry(self.ventana)
        self.apellidos.grid(column=1,row=2)
        self.dirlabel=tk.Label(self.ventana, text="Dirección")
        self.dirlabel.grid(column=0,row=3)
        self.dir=tk.Entry(self.ventana)
        self.dir.grid(column=1,row=3)
        self.tellabel=tk.Label(self.ventana, text="Télefono")
        self.tellabel.grid(column=0,row=4)
        self.telefono=tk.Entry(self.ventana)
        self.telefono.grid(column=1,row=4)
        self.sexolabel=tk.Label(self.ventana,text="Sexo:")
        self.sexolabel.grid(column=0,row=5)
        self.spinbox1=ttk.Spinbox(self.ventana, from_=0,to=100, width=10, state="readonly")
        self.spinbox1.bind("<<Increment>>", self.incremento)
        self.spinbox1.bind("<<Decrement>>", self.decremento)
        self.spinbox1.set(0)
        self.spinbox1.grid(column=1, row=11)
        self.label=ttk.Label(self.ventana, text="Edad actual: 0")
        self.label.grid(column=0, row=11)
        self.genero=tk.StringVar()
        self.radio1=tk.Radiobutton(self.ventana, text="Masculino", variable=self.genero,value="Masculino")
        self.radio1.grid(column=1, row=5)
        self.radio2=tk.Radiobutton(self.ventana, text="Femenino",variable=self.genero, value="Femenino")
        self.radio2.grid(column=1, row=6)
        self.checkbutton=tk.StringVar()
        self.becado=tk.Checkbutton(self.ventana,variable=self.checkbutton, text="Becado")
        self.becado.grid(column=1, row=7)
        self.hobby=tk.StringVar()
        self.hobbyslabel=tk.Label(self.ventana,text="Hobbys:")
        self.hobbyslabel.grid(column=0, row=8)
        self.hobbyslist=tk.Listbox(self.ventana)
        self.hobbyslist.grid(column=1, row=8)
        self.hobbyslist.insert(0,"Leer")
        self.hobbyslist.insert(1,"Deporte")
        self.hobbyslist.insert(2,"Cocinar")
        self.hobbyslist.insert(3,"Videojuegos")
        self.boton1=tk.Button(self.ventana,text="Recuperar",command=self.recuperar)
        self.boton1.grid(column=1, row=9)
        menu1=tk.Menu(self.ventana)
        self.ventana.config(menu=menu1)
        opciones1=tk.Menu(menu1)
        opciones1.add_command(label="Guardar",command=self.guardar)
        opciones1.add_command(label="Abrir",command=self.abrir)
        opciones1.add_command(label="Salir", command=self.salir)
        menu1.add_cascade(label="Archivo", menu=opciones1)
        self.pais=tk.StringVar()
        self.paislabel=tk.Label(self.ventana, text="Seleccione su país :")
        self.paislabel.grid(column=0, row=10)
        paises=("España","Francia","Portugal")
        self.combobox1=ttk.Combobox(self.ventana,width=10, textvariable=self.pais,values=paises)
        self.combobox1.current(0)
        self.combobox1.grid(column=1, row=10)
        '''self.cuaderno1 = ttk.Notebook(self.ventana) #Creación de un alumno
        self.cuaderno1.add(self.pagina1, text="Button") #asociación del frame1
        self.pagina2 = ttk.Frame(self.cuaderno1)#Creación del frame2
        self.cuaderno1.add(self.pagina2, text="Label") #asociación del frame2 al Notebook'''
        
        self.ventana.mainloop()

    def guardar(self): 
        archivo="alumno.txt"  
        path=os.listdir()
        if archivo in path:
            archivo=open(archivo,"w")
            archivo.write(f"Nombre:" + self.nombre.get() + "\n")
            archivo.write(f"Apellidos:" + self.apellidos.get()+"\n")
            archivo.write(f"Dirección:" + self.dir.get()+"\n")
            archivo.write(f"Telefono:"+ self.telefono.get()+"\n")
            archivo.write(f"Sexo:" + self.genero.get() + "\n")
            archivo.write(f"Becado:" + self.checkbutton.get() + "\n")
            archivo.write(f"Hobbys:" + self.hobby.get() + "\n")
            #archivo.write(f"Hobbys:" + self.hobbyslabel.get() + "\n")
            archivo.write(f"Pais: {self.pais.get()}")
            archivo.write(f"Edad:" + {self.spinbox1.get()} + "\n")


            #archivo.write(f"Becado:" + self.checkbutton.get() + "\n")
            #archivo.write(f"Hobbys:" + self.hobbyslist.get(0,tk.END) +"\n")
            archivo.close()

        else:
            archivo=open(archivo,"w")
            archivo.write(f"Nombre:" + self.nombre.get() + "\n")
            archivo.write(f"Apellidos:" + self.apellidos.get()+"\n")
            archivo.write(f"Dirección:" + self.dir.get()+"\n")
            archivo.write(f"Telefono:"+ self.telefono.get()+"\n")
            archivo.write(f"Sexo:" + self.genero.get() + "\n")
            archivo.write(f"Becado:" + self.checkbutton.get() + "\n")
            archivo.write(f"Hobbys:" + self.hobbyslabel + "\n")
            #archivo.write(f"Hobbys:" + self.hobbyslabel.get() + "\n")
            archivo.write(f"Pais: {self.pais.get()}")
            archivo.write(f"Edad:" + self.spinbox1.get() +"\n")


            archivo.close()

    def abrir(self):
        archivo="alumno.txt"  
        path=os.listdir()
        if archivo in path:
            with open(archivo,"r") as archivo:
                contenido = archivo.readlines()
                self.nombre.delete(0, tk.END)
                self.nombre.insert(tk.END, contenido[0].split(":")[1].strip())
                self.apellidos.delete(0, tk.END)
                self.apellidos.insert(tk.END, contenido[1].split(":")[1].strip())
                self.dir.delete(0, tk.END)
                self.dir.insert(tk.END, contenido[2].split(":")[1].strip())
                self.telefono.delete(0, tk.END)
                self.telefono.insert(tk.END, contenido[3].split(":")[1].strip())
                self.genero.set(contenido[4].split(":")[1].strip())
                self.checkbutton.set(contenido[5].split(":")[1].strip())
                self.hobbyslist.delete(0, tk.END)
                for hobby in contenido[6].split(":")[1].strip().split(","):
                    self.hobbyslist.insert(tk.END, hobby.strip())

    def incremento(self, event):
        edad = self.spinbox1.get()
        self.label.config(text=f"edad actual: {edad}")
    def decremento(self, event):
        edad = self.spinbox1.get()
        self.label.config(text=f"edad actual: {edad}")
        
    def salir(self):
        sys.exit(0)     
    def recuperar(self):
        if len(self.hobbyslist.curselection())!=0:
            self.hobbyslabel.configure(self.hobbyslist.get(self.hobbyslist.curselection)[0])
app=Aplicacion()
