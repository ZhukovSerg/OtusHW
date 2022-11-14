from vehicle import Vehicle
from engine import Engine


class Car(Vehicle, Engine):
    def __init__(self, weight=1000, started=False, fuel=6, fuel_consumption=5):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine=Engine()

    def set_engine(self, engine: Engine):
        self.engine = engine

vag=Car()
#print(vag.engine)

