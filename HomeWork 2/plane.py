from vehicle import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, cargo=100, max_cargo=1500):
        super().__init__()
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self):
        if self.max_cargo >= self.cargo + self.weight:
            self.weight = self.weight + self.cargo
        else:
            raise CargoOverload
        #print(self.weight)

    def remove_all_cargo(self):
        tmp = self.cargo
        self.cargo = 0
        return tmp

samolet = Plane()
samolet.load_cargo()
samolet.remove_all_cargo()
#print(samolet.remove_all_cargo())