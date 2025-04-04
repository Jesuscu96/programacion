import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Ejercicio 1")
        self.ventana1.geometry("800x800")
        self.ventana1.configure(bg="white")
        self.ventana1.mainloop()
        self.seleccion=tk.IntVar()
        self.seleccion.set(3)
        self.radio1 = tk.Radiobutton(self.ventana1, variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=1)
        
aplicacion1=Aplicacion()