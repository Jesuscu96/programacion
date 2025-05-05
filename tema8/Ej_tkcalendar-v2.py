import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
from tkcalendar import Calendar
import mysql.connector

class MiniAgenda(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Añadir nueva cita")
        self.geometry("600x400")
        self.resizable(False, False)
        self.create_widgets()
        self.citas = []
        
        # Conexión a MySQL
        self.conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='bbdd',  # cámbiala por la real
        database='calendario'
    )
    fecha_minima = datetime.now() + timedelta(days=1)

    def create_widgets(self):
        # Frame superior para añadir citas
        frame_add = tk.Frame(self)
        frame_add.pack(padx=10, pady=10, fill='x')

        tk.Label(frame_add, text="Nombre:").pack(side='left')
        self.entry_nombre = tk.Entry(frame_add, width=30)
        self.entry_nombre.pack(side='left', padx=5)

        tk.Label(frame_add, text="Fecha:").pack(side='left')
        self.entry_fecha = tk.Entry(frame_add, width=12)
        self.entry_fecha.insert(0, "2025-06-06")
        self.entry_fecha.pack(side='left', padx=5)

        btn_add = tk.Button(frame_add, text="Añadir cita", command=self.agregar_cita)
        btn_add.pack(side='left', padx=5)

        # Frame central para mostrar citas
        frame_list = tk.Frame(self)
        frame_list.pack(padx=10, pady=10, fill='both', expand=True)

        tk.Label(frame_list, text="Citas registradas").pack(anchor='w')

        columns = ("Nombre", "Fecha")
        self.tree = ttk.Treeview(frame_list, columns=columns, show='headings')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.pack(fill='both', expand=True)

        # Frame inferior para eliminar cita
        btn_delete = tk.Button(self, text="Eliminar cita seleccionada", command=self.borrar_cita)
        btn_delete.pack(pady=10)

    def agregar_cita(self):
        nombre = self.entry_nombre.get().strip()
        fecha = self.entry_fecha.get().strip()
        if nombre and fecha:
            self.tree.insert("", "end", values=(nombre, fecha))
            self.entry_nombre.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos vacíos", "Por favor, introduce nombre y fecha.")

    def borrar_cita(self):
        selected = self.tree.selection()
        if selected:
            self.tree.delete(selected)
        else:
            messagebox.showwarning("Sin selección", "Selecciona una cita para eliminar.")

if __name__ == "__main__":
    app = MiniAgenda()
    app.mainloop()