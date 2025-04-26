import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


conexion1 = mysql.connector.connect(

    host="localhost",

    user="root",

    password="bbdd",

    database="gestionempresarial"

)

cursor1=conexion1.cursor()



sql="insert into productos(nombre, descripcion, precio) values (%s,%s,%s)"

datos=("naranjas","naranjas de Valencia", 23.50)

cursor1.execute(sql, datos)

datos=("peras","peras de Zamora", 34)

cursor1.execute(sql, datos)

datos=("bananas","bananas de Brasil", 25)

cursor1.execute(sql, datos)

conexion1.commit()

conexion1.close()