from vehicle import Vehicle
from engine import Engine

class Car(Vehicle):

    def __int__(self, engine):
        self.engine=engine

    def set_engine(self):
        self.engine=Engine()
