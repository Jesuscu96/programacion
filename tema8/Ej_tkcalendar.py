import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from tkcalendar import Calendar
import mysql.connector

class AppClientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda")
        
        # Conexión a MySQL
        self.conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='bbdd',  # cámbiala por la real
        database='calendario'
    )
        self.cursor = self.conn.cursor()
        form_frame = ttk.LabelFrame(root, text="Formulario Cliente")
        form_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = ttk.Entry(form_frame)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(form_frame, text="Email:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_email = ttk.Entry(form_frame)
        self.entry_email.grid(row=0, column=3, padx=5, pady=5)
        ttk.Label(form_frame, text="Teléfono:").grid(row=0, column=4, padx=5, pady=5)
        self.entry_telefono = ttk.Entry(form_frame)
        self.entry_telefono.grid(row=0, column=5, padx=5, pady=5)
        ttk.Button(form_frame, text="Añadir cliente", command=self.insertar_cliente).grid(row=0, column=6, padx=5)
        # === botón Modificar ===
        ttk.Button(form_frame, text="Modificar cliente", command=self.modificar_cliente).grid(row=0, column=7, padx=5)

        # === Treeview ===
        bottom_frame = ttk.Frame(root)
        bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree = ttk.Treeview(bottom_frame, columns=("ID", "Nombre", "Email", "Teléfono"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.cargar_cliente_en_formulario)
        scrollbar = ttk.Scrollbar(bottom_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        ttk.Button(root, text="Eliminar cliente seleccionado", command=self.eliminar_cliente).pack(pady=5)

        self.mostrar_clientes()
     # === Cargar datos de la seleccion ===
    def cargar_cliente_en_formulario(self, event):
        seleccion = self.tree.selection()
        if not seleccion:
            return
        item = self.tree.item(seleccion)
        cliente = item["values"]
        self.cliente_seleccionado_id = cliente[0]
        self.entry_nombre.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_nombre.insert(0, cliente[1])
        self.entry_email.insert(0, cliente[2])
        self.entry_telefono.insert(0, cliente[3])

     # === Método para modificar ===
    def modificar_cliente(self):
        if self.cliente_seleccionado_id is None:
            messagebox.showwarning("Ningún cliente seleccionado", "Selecciona un cliente para modificar.")
            return
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()
        if not nombre or not email or not telefono:
            messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
            return
        sql = "UPDATE clientes SET nombre=%s, email=%s, telefono=%s WHERE Identificador=%s"
        valores = (nombre, email, telefono, self.cliente_seleccionado_id)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        self.mostrar_clientes()
        self.limpiar_formulario()
        messagebox.showinfo("Actualizado", "Cliente modificado correctamente.")

    def mostrar_clientes(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.cursor.execute("SELECT * FROM clientes")
        for cliente in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=cliente)

    def insertar_cliente(self):
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()

        if not nombre or not email or not telefono:
            messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
            return

        sql = "INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)"
        valores = (nombre, email, telefono)
        self.cursor.execute(sql, valores)
        self.conn.commit()

        self.limpiar_formulario()
        self.mostrar_clientes()
        messagebox.showinfo("Éxito", "Cliente añadido correctamente.")

    def eliminar_cliente(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selecciona un cliente", "Por favor, selecciona un cliente para eliminar.")
            return

        item = self.tree.item(seleccion)
        cliente_id = item["values"][0]

        confirmar = messagebox.askyesno("Confirmar eliminación", f"¿Deseas eliminar el cliente con ID {cliente_id}?")
        if confirmar:
            self.cursor.execute("DELETE FROM clientes WHERE Identificador = %s", (cliente_id,))
            self.conn.commit()
            self.mostrar_clientes()
            self.limpiar_formulario()
            messagebox.showinfo("Eliminado", "Cliente eliminado correctamente.")

   
    def limpiar_formulario(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.cliente_seleccionado_id = None

# === Ejecutar app ===
root = tk.Tk()
app = AppClientes(root)
root.mainloop()