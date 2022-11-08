from vehicle import Vehicle
from exceptions import CargoOverload


class Plane (Vehicle):

    cargo=100
    max_cargo=500

    def __int__(self):
        self.max_cargo=600

    def load_cargo(self):
        try:
            gruz = float(input("Введите массу груза:"))
            if gruz+self.cargo <= self.max_cargo:
                self.cargo=gruz+self.cargo
                print (self.cargo)
            elif gruz+self.cargo > self.max_cargo:
                raise CargoOverload
        except CargoOverload:
            print("CargoOverload")

    def remove_all_cargo(self):
        self.cargo=0
        self.cargo=Plane.cargo
        print(self.cargo)

samolet=Plane()
samolet.load_cargo()
samolet.remove_all_cargo()

