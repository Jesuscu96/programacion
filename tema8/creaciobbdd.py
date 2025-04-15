import tkinter as tk

from tkinter import messagebox

import mysql.connector

from mysql.connector import Error



class DatabaseCreatorApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Creador de Base de Datos MySQL")

        self.root.geometry("500x400")

        

        # Variables de conexión

        self.host_var = tk.StringVar(value="localhost")

        self.user_var = tk.StringVar(value="root")

        self.password_var = tk.StringVar(value="")

        self.db_name_var = tk.StringVar(value="gestionempresarial")

        self.db_user_var = tk.StringVar(value="gestionempresarial")

        self.db_password_var = tk.StringVar(value="")

        

        # Frame

        conn_frame = tk.LabelFrame(root, text="Configuración de Conexión MySQL", padx=10, pady=10)

        conn_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(conn_frame, text="Host:").grid(row=0, column=0, sticky="e")

        tk.Entry(conn_frame, textvariable=self.host_var).grid(row=0, column=1, sticky="ew", padx=5, pady=2)

        tk.Label(conn_frame, text="Usuario MySQL:").grid(row=1, column=0, sticky="e")

        tk.Entry(conn_frame, textvariable=self.user_var).grid(row=1, column=1, sticky="ew", padx=5, pady=2)

        tk.Label(conn_frame, text="Contraseña MySQL:").grid(row=2, column=0, sticky="e")

        tk.Entry(conn_frame, textvariable=self.password_var, show="*").grid(row=2, column=1, sticky="ew", padx=5, pady=2)

        # Frame de base de datos

        db_frame = tk.LabelFrame(root, text="Configuración de la Base de Datos", padx=10, pady=10)

        db_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(db_frame, text="Nombre BD:").grid(row=0, column=0, sticky="e")

        tk.Entry(db_frame, textvariable=self.db_name_var).grid(row=0, column=1, sticky="ew", padx=5, pady=2)

        tk.Label(db_frame, text="Usuario BD:").grid(row=1, column=0, sticky="e")

        tk.Entry(db_frame, textvariable=self.db_user_var).grid(row=1, column=1, sticky="ew", padx=5, pady=2)

        tk.Label(db_frame, text="Contraseña BD:").grid(row=2, column=0, sticky="e")

        tk.Entry(db_frame, textvariable=self.db_password_var, show="*").grid(row=2, column=1, sticky="ew", padx=5, pady=2)

        tk.Button(root, text="Crear Base de Datos", command=self.create_database, 

                 bg="green", fg="white").pack(pady=20)

        # Área logs

        self.log_text = tk.Text(root, height=8, state="disabled")

        self.log_text.pack(pady=10, padx=10, fill="both", expand=True)

        

    def log_message(self, message):

        self.log_text.config(state="normal")

        self.log_text.insert("end", message + "\n")

        self.log_text.see("end")

        self.log_text.config(state="disabled")

        

    def create_database(self):

        try:

            # Conectar al servidor MySQL

            connection = mysql.connector.connect(

                host=self.host_var.get(),

                user=self.user_var.get(),

                password=self.password_var.get()

            )

            

            if connection.is_connected():

                self.log_message("Conexión establecida con el servidor MySQL")

                

                cursor = connection.cursor()

                

                # Crear la base de datos

                db_name = self.db_name_var.get()

                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

                self.log_message(f"Base de datos '{db_name}' creada o ya existente")

                

                # Crear usuario y permisos

                db_user = self.db_user_var.get()

                db_password = self.db_password_var.get()

                

                cursor.execute(f"CREATE USER IF NOT EXISTS '{db_user}'@'localhost' IDENTIFIED BY '{db_password}'")

                cursor.execute(f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'localhost'")

                cursor.execute("FLUSH PRIVILEGES")

                self.log_message(f"Usuario '{db_user}' creado y permisos asignados")

                

                # Usar la base de datos

                cursor.execute(f"USE {db_name}")

                

                # Crear tabla clientes

                cursor.execute("""

                CREATE TABLE IF NOT EXISTS `clientes` (

                    `Identificador` INT NOT NULL AUTO_INCREMENT,

                    `nombre` VARCHAR(255) NOT NULL,

                    `email` VARCHAR(255) NOT NULL,

                    `telefono` VARCHAR(255) NOT NULL,

                    PRIMARY KEY (`Identificador`)

                ) ENGINE = InnoDB

                """)

                self.log_message("Tabla 'clientes' creada")

                

                # Crear tabla productos

                cursor.execute("""

                CREATE TABLE IF NOT EXISTS `productos` (

                    `Identificador` INT NOT NULL AUTO_INCREMENT,

                    `nombre` VARCHAR(255) NOT NULL,

                    `descripcion` VARCHAR(255) NOT NULL,

                    `precio` DECIMAL(10,2) NOT NULL,

                    PRIMARY KEY (`Identificador`)

                ) ENGINE = InnoDB

                """)

                self.log_message("Tabla 'productos' creada")

                

                # Crear tabla categorias

                cursor.execute("""

                CREATE TABLE IF NOT EXISTS `categorias` (

                    `Identificador` INT NOT NULL AUTO_INCREMENT,

                    `nombre` VARCHAR(255) NOT NULL,

                    PRIMARY KEY (`Identificador`)

                ) ENGINE = InnoDB

                """)

                self.log_message("Tabla 'categorias' creada")

                

                # Crear tabla pedidos (después de clientes y productos)

                cursor.execute("""

                CREATE TABLE IF NOT EXISTS `pedidos` (

                    `Identificador` INT NOT NULL AUTO_INCREMENT,

                    `fecha` DATE NOT NULL,

                    `clientes_id` INT NOT NULL,

                    `productos_id` INT NOT NULL,

                    PRIMARY KEY (`Identificador`)
                ) ENGINE = InnoDB

                """)

                self.log_message("Tabla 'pedidos' creada")

                

                connection.commit()

                messagebox.showinfo("Éxito", "Base de datos y tablas creadas correctamente")

                

        except Error as e:

            self.log_message(f"Error: {e}")

            messagebox.showerror("Error", f"Ocurrió un error: {e}")

        finally:

            if 'connection' in locals() and connection.is_connected():

                cursor.close()

                connection.close()

                self.log_message("Conexión MySQL cerrada")



if __name__ == "__main__":

    root = tk.Tk()

    app = DatabaseCreatorApp(root)

    root.mainloop()