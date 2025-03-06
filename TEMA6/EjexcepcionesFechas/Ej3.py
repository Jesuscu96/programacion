from datetime import datetime
import os
class FechaPasadaError(Exception): #Clase de excepción propia
def __init__(self, mensaje="Fecha Incorrecta"):
super().__init__(mensaje) = mensaje
def agregar_tarea():
try:
nombre = input("Introduce tarea: ")
fecha_str = input("Introduce la fecha de vencimiento (DD-MM-YYYY): ")
fecha_vencimiento = datetime.strptime(fecha_str, "%d-%m-%Y").date()
if fecha_vencimiento < datetime.today().date():
raise FechaPasadaError("La fecha ingresada es anterior. Intenta con una fecha futura.")
with open("tareas.txt", "a") as archivo: #abre fichero en modo añadir
archivo.write(f"Tarea: {nombre} - Fecha límite: {fecha_str}\n")
print("Tarea agregada!")
except FechaPasadaError as e:
print(f"Error: {e}")
except ValueError:
print("Error: Formato de fecha incorrecto. Usa DD-MM-YYYY.")
except Exception as e:
print(f"Error inesperado: {e}")
def mostrar_tareas():
try:
if not os.path.exists("tareas.txt"): #pregunta si existe el fichero
print("No hay tareas registradas.")
return
with open("tareas.txt", "r") as archivo: #abre fichero en modo lectura
tareas = archivo.readlines() #crea una lista con las líneas del fichero
if not tareas:
print("No hay tareas registradas.")
else:
print("Tareas pendientes:")
for tarea in tareas:
print(tarea)
except Exception as e:
print(f"Error al leer el archivo: {e}")
def borrar_tareas_expiradas():
try:
if not os.path.exists("tareas.txt"):
print("No hay tareas registradas para eliminar.")
return
with open("tareas.txt", "r") as archivo: #abre fichero en modo lectura
tareas = archivo.readlines() #crea una lista con las líneas del fichero
hoy = datetime.today().date()
tareas_actualizadas = []
for tarea in tareas:
try:
nombre, fecha_str = tarea.strip().split(" - Fecha límite: ")
fecha_vencimiento = datetime.strptime(fecha_str, "%d-%m-%Y").date()
if fecha_vencimiento >= hoy: #si la fecha de vencimiento de la tarea es mayor se añade a la lista
tareas_actualizadas.append(tarea)
except ValueError:
print(f"Error procesando tarea: {tarea.strip()}")
with open("tareas.txt", "w") as archivo: #abre fichero en modo escritura (sobreescribe el fichero completo
for tarea in tareas_actualizadas: #recorre la lista de tareas_actualizadas, no están las anteriores a hoy
archivo.write(tarea)
print("Tareas vencidas eliminadas correctamente.")
except Exception as e:
print(f"Error al borrar tareas vencidas: {e}")
def menu():
while True:
print("Menú")
print("1. Agregar tarea")
print("2. Mostrar tareas")
print("3. Borrar tareas vencidas")
print("4. Salir")
opcion = input("Elige una opción: ")
match opcion:
case "1":
agregar_tarea()
case "2":
mostrar_tareas()
case "3":
borrar_tareas_expiradas()
case "4":
print("Saliendo")
break
case _:
print("Opción inválida. Intentalo de nuevo.")
# Comienza a ejecutar
menu()