from Semaforo import Semaforo
#Constructor
semaforo = Semaforo("verde")

print(semaforo.mostrar_estado()) # El semáforo está en verde.
semaforo.color = "amarillo"
print(semaforo.mostrar_estado()) # El semáforo está en amarillo.
semaforo.color = "rojo"
print(semaforo.mostrar_estado()) # El semáforo está en rojo.
semaforo.color = "azul" # Esto genera un Error.
print(semaforo.mostrar_estado())
