# Crea otro módulo generador_numeros.py que tenga una función:
# • generar_numeros(cantidad, minimo, maximo) que devuelva una lista de números aleatorios
#   entre un rango.
import random


def generar_numeros (cantidad=0, maximo=0, minimo=0):
   return [random.randint(maximo,minimo) for _ in range(cantidad)]