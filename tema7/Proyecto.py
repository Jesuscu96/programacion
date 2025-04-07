import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sys
class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Registro de juegos")
        self.ventana1.geometry("650x700")
        self.ventana1.minsize(400, 500)
        self.ventana1.maxsize(1024, 768)
        self.registronote=ttk.Notebook(self.ventana1)
        self.ventana1.configure(bg="black")
        

        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1=tk.Menu(menubar1)
        opciones1.add_command(label="Guardar", command=self.menuguardar)
        opciones1.add_command(label="Abrir", command=self.menuabrir)
        opciones1.add_command(label="Salir", command=self.menusalir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)
        
        self.registronote.grid(column=0)
        self.registronoteframe=ttk.Frame(self.registronote)
        self.registronote.add(self.registronoteframe,text="Registro")
        self.label1=tk.Label(self.registronoteframe, text="Registro de Alumno")
        self.label1.grid(column=0,row=0)
        

        self.label2=tk.Label(self.registronoteframe,text="Nombre:")
        self.label2.grid(column=0, row=1)
        self.dato_nombre=tk.StringVar()
        self.entry1=tk.Entry(self.registronoteframe, width=10, textvariable=self.dato_nombre)
        self.entry1.grid(column=1, row=1)

        self.label3=tk.Label(self.registronoteframe,text="Apellido:")
        self.label3.grid(column=0, row=2)
        self.dato_apellido=tk.StringVar()
        self.entry2=tk.Entry(self.registronoteframe, width=10, textvariable=self.dato_apellido)
        self.entry2.grid(column=1, row=2)

        self.label4=tk.Label(self.registronoteframe,text="Direccion:")
        self.label4.grid(column=0, row=3)
        self.dato_direccion=tk.StringVar()
        self.entry3=tk.Entry(self.registronoteframe, width=10, textvariable=self.dato_direccion)
        self.entry3.grid(column=1, row=3)

        self.label5=tk.Label(self.registronoteframe,text="Telofono:")
        self.label5.grid(column=0, row=4)
        self.dato_telefono=tk.StringVar()
        self.entry4=tk.Entry(self.registronoteframe, width=10, textvariable=self.dato_telefono)
        self.entry4.grid(column=1, row=4)

        self.label6=tk.Label(self.registronoteframe,text="Sexo:")
        self.label6.grid(column=0, row=5)
        self.select_sexo = tk.StringVar()  
        self.select1=tk.Radiobutton(self.registronoteframe, text="Masculino", variable=self.select_sexo, value="masculino")
        self.select1.grid(column=1, row=5)
        self.select2=tk.Radiobutton(self.registronoteframe, text="Femenino", variable=self.select_sexo, value="femenino")
        self.select2.grid(column=1, row=6)

        self.select_becado = tk.BooleanVar()  
        self.check1=tk.Checkbutton(self.registronoteframe, text="Becado", variable=self.select_becado)
        self.check1.grid(column=1, row=7)

        self.label7=tk.Label(self.registronoteframe, text="Hobbys:")
        self.label7.grid(column=0,row=8)
        self.list_hobbys=tk.Listbox(self.registronoteframe, selectmode=tk.MULTIPLE)
        self.list_hobbys.insert(0,"Leer")
        self.list_hobbys.insert(1,"Deportes")
        self.list_hobbys.insert(2,"Cocinar")
        self.list_hobbys.insert(3,"Videojuegos")
        self.list_hobbys.grid(column=1,row=8)

        self.label8=tk.Label(self.registronoteframe, text="Selecciona el pais: ")
        self.label8.grid(column=0,row=10)
        self.pais=tk.StringVar()
        selectpais=("España", "Francia", "Portugal")
        self.combobox1=ttk.Combobox(self.registronoteframe, width=10, textvariable=self.pais, values=selectpais, state='readonly')
        self.combobox1.current(0)
        self.combobox1.grid(column=0,row=11)

        self.label9=tk.Label(self.registronoteframe, text="Edad: ")
        self.label9.grid(column=0,row=12)
        self.spinbox1=ttk.Spinbox(self.registronoteframe, from_=0, to=100, width=10, state='readonly')
        self.spinbox1.set(0)
        self.spinbox1.grid(column=0,row=13)

        self.registronoteframe2=ttk.Frame(self.registronote)
        self.registronote.add(self.registronoteframe2,text="Datos Matricula")
        self.labelnotebook1=tk.Label(self.registronoteframe2, text="Curso elegido: ")
        self.labelnotebook1.grid(column=0,row=0)
        self.entrynotebook1=tk.Entry(self.registronoteframe2)
        self.entrynotebook1.grid(column=1,row=0)
        self.labelnotebook2=tk.Label(self.registronoteframe2, text="Ciclo elegido: ")
        self.labelnotebook2.grid(column=0,row=1)
        self.entrynotebook2=tk.Entry(self.registronoteframe2)
        self.entrynotebook2.grid(column=1,row=1)
        self.ventana1.mainloop()

    def abrirdialogo(self):
        self.curso=tk.Toplevel(self.ventana1)
        self.curso.title("Matriculacion")
        self.curso.geometry("250x200")
        self.labelcurso1=tk.Label(self.curso, text="Elegir ciclo: ")
        self.labelcurso1.grid(column=0, row=0)
        self.notecomboboxciclo=tk.StringVar()
        selectcurso=("DAW", "SMR")
        self.notecombobox1=ttk.Combobox(self.curso, width=10, textvariable=self.notecomboboxciclo, values=selectcurso, state='readonly')
        self.notecombobox1.grid(column=1,row=0)
 
        self.labelcurso2=tk.Label(self.curso, text="Elegir curso: ")
        self.labelcurso2.grid(column=0, row=1)
        self.notecomboboxcurso=tk.StringVar()
        selectcurso=("Primero", "Segundo")
        self.notecombobox2=ttk.Combobox(self.curso, width=10, textvariable=self.notecomboboxcurso, values=selectcurso, state='readonly')
        self.notecombobox2.grid(column=1,row=1)

        self.confirmar=tk.Button(self.curso, text="Confirmar", command=self.notebook)
        self.confirmar.grid(column=0, row=4)
    
    def notebook(self):
        ciclo=self.notecomboboxciclo.get()
        curso=self.notecomboboxcurso.get()
        self.curso.destroy()
        self.entrynotebook1.insert(0,curso)
        self.entrynotebook2.insert(0,ciclo)

    def menuguardar(self):
        campos = [
        self.dato_nombre.get(),
        self.dato_apellido.get(),
        self.dato_direccion.get(),
        self.dato_telefono.get(),
        self.select_sexo.get(),
        self.pais.get(),
        self.spinbox1.get(),
    ]
        if any(not campo for campo in campos):
            mb.showerror("Error", "Todos los campos deben ser completados")
            return
        
        datos={
            "Nombre": self.dato_nombre.get(),
            "Apellido": self.dato_apellido.get(),
            "Direccion": self.dato_direccion.get(),
            "Telefono": self.dato_telefono.get(),
            "Sexo": self.select_sexo.get(),
            "Becado": self.select_becado.get(),
            "Hobbys": [self.list_hobbys.get(i)for i in self.list_hobbys.curselection()],  
#recorre la lita grafica y recoge lo que hay marcado con el curselection
            "Pais":self.pais.get(),
            "Edad":self.spinbox1.get(),
        }
        with open("alumn.txt","w") as archivo:
            for clave,valor in datos.items():
                if isinstance(valor,list):  #Transformador de cadena de texto
                    valor=",".join(valor)
                archivo.write(f"{clave}:{valor}\n")
        print("Guardado los datos correctamente.")
        self.abrirdialogo()

    def menuabrir(self):
        with open("alumn.txt","r") as archivo:
            lines=archivo.readlines()
            if not lines:
                print("Archivo vacio")
            for line in lines:
                clave,valor = line.strip().split(":",1)
                if clave== "Nombre":
                    self.dato_nombre.set(valor)
                elif clave=="Apellido":
                    self.dato_apellido.set(valor)
                elif clave=="Direccion":
                    self.dato_direccion.set(valor)
                elif clave=="Telefono":
                    self.dato_telefono.set(valor)
                elif clave=="Sexo":
                    self.select_sexo.set(valor)
                elif clave=="Becado":
                    self.select_becado.set(valor)
                elif clave=="Hobbys":
                    hobbys=valor.split(",") if valor else []
                    self.list_hobbys.select_clear(0,tk.END)  #tk.END hasta el ultimo elemento de la lista
                    for i in range(self.list_hobbys.size()):  #size recorre toda la lista
                        if self.list_hobbys.get(i) in hobbys:
                            self.list_hobbys.select_set(i)
                elif clave=="Pais":
                    self.pais.set(valor)
                elif clave=="Edad":
                    self.spinbox1.set(valor)

    def menusalir(self):
        respuesta=mb.askyesno("Advertencia", "¿Estas seguro que deseas salir?")
        if respuesta:
            sys.exit(0)
        else:
            print("Cancelado, la ventana sigue abierta.")
        
aplicacion1=Aplicacion()