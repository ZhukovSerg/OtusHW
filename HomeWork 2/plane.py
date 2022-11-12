from vehicle import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight=1000, fuel=6, fuel_consumption=5, cargo=100, max_cargo=1500):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, pl_weight=1000):
        if self.max_cargo >= self.cargo + pl_weight:
            self.pl_weight = pl_weight + self.cargo
        else:
            raise CargoOverload
        print(self.pl_weight)

    def remove_all_cargo(self):
        tmp = self.cargo
        self.cargo = 0
        return tmp

samolet = Plane()
samolet.load_cargo()
samolet.remove_all_cargo()
#print(samolet.remove_all_cargo())