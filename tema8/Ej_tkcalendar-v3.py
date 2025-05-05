import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from tkcalendar import Calendar
import mysql.connector

class MiniAgenda(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Añadir nueva cita")
        self.geometry("600x400")
        self.resizable(False, False)
        self.citas = []

        # Conexión a MySQL
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='bbdd',  # cámbiala por la real
            database='calendario'
        )
        self.cursor = self.conn.cursor()

        self.create_widgets()
        self.cargar_citas()
        cal = Calendar(root, selectmode="day", loccale="es_ES", datepattern="dd/mm/yyyy")
        cal.pack(pady=20, padx=20)
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

        columns = ("ID", "Nombre", "Fecha")
        self.tree = ttk.Treeview(frame_list, columns=columns, show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.column("ID", width=50)
        self.tree.pack(fill='both', expand=True)

        # Frame inferior para eliminar cita
        btn_delete = tk.Button(self, text="Eliminar cita seleccionada", command=self.borrar_cita)
        btn_delete.pack(pady=10)

    def agregar_cita(self):
        nombre = self.entry_nombre.get().strip()
        fecha = self.entry_fecha.get().strip()
        if nombre and fecha:
            try:
                # Insertar cita en la base de datos
                sql = "INSERT INTO citas (nombre, fecha) VALUES (%s, %s)"
                self.cursor.execute(sql, (nombre, fecha))
                self.conn.commit()

                # Insertar cita en el Treeview
                cita_id = self.cursor.lastrowid
                self.tree.insert("", "end", values=(cita_id, nombre, fecha))

                # Limpiar campos
                self.entry_nombre.delete(0, tk.END)
                self.entry_fecha.delete(0, tk.END)
                self.entry_fecha.insert(0, "2025-06-06")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo añadir la cita: {err}")
        else:
            messagebox.showwarning("Campos vacíos", "Por favor, introduce nombre y fecha.")

    def cargar_citas(self):
        try:
            # Cargar citas desde la base de datos
            self.cursor.execute("SELECT id, nombre, fecha FROM citas")
            citas = self.cursor.fetchall()
            for cita in citas:
                self.tree.insert("", "end", values=cita)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudieron cargar las citas: {err}")

    def borrar_cita(self):
        selected = self.tree.selection()
        if selected:
            try:
                # Obtener el ID de la cita seleccionada
                item = self.tree.item(selected[0])
                cita_id = item["values"][0]

                # Eliminar cita de la base de datos
                sql = "DELETE FROM citas WHERE id = %s"
                self.cursor.execute(sql, (cita_id,))
                self.conn.commit()

                # Eliminar cita del Treeview
                self.tree.delete(selected)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"No se pudo eliminar la cita: {err}")
        else:
            messagebox.showwarning("Sin selección", "Selecciona una cita para eliminar.")

    def __del__(self):
        # Cerrar la conexión a la base de datos al cerrar la aplicación
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()

if __name__ == "__main__":
    app = MiniAgenda()
    app.mainloop()