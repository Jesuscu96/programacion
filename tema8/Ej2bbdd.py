import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class AppClientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Clientes")

        # Conexión a MySQL
        self.conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='bbdd',  # cámbiala por la real
        database='gestionempresarial'
    )
        self.cursor = self.conn.cursor()
        # Treeview para mostrar los clientes
        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Email", "Teléfono"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.mostrar_clientes()

    def mostrar_clientes(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.cursor.execute("SELECT * FROM clientes")
        for cliente in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=cliente)

root = tk.Tk()
app = AppClientes(root)
root.mainloop()