import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sys

#FORMATO DE TEXTO font=("Arial", 12,), fg="white", bg="grey25" 

class Aplicacion:
    def __init__(self):
        #Creacion de la ventana con tamaño max, min y color de fondo 
        
        
        self.ventana1=tk.Tk()
        self.ventana1.title("Registro de juegos")
        self.ventana1.geometry("800x700")
        self.ventana1.minsize(400, 500)
        self.ventana1.maxsize(1024, 768)
        self.registronote=ttk.Notebook(self.ventana1)
        self.ventana1.configure(bg="gray25")
        
        #Creacion de Entry o Cuadrados de texto
        
        
        self.titulo_var = tk.StringVar() #Contructor str
        self.entry_titulo=tk.Entry( self.ventana1, textvariable = self.titulo_var, width=25, font=("Arial", 12,), fg="white", bg="black", insertbackground="white", justify="center")
        self.entry_titulo.grid(column=1, row=1, pady=(80, 10), padx=(10, 50)) #Asignamos la posicion del Entry
        
        self.desarolladora_var = tk.StringVar()
        self.entry_desarolladora=tk.Entry(self.ventana1, textvariable=self.desarolladora_var, width=25, font=("Arial", 12,), fg="white", bg="black", insertbackground="white", justify="center" )
        self.entry_desarolladora.grid(column=1, row=2, pady=10, padx=(10, 50))
        
        self.editor_var = tk.StringVar()
        self.entry_editor=tk.Entry(self.ventana1, textvariable=self.editor_var, width=25, font=("Arial", 12,), fg="white", bg="black", insertbackground="white", justify="center")
        self.entry_editor.grid(column=1, row=3, pady=10, padx=(10, 50))
        
        self.fechaSalida_var=tk.StringVar()
        self.entry_fechaSalida=tk.Entry(textvariable=self.fechaSalida_var, width=25, font=("Arial", 12,), fg="white", bg="black", insertbackground="white", justify="center")
        self.entry_fechaSalida.grid(column=1, row=4, pady=10, padx=(10, 50))
        
        #Creacion Label Textos mostrados por pantalla
        
        
        
        self.label_titulo=tk.Label(self.ventana1, text="Titulo", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_titulo.grid(column=0, row=1, pady=(80, 10), padx=(10, 50))
        
        self.label_desarolladora=tk.Label(self.ventana1, text="Desarolladora", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_desarolladora.grid(column=0, row=2, pady=10, padx=(10, 50))
        
        self.label_editor=tk.Label(self.ventana1, text="Editor", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_editor.grid(column=0, row=3, pady=10, padx=(10, 50))
        
        self.label_fechaSalida=tk.Label(self.ventana1, text="Titulo", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_fechaSalida.grid(column=0, row=4, pady=10, padx=(10, 50))
        
        self.text_box=tk.Label(self.ventana1, text="Breve descripcion del juego", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.text_box.grid(column=0, row=5, pady=(40, 10), padx=(40, 50))
        
        self.label_etiquetas=tk.Label(self.ventana1,text="Etiquetas del juego:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_etiquetas.grid(column=0, row=6, pady=(40, 10), padx=(40, 50))
        
        #Creacion del textBox
        
        
        self.text_box=tk.Text(self.ventana1, width=40, height=10, font=("Arial", 12), fg="white", bg="black", insertbackground="white")
        self.text_box.grid(column=1, row=5, pady=(40, 10), padx=(10, 60))
        
        
        
        #Creacion de la listbox
        
        self.scroll = tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)
        self.etiquetas=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE, yscrollcommand=self.scroll.set)
        self.etiquetas.grid(column=1, row=6, pady=(40, 10), padx=(10, 0))
        self.scroll.configure(command=self.etiquetas.yview)
        self.scroll.grid(column=2, row=6, sticky="NS")
        self.etiquetas.insert(0,"Accion")
        self.etiquetas.insert(1,"Acceso anticipado")
        self.etiquetas.insert(2,"Agricultura y fabricacion")
        self.etiquetas.insert(3,"Arcade y ritmo")
        self.etiquetas.insert(4,"Aventura")
        self.etiquetas.insert(5,"Bandas sonoras")
        self.etiquetas.insert(6,"Carreras")
        self.etiquetas.insert(7,"Cartas y mesa")
        self.etiquetas.insert(8,"Ciencia ficcion")
        self.etiquetas.insert(9,"Contruccion y automatizacion")
        self.etiquetas.insert(10,"Deportes y carreras")
        self.etiquetas.insert(11,"Disparos en primera persona")
        self.etiquetas.insert(12,"Disparos en segunda persona")
        self.etiquetas.insert(13,"Espacio y vuelo")
        self.etiquetas.insert(14,"Estrategia")
        self.etiquetas.insert(15,"Hack and slash")
        self.etiquetas.insert(16,"Hardware de RV")
        self.etiquetas.insert(17,"Lucha y artes marciales")
        self.etiquetas.insert(18,"Militares")
        self.etiquetas.insert(19,"Mundo abierto")
        self.etiquetas.insert(20,"Multijugador")
        self.etiquetas.insert(21,"Multijugador en linea")
        self.etiquetas.insert(22,"Novelas visuales")
        self.etiquetas.insert(23,"Pesca y caza")
        self.etiquetas.insert(24,"Plata forma y corredores")
        self.etiquetas.insert(25,"Puzles")
        self.etiquetas.insert(26,"Remote play")
        self.etiquetas.insert(27,"Rol")
        self.etiquetas.insert(28,"Roguelike")
        self.etiquetas.insert(29,"Simulacion")
        self.etiquetas.insert(30,"Terror")
        self.etiquetas.insert(31,"Un jugador")
    
        
        
         
         
        self.ventana1.mainloop()       
aplicacion1=Aplicacion()