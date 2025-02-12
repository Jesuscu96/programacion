# Ejercicio 2: Operaciones con números
# Crea un módulo operaciones.py que contenga las siguientes funciones:
# • calcular_promedio(lista): Calcula la media de una lista de números.
# • calcular_maximo(lista): Encuentra el valor máximo en la lista.
# • calcular_minimo(lista): Encuentra el valor mínimo en la lista.
# Crea otro módulo generador_numeros.py que tenga una función:
# • generar_numeros(cantidad, minimo, maximo) que devuelva una lista de números aleatorios
#   entre un rango.
# En main.py, importa ambos módulos y:
# • Genera una lista de números aleatorios.
# • Usa las funciones del módulo operaciones.py para calcular y mostrar el promedio, el valor
#   máximo y el mínimo.

main = __name__

import operaciones
import generador_numeros

cantidad=int(input("ingresa la cantidad que desees: "))
maximo=int(input("ingresa el numero maximo: "))
minimo=int(input("ingresa el numero minimo: "))
numerosAlt=[generador_numeros.generar_numeros(maximo,minimo,cantidad)]
media=operaciones.pormedio(numerosAlt)
max=operaciones.maximo(numerosAlt)
min=operaciones.minimo(numerosAlt)
print(numerosAlt)
print(media)
print(min)
print(max)
