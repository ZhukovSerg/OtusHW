from exceptions import LowFuelError, NotEnoughFuelError


class Vehicle:
    def __init__(self, weight=1000, started=False, fuel=6, fuel_consumption=5):
        self.weight = weight
        self.started= started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
            if not self.started:
                if self.fuel>0:
                    self.started = True
                else:
                    raise LowFuelError
            #print(self.started)

    def move(self, distance=100):
        #self.distance=distance
        if self.fuel >= (self.fuel_consumption*distance)/100:
            self.fuel -= (self.fuel_consumption*distance)/100
        else:
            raise NotEnoughFuelError
        #print(self.fuel)

drandulet=Vehicle()
drandulet.start()
drandulet.move()
