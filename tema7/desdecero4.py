import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sys
import os

#FORMATO DE TEXTO font=("Arial", 12,), fg="white", bg="grey25" 

class Aplicacion:
    def __init__(self):
        #Creacion de la ventana con tamaño max, min y color de fondo 
        
        
        self.ventana1=tk.Tk()
        self.ventana1.title("Registro de juegos")
        self.ventana1.geometry("800x700")
        #self.ventana1.minsize(400, 500)
        #self.ventana1.maxsize(1024, 768)
        self.registronote=ttk.Notebook(self.ventana1)
        self.ventana1.configure(bg="gray25")
        
        style = ttk.Style()
        style.theme_use("default") # depende del sistema pude dar error una default o clam
        style.configure("TFrame", background="gray25")
        style.configure("TLabel", foreground="white", font=("Arial", 12, "bold"))
        style.configure("TNotebook", background="gray25", borderwidth=0)
        style.configure("TNotebook.Tab", background="gray15", foreground="white", font=("Arial", 14))
        style.map("TNotebook.Tab", background=[("selected", "#333333")], foreground=[("selected", "cyan")])
        
        #Creacion de un menu de opciones
        
        
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1=tk.Menu(menubar1)
        opciones1.add_command(label="Guardar", command=self.save)
        opciones1.add_command(label="Abrir", )
        opciones1.add_command(label="Salir", command=self.menusalir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)
        
        #Creacion del notebook
        
        
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.cuaderno1.pack(expand=True, fill="both")
            ###Todos los Entry, Text Box y FRAME 1### 
        self.pagina1 = ttk.Frame(self.cuaderno1, style="TFrame")
        self.cuaderno1.add(self.pagina1, text="Pagina 1")
        
            ###Todos los Lisbox, un check multiple de idioma y FRAME 2###
        self.pagina2 = ttk.Frame(self.cuaderno1, style="TFrame")
        self.cuaderno1.add(self.pagina2, text="Pagina 2")
       
            ###Un check multiple de plataforma, un check unico de reseñas, spimbox, listbox y FRAME 3###
        self.pagina3 = ttk.Frame(self.cuaderno1, style="TFrame")
        self.cuaderno1.add(self.pagina3, text="Pagina 3")        
        
        #Creacion de Entry o Cuadrados de texto
        
        
        self.titulo_var = tk.StringVar() #Contructor str
        self.entry_titulo=tk.Entry( self.pagina1, textvariable = self.titulo_var, width=25, font=("Arial", 12,), fg="white", bg="black", insertbackground="white", justify="center")
        self.entry_titulo.grid(column=1, row=0, pady=10, padx=(10, 190)) 
        
        #Asignamos la posicion del Entry
        
        self.desarrolladora_var = tk.StringVar()
        self.entry_desarrolladora=tk.Entry(self.pagina1, textvariable=self.desarrolladora_var, width=25, font=("Arial", 12,), fg="white", bg="black", insertbackground="white", justify="center" )
        self.entry_desarrolladora.grid(column=1, row=1, pady=10, padx=(10, 190))
        
        self.editor_var = tk.StringVar()
        self.entry_editor=tk.Entry(self.pagina1, textvariable=self.editor_var, width=25, font=("Arial", 12,), fg="white", bg="black", insertbackground="white", justify="center")
        self.entry_editor.grid(column=1, row=2, pady=10, padx=(10, 190))
        
        self.fechaSalida_var=tk.StringVar()
        self.entry_fechaSalida=tk.Entry(self.pagina1, textvariable=self.fechaSalida_var, width=25, font=("Arial", 12,), fg="white", bg="black", insertbackground="white", justify="center")
        self.entry_fechaSalida.grid(column=1, row=3, pady=10, padx=(10, 190))
        
        #Creacion Label Textos mostrados por pantalla
        
        
        
        self.label_titulo=tk.Label(self.pagina1, text="Titulo:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_titulo.grid(column=0, row=0, pady=(10, 10), padx=(10, 50))
        
        self.label_desarrolladora=tk.Label(self.pagina1, text="Desarrolladora:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_desarrolladora.grid(column=0, row=1, pady=10, padx=(10, 50))
        
        self.label_editor=tk.Label(self.pagina1, text="Editor:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_editor.grid(column=0, row=2, pady=10, padx=(10, 50))
        
        self.label_fechaSalida=tk.Label(self.pagina1, text="Fecha salida:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_fechaSalida.grid(column=0, row=3, pady=10, padx=(10, 50))
        
        self.text_box=tk.Label(self.pagina1, text="Breve descripcion del juego", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.text_box.grid(column=0, row=5, pady=(40, 10), padx=(40, 50))
        
        self.label_etiquetas=tk.Label(self.pagina2,text="Etiquetas del juego:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_etiquetas.grid(column=2, row=0, pady=(40, 10), padx=(40, 50))
       
        self.label_etiquetas1=tk.Label(self.pagina2,text="Idiomas del juego:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_etiquetas1.grid(column=2, row=1, pady=(40, 10), padx=(40, 50))
       
        self.label_check_idomas=tk.Label(self.pagina2, text="Adaptacion del idioma:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_check_idomas.grid(column=2, row=2, pady=(22, 15), padx=(40, 50))
        
        self.label_check_plataformas=tk.Label(self.pagina3, text="Plataformas de salida:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_check_plataformas.grid(column=0, row=0, pady=(22, 15), padx=(40, 50))
        
        self.label_reseñas=tk.Label(self.pagina3, text="Reseñas de los jugadores:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_reseñas.grid(column=0, row=1, pady=(70, 15), padx=(22, 0))
        
        self.label_precio=tk.Label(self.pagina3, text="Precio del juego en €:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_precio.grid(column=0, row=5, pady=(15, 15), padx=(22, 0))
        
        self.label_pegi=tk.Label(self.pagina3, text="Clasificacion PEGI:", font=("Arial", 12, "bold"), fg="white", bg="gray25")
        self.label_pegi.grid(column=0, row=6, pady=(15, 15), padx=(22, 0))
        
        #Creacion del textBox
        
        
        self.text_box=tk.Text(self.pagina1, width=40, height=10, font=("Arial", 12), fg="white", bg="black", insertbackground="white")
        self.text_box.grid(column=1, row=5, pady=(40, 10), padx=(10, 60))
            
        #Creacion del Frame
        
           
        self.frame_lista = tk.Frame(self.pagina2, bg="gray25")
        self.frame_lista.grid(column=3, row=0, pady=(40, 10), padx=(10, 60))
        
        #Creacion de la listbox JUEGOS
        
        
        
        self.etiquetas=tk.Listbox(self.frame_lista, selectmode=tk.MULTIPLE)
        #self.selected=self.etiquetas
        self.scroll = tk.Scrollbar(self.frame_lista, orient=tk.VERTICAL, command=self.etiquetas.yview)
        self.etiquetas.config(yscrollcommand=self.scroll.set)
        self.etiquetas.pack(side=tk.LEFT, fill=tk.BOTH)
        #self.etiquetas.grid(column=1, row=6, pady=(40, 10), padx=(10, 0))
        self.scroll.configure(command=self.etiquetas.yview)
        #self.scroll.grid(column=2, row=6, sticky="NS")
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y) 
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
         
        #Creacion de la listbox IDIOMAS
        
        
        self.etiquetas1=tk.Listbox(self.pagina2, selectmode=tk.MULTIPLE)
        self.etiquetas1.grid(column=3, row=1, pady=(15, 10), padx=(10, 70))
        
        self.etiquetas1.insert(0,"Ingles")
        self.etiquetas1.insert(1,"Español")
        self.etiquetas1.insert(2,"Portugues")
        self.etiquetas1.insert(3,"Aleman")
        self.etiquetas1.insert(4,"Japones")
        self.etiquetas1.insert(5,"Frances")
        self.etiquetas1.insert(6,"Chino")
        self.etiquetas1.insert(7,"Ruso")
         
        #Creacion de el check multiple para IDIOMAS
        
        
        # Creación de Checkbuttons para idiomas en Página 2
        self.frame_check_idiomas = tk.Frame(self.pagina2, bg="gray25")
        self.frame_check_idiomas.grid(column=3, row=2, pady=(15, 10), padx=(10, 70))

            # Opciones de idiomas
        idiomas = ["Interfaz", "Subtitulos", "Audio"]

            # Diccionario para almacenar el estado de cada idioma
        self.idiomas_estado = []
        for idioma in idiomas:
            # Crear una variable BooleanVar para cada idioma
            self.estado = tk.BooleanVar()
            self.idiomas_estado.append(self.estado) 

            # Crear el Checkbutton
            check_idioma = tk.Checkbutton(self.frame_check_idiomas, text=idioma, variable=self.estado, onvalue=True, offvalue=False, bg="gray25", fg="white", selectcolor="black", font=("Arial", 12, "bold"))
            check_idioma.pack(anchor="w")
             
        #Creacion de el check multiple para PLATAFORMA DE SALIDA
        
        
            # Creación de Checkbuttons para plataformas en Página 3
        self.frame_check_plataformas = tk.Frame(self.pagina3, bg="gray25")
        self.frame_check_plataformas.grid(column=1, row=0, pady=(15, 10), padx=(10, 70))

            # Opciones de idiomas
        plataformas = ["PS5", "PS4", "Xbox Series X", "Xbox ONE", "PC", "Nintendo Switch 1", "Nintendo Switch 2"]

            # Diccionario para almacenar el estado de cada plataforma
        self.plataformas = []
        for plataforma in plataformas:
            # Crear una variable BooleanVar para cada idioma
            self.estados = tk.BooleanVar()
            self.plataformas.append(self.estados) 

            # Crear el Checkbutton
            check_plataforma = tk.Checkbutton(self.frame_check_plataformas, text=plataforma, variable=self.estados, onvalue=True, offvalue=False, bg="gray25", fg="white", selectcolor="black", font=("Arial", 12, "bold"))
            check_plataforma.pack(anchor="w")
                
        #Creacion de el check radiobutton RESEÑAS
        
        
        self.reseñas = tk.IntVar()
        self.reseñas.set(2)
        self.frame_resenas = tk.Frame(self.pagina3, bg="gray25")
        self.frame_resenas.grid(column=1, row=1, pady=(15, 10), padx=(1, 90), rowspan=4)

        self.radio1 = tk.Radiobutton(self.frame_resenas, text="Muy positivas", bg="gray25", fg="white", selectcolor="black", font=("Arial", 12, "bold"), variable=self.reseñas, value=1)
        self.radio1.pack(anchor="w", pady=(5, 5))

        self.radio2 = tk.Radiobutton(self.frame_resenas, text="Positivas", bg="gray25", fg="white", selectcolor="black", font=("Arial", 12, "bold"), variable=self.reseñas, value=2)
        self.radio2.pack(anchor="w", pady=(5, 5))

        self.radio3 = tk.Radiobutton(self.frame_resenas, text="Negativas", bg="gray25", fg="white", selectcolor="black", font=("Arial", 12, "bold"), variable=self.reseñas, value=3)
        self.radio3.pack(anchor="w", pady=(5, 5))

        self.radio4 = tk.Radiobutton(self.frame_resenas, text="Muy negativas", bg="gray25", fg="white", selectcolor="black", font=("Arial", 12, "bold"), variable=self.reseñas, value=4)
        self.radio4.pack(anchor="w", pady=(5, 5))
            
        #Creacion de el Spinbox PRECIO
        
        
        self.precio = ttk.Spinbox(self.pagina3, from_=0, to=500, increment=0.5, width=10, font=("Arial", 12))
        self.precio.grid(column=1, row=5, pady=(10, 10), padx=(10, 110))
            
        #Creacion de el Combobox PEGI
        
        
        self.pegi_lista = ["+3", "+7", "+12", "+16", "+18"]
        self.pegi = ttk.Combobox(self.pagina3, values=self.pegi_lista, state="readonly", width=10, font=("Arial", 12))
        self.pegi.grid(column=1, row=6, pady=(10, 10), padx=(10, 110))
        self.pegi.current(0)
        
         
        
        self.ventana1.mainloop()
        
##########COPIADO DE EL EJERCICIO 2##########
   

    '''def menuabrir(self):
        with open("registro.txt","r") as archivo:
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
                    for i in range(self.list_hobbys.size():  #size recorre toda la lista
                        if self.list_hobbys.get(i) in hobbys:
                            self.list_hobbys.select_set(i)
                elif clave=="Pais":
                    self.pais.set(valor)
                elif clave=="Edad":
                    self.spinbox1.set(valor)'''
    def save(self):
        archivo = "registro.txt"
        path = os.listdir()
        if archivo in path:
            with open("registro.txt", "w", encoding="utf-8") as archivo:
                archivo.write(f"Titulo: " + self.entry_titulo.get() + "\n")
                archivo.write(f"Desarroladora: " + self.entry_desarrolladora.get() + "\n")
                archivo.write(f"Editor: " + self.entry_editor.get() + "\n")
                archivo.write(f"Fecha de salida: " + self.entry_fechaSalida.get() + "\n")
                archivo.write(f"Descripcion: " + self.text_box.get("1.0", tk.END).strip() + "\n")
                
                # Obtener etiquetas seleccionadas
                selection = [self.etiquetas.get(i) for i in self.etiquetas.curselection()]
                etiquetas_texto = ", ".join(selection) if selection else "Ninguna"
                archivo.write(f"Etiquetas del juego: " + etiquetas_texto + "\n")
                
                # Obtener idiomas seleccionados
                selection1 = [self.etiquetas1.get(i) for i in self.etiquetas1.curselection()]
                idiomas_texto = ", ".join(selection1) if selection1 else "Ninguno"
                archivo.write(f"Idiomas del juego: " + idiomas_texto + "\n")
                
                # Adaptación del idioma (Checkbuttons seleccionados)
                adaptacion_nombres = ["Interfaz", "Subtítulos", "Audio"]
                adaptacion_seleccionada = [adaptacion_nombres[i] for i, estado in enumerate(self.idiomas_estado) if estado.get()]
                adaptacion_texto = ", ".join(adaptacion_seleccionada) if adaptacion_seleccionada else "Ninguna"
                archivo.write(f"Adaptacion del idioma: " + adaptacion_texto + "\n")
                
                # Obtener plataformas seleccionadas
                plataformas_nombres = ["PS5", "PS4", "Xbox Series X", "Xbox ONE", "PC", "Nintendo Switch 1", "Nintendo Switch 2"]
                plataformas_seleccionadas = [plataformas_nombres[i] for i, estado in enumerate(self.plataformas) if estado.get()]
                archivo.write(f"Plataforma de salida: " + ", ".join(plataformas_seleccionadas) + "\n")
                
                archivo.write(f"Reseñas: " + str(self.reseñas.get()) + "\n")
                archivo.write(f"Precio: " + self.precio.get() + "\n")
                archivo.write(f"PEGI: " + self.pegi.get() + "\n")
        else:
            with open("registro.txt", "w", encoding="utf-8") as archivo:
                archivo.write(f"Titulo: " + self.entry_titulo.get() + "\n")
                archivo.write(f"Desarroladora: " + self.entry_desarrolladora.get() + "\n")
                archivo.write(f"Editor: " + self.entry_editor.get() + "\n")
                archivo.write(f"Fecha de salida: " + self.entry_fechaSalida.get() + "\n")
                archivo.write(f"Descripcion: " + self.text_box.get("1.0", tk.END).strip() + "\n")
                
                # Obtener etiquetas seleccionadas
                selection = [self.etiquetas.get(i) for i in self.etiquetas.curselection()]
                etiquetas_texto = ", ".join(selection) if selection else "Ninguna"
                archivo.write(f"Etiquetas del juego: " + etiquetas_texto + "\n")
                
                # Obtener idiomas seleccionados
                selection1 = [self.etiquetas1.get(i) for i in self.etiquetas1.curselection()]
                idiomas_texto = ", ".join(selection1) if selection1 else "Ninguno"
                archivo.write(f"Idiomas del juego: " + idiomas_texto + "\n")
                
                # Adaptación del idioma (Checkbuttons seleccionados)
                adaptacion_nombres = ["Interfaz", "Subtítulos", "Audio"]
                adaptacion_seleccionada = [adaptacion_nombres[i] for i, estado in enumerate(self.idiomas_estado) if estado.get()]
                adaptacion_texto = ", ".join(adaptacion_seleccionada) if adaptacion_seleccionada else "Ninguna"
                archivo.write(f"Adaptacion del idioma: " + adaptacion_texto + "\n")
                
                # Obtener plataformas seleccionadas
                plataformas_nombres = ["PS5", "PS4", "Xbox Series X", "Xbox ONE", "PC", "Nintendo Switch 1", "Nintendo Switch 2"]
                plataformas_seleccionadas = [plataformas_nombres[i] for i, estado in enumerate(self.plataformas) if estado.get()]
                archivo.write(f"Plataforma de salida: " + ", ".join(plataformas_seleccionadas) + "\n")
                
                archivo.write(f"Reseñas: " + str(self.reseñas.get()) + "\n")
                archivo.write(f"Precio: " + self.precio.get() + "\n")
                archivo.write(f"PEGI: " + self.pegi.get() + "\n")
            
            
            
            

    def menusalir(self):
        respuesta=mb.askyesno("Advertencia", "¿Estas seguro que deseas salir?")
        if respuesta:
            sys.exit(0)
        else:
            print("Cancelado, la ventana sigue abierta.")
    
aplicacion1=Aplicacion()