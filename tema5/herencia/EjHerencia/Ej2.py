class Abuelo:
    def m1(self):
        return 0
    def m2(self):
        print("Abuelo.m2")
    def m3(self):
        print("Abuelo.m3")
    def m4(self):
        print("Abuelo.m4")
class Padre(Abuelo):
    def m1(self):
        return 1
    def m2(self):
        super().m2()
        print("Padre.m2")
    def m4(self):
        super().m4()
        print("Padre.m4")
class Hijo(Padre):
    def m1(self):
        return super().m1()
    def m2(self):
        super().m2()
        print("Hijo.m2")
    def m3(self):
        super().m3()
        print("Hijo.m3")
# Prueba
if __name__ == "__main__":
    h = Hijo()
    print("\nm1 devuelve:", h.m1())
    print("\nm2:")
    h.m2()
    print("\nm3:")
    h.m3()
    print("\nm4:")
    h.m4()