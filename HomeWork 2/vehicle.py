from exceptions import LowFuelError, NotEnoughFuelError



class Vehicle:
    def __init__(self):
        self.weight = 1000
        self.started= 0
        self.fuel = 1
        self.fuel_consumption = 5

    def start(self):
        try:
            if self.fuel > 0:
                self.started = 1
            elif self.fuel <= 0:
                raise LowFuelError
        except LowFuelError:
            print("LowFuel")
        #print(self.started)

    def move(self):
        try:
            if self.fuel<self.fuel_consumption:
                raise NotEnoughFuelError
        except NotEnoughFuelError:
            print("NotEnoughFuel")
            if self.fuel!=self.fuel_consumption:
                self.fuel=self.fuel_consumption
            #print(self.fuel)

drandulet=Vehicle()
drandulet.start()
drandulet.move()
