from vehicle import Vehicle
from engine import Engine

class Car(Vehicle, Engine):
    def __init__(self, weight=1000, started=False, fuel=6, fuel_consumption=5, engine=Engine()):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine=engine

    def set_engine(self):
        self.engine = Engine()

vag=Car()
print(vag.engine)

