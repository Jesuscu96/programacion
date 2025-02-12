# Ejercicio3
# ADSLZone desea gestionar todos los usuarios de la web (tanto zoneros, como miembros del staff) los
# programadores de la página se reunieron para decidir como tenía que hacerse esta gestión y llegaron
# todos al siguiente consenso:
# Todos los miembros son usuarios
# Los usuarios tendrán los siguientes atributos privados
# 1. Un entero que indica cuántos mensajes lleva.
# 2. Un texto que contiene el correo electrónico.
# 3. Un texto que contiene el nombre(nick) en el foro.
# Los usuarios tienen los siguientes métodos:
# 1. Incrementa en 1 el número de mensajes.
# 2. Decremento en 1 el número de mensajes.
# 3. Modifica el correo electrónico.
# Los programadores de AdslZone, quieren que haya dentro de los usuarios dos clases: moderadores y
# administradores.
# Los moderadores tienen los siguientes atributos privados:
# 1. Un entero que indica cuántos mensajes lleva.
# 2. Un texto que contiene el correo electrónico.
# 3. Un texto que contiene el nombre(nick) en el foro.
# 4. Un entero que indica el número de mensajes que ha mandado a la papelera.
# Los moderadores tienen los siguientes métodos:
# 1. Incrementa en 1 el número de mensajes
# 2. Decremento en 1 el número de mensajes
# 3. Modifica el correo electrónico
# 4. Incrementa en 1 el número de mensajes que ha mandado a la papelera por incumplir las
# normas
# Los administradores tienen los siguientes atributos privados:
# 1. Un entero que indica cuántos mensajes lleva.
# 2. Un texto que contiene el correo electrónico.
# 3. Un texto que contiene el nombre(nick) en el foro.
# 4. Un entero que indica el número mensajes que han mandado a la papelera.
# 5. un entero que indico el número de baneos que ha realizado.
# Y tienen los siguientes métodos:
# 1. Incrementa en 1 el número de mensajes.
# 2. Decremento en 1 el número de mensajes.
# 3. Modifica el correo electrónico.
# 4. Cambia su propio nombre de usuario.
# 5. Incrementa en 1 el número de mensajes que ha mandado a la papelera por incumplir
# las normas.
# 6. Incrementa en 1 el número de baneos de usuarios por ser spammers.
# De aquí deducimos que tenemos una superclase clara, los usuarios, y después dos subclases, los
# moderadores y los administradores.
# Se nos pide, implementar las tres clases con sus respectivos métodos.
# Realiza además una clase que pruebe el funcionamiento de las tres clases generadas y una lista que
# almacene los objetos creados.

class Usuarios:
    def __init__(self, email, nombre):
        self.__email = email
        self.__nombre = nombre
        self.__mensajes = 0
    
    def incrimenta_mensajes(self):
        self.__mensajes += 1
    
    def decrimenta_mensajes(self):
        self.__mensajes -= 1

    def modifica_email(self):
        return f"Se ha modificado el correro"

class moderadores(Usuarios):
    