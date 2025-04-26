import tkinter as tk
from tkinter import ttk, filedialog
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
        opciones1=tk.Menu(menubar1,  tearoff=0)
        opciones1.add_command(label="Guardar", command=self.save)
        opciones1.add_command(label="Abrir", command=self.menu_abrir)
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
        
        #About me 
        self.pagina4 = ttk.Frame(self.cuaderno1, style="TFrame")
        self.cuaderno1.add(self.pagina4, text="Pagina 4")  

        #Creación botón
        boton_about = tk.Button(self.pagina4, text="About Me", command=self.abrir_about_me, bg="SlateGray3")
        boton_about.grid(row=2, column=3, pady=(10, 10), padx=(10, 70), sticky="e")
        
        boton_ayuda = tk.Button(self.pagina4, text="Ayuda", command=self.abrir_ayuda, bg="SlateGray3")
        boton_ayuda.grid(row=3, column=3, pady=(10, 10), padx=(10, 70), sticky="e")
        
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
        
        
        
        self.etiquetas = tk.Listbox(self.frame_lista, selectmode=tk.MULTIPLE, exportselection=False)
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
        
        
        self.etiquetas1 = tk.Listbox(self.pagina2, selectmode=tk.MULTIPLE, exportselection=False)
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
        self.idiomas_nombres = idiomas


            # Diccionario para almacenar el estado de cada idioma
        self.idiomas_estado = []
        for idioma in idiomas:
            # Crear una variable BooleanVar para cada idioma
            adaptacion = tk.BooleanVar()
            self.idiomas_estado.append(adaptacion) 

            # Crear el Checkbutton
            check_idioma = tk.Checkbutton(self.frame_check_idiomas, text=idioma, variable=adaptacion, onvalue=True, offvalue=False, bg="gray25", fg="white", selectcolor="black", font=("Arial", 12, "bold"))
            check_idioma.pack(anchor="w")
             
        #Creacion de el check multiple para PLATAFORMA DE SALIDA
        
        
            # Creación de Checkbuttons para plataformas en Página 3
        self.frame_check_plataformas = tk.Frame(self.pagina3, bg="gray25")
        self.frame_check_plataformas.grid(column=1, row=0, pady=(15, 10), padx=(10, 70))

            # Opciones de plataformas
        self.plataformas_nombres = ["PS5", "PS4", "Xbox Series X", "Xbox ONE", "PC", "Nintendo Switch 1", "Nintendo Switch 2"]

            # Diccionario para almacenar el estado de cada plataforma
        self.plataformas = []
        for plataforma in self.plataformas_nombres:
            # Crear una variable BooleanVar para cada plataforma
            estado = tk.BooleanVar()
            self.plataformas.append(estado)

            # Crear el Checkbutton
            check_plataforma = tk.Checkbutton(self.frame_check_plataformas, text=plataforma, variable=estado, onvalue=True, offvalue=False, bg="gray25", fg="white", selectcolor="black", font=("Arial", 12, "bold"))
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
        
    def reseñas_texto(self):
        # Obtener el valor seleccionado del Radiobutton
        reseñas_seleccionadas = self.reseñas.get()
        # Actualizar el texto de reseña según la opción seleccionada
        match reseñas_seleccionadas:
            case 1:
                self.texto_reseña = "Muy positivas"
            case 2:  
                self.texto_reseña = "Positivas"
            case 3:
                self.texto_reseña = "Negativas"
            case 4:
                self.texto_reseña = "Muy negativas"
         
        
        

    def abrir_about_me(self):
        ventana_about = tk.Toplevel(self.ventana1)
        ventana_about.title("Sobre la App")
        ventana_about.configure(bg="gray20")
        ventana_about.geometry("400x250")
        texto = (
            "📌 Aplicación de Registro de Juegos\n"
            "🧑 Desarrollado por: Jesús Clemente\n"
            "🕹️ Permite registrar información sobre videojuegos\n"
            "📁 Guarda etiquetas, idiomas, y más\n"
            "💡 Versión: 1.0\n"
            "📅 Fecha: Abril 2025"
        )

        label_about = tk.Label(ventana_about, text=texto, bg="gray20", fg="white", font=("Arial", 10), justify="left")
        label_about.pack(padx=20, pady=20)
        
    def abrir_ayuda(self):
        ventana_about1 = tk.Toplevel(self.ventana1)
        ventana_about1.title("Ayuda de la App")
        ventana_about1.configure(bg="gray20")
        ventana_about1.geometry("800x350")
        
        texto = (
            "Esta es una aplicación para introducir todos los datos necesarios para los viedojuegos. \n "
            "Tenemos 4 pestañas las tres priemeras son para introdicir los datos y la ultima la cuarta es paro ofrecer informacion. \n"
            "Desde el menu tienes estas tres opciones: abrir, guardar y salir del programa. \n"
            "Abrir: Abre un archivo de texto donde podras modificar el archivo creado. \n"
            "Antes de salir asugurate de guardar tus datos y no olvidar su ubicación o se perderan. \n"
            "Los selectores de etiquetas de juego y selector de idioma son de elección múltiple ambos. \n"
            "La adaptacion del idioma y seleccion de plataforma son elección multiple. \n"
            "Las reseñas son un selector de una sola opción. \n"
            "El precio es un selector de tipo flechas para cambiar el precio pero tabien puedes clicar y introducirlo mediante teclado. \n"
            "El PEGI es un selector de una sola opción. \n"
        )
        label_about = tk.Label(ventana_about1, text=texto, bg="gray20", fg="white", font=("Arial", 10), justify="left")
        label_about.pack(padx=20, pady=(15, 0))
        


        

   

    
    def guardar_datos(self, archivo):
        
        archivo.write(f"Título: {self.entry_titulo.get()}\n")
        archivo.write(f"Desarrolladora: {self.entry_desarrolladora.get()}\n")
        archivo.write(f"Editor: {self.entry_editor.get()}\n")
        archivo.write(f"Fecha de salida: {self.entry_fechaSalida.get()}\n")
        archivo.write(f"Descripción: {self.text_box.get('1.0', tk.END).strip()}\n")
        archivo.write(f"Reseñas: {self.texto_reseña}\n")
        archivo.write(f"Precio: {self.precio.get()}\n")
        archivo.write(f"PEGI: {self.pegi.get()}\n")

        # Etiquetas seleccionadas
        seleccion_etiquetas = [self.etiquetas.get(i) for i in self.etiquetas.curselection()]
        etiquetas_texto = ", ".join(seleccion_etiquetas) if seleccion_etiquetas else "Ninguna"
        archivo.write(f"Etiquetas del juego: {etiquetas_texto}\n")

        # Idiomas seleccionados
        seleccion_idiomas = [self.etiquetas1.get(i) for i in self.etiquetas1.curselection()]
        idiomas_texto = ", ".join(seleccion_idiomas) if seleccion_idiomas else "Ninguno"
        archivo.write(f"Idiomas del juego: {idiomas_texto}\n")

        # Adaptación del idioma
        adaptacion_texto = ", ".join(
            self.idiomas_nombres[i] for i, estado in enumerate(self.idiomas_estado) if estado.get()
        )
        adaptacion_texto = adaptacion_texto if adaptacion_texto else "Ninguna"
        archivo.write(f"Adaptación del idioma: {adaptacion_texto}\n")


        # Plataformas seleccionadas
        plataformas_texto = ", ".join(
            self.plataformas_nombres[i] for i, estado in enumerate(self.plataformas) if estado.get()
        )
        plataformas_texto = plataformas_texto if plataformas_texto else "Ninguna"
        archivo.write(f"Plataformas seleccionadas: {plataformas_texto}\n")


    def save(self):
        archivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Texto", "*.txt")])
        
        path = os.listdir()
        if archivo in path:
            confirmar = mb.askyesno("Confirmar guardado", "¿Estás seguro de que quieres guardar los datos?")
            if not confirmar:
                return
            with open(archivo, "w", encoding="utf-8") as archivo:
                self.guardar_datos(archivo)
        else:
            confirmar = mb.askyesno("Confirmar guardado", "¿Estás seguro de que quieres guardar los datos?")
            if not confirmar:
                return
            with open(archivo, "w", encoding="utf-8") as archivo:
                self.guardar_datos(archivo)
    
    
    def menu_abrir(self):
        try:
            archivo = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Texto", "*.txt")])
            with open(archivo, "r", encoding="utf-8") as archivo:
                lines = archivo.readlines()
                for line in lines:
                    clave, valor = line.strip().split(":", 1)
                    valor = valor.strip()
                    if clave == "Titulo":
                        self.titulo_var.set(valor)
                    elif clave == "Desarroladora":
                        self.desarrolladora_var.set(valor)
                    elif clave == "Editor":
                        self.editor_var.set(valor)
                    elif clave == "Fecha de salida":
                        self.fechaSalida_var.set(valor)
                    elif clave == "Descripcion":
                        self.text_box.delete("1.0", tk.END)
                        self.text_box.insert(tk.END, valor)
                    elif clave == "Etiquetas del juego":
                        etiquetas = valor.split(",")
                        for etiqueta in etiquetas:
                            if etiqueta.strip() in self.etiquetas.get(0, tk.END):
                                index = self.etiquetas.get(0, tk.END).index(etiqueta.strip())
                                self.etiquetas.select_set(index)
                    elif clave == "Idiomas del juego":
                        idiomas = valor.split(",")
                        for idioma in idiomas:
                            if idioma.strip() in self.etiquetas1.get(0, tk.END):
                                index = self.etiquetas1.get(0, tk.END).index(idioma.strip())
                                self.etiquetas1.select_set(index)
                    elif clave == "Adaptacion del idioma":  
                        adaptacion = valor.split(",")
                        for i, estado in enumerate(self.idiomas_estado):
                            if self.idiomas_nombres[i] in adaptacion:
                                estado.set(True)
                            else:
                                estado.set(False)
                    elif clave == "Plataformas seleccionadas":
                        plataformas = valor.split(",")
                        for i, estado in enumerate(self.plataformas):
                            if self.plataformas_nombres[i] in plataformas:
                                estado.set(True)
                            else:
                                estado.set(False)
                    elif clave == "Reseñas":
                        if valor == "Muy positivas":
                            self.reseñas.set(1)
                        elif valor == "Positivas":
                            self.reseñas.set(2)
                        elif valor == "Negativas":
                            self.reseñas.set(3)
                        elif valor == "Muy negativas":
                            self.reseñas.set(4)                        
                    elif clave == "Precio":
                        self.precio.set(valor)
                    elif clave == "PEGI":
                        self.pegi.set(valor)
                    # Puedes seguir completando para otros campos si lo deseas
            mb.showinfo("Archivo abierto", "Datos cargados correctamente.")
        except Exception as e:
            mb.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
                         
    


    def menusalir(self):
        respuesta=mb.askyesno("Advertencia", "¿Estas seguro que deseas salir?")
        if respuesta:
            sys.exit(0)
        else:
            print("Cancelado, la ventana sigue abierta.")
    
aplicacion1=Aplicacion()