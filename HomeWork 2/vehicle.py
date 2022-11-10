from exceptions import LowFuelError, NotEnoughFuelError


class Vehicle:
    def __init__(self, weight=1000, started=0, fuel=6, fuel_consumption=5):
        self.weight = weight
        self.started= started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
            if self.started==False:
                if self.fuel>0:
                    self.started = True
            else:
                raise LowFuelError
            #print(self.started)

    def move(self, distance=1):
        #self.distance=distance
        if self.fuel >= self.fuel_consumption*distance:
            self.fuel = self.fuel-self.fuel_consumption
        else:
            raise NotEnoughFuelError
        #print(self.fuel)

drandulet=Vehicle()
drandulet.start()
drandulet.move()
