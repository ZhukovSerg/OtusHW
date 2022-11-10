from vehicle import Vehicle
from engine import Engine

class Car(Vehicle):

    def __init__(self, engine):
        super().__init__()
        self.engine=engine

    def set_engine(self, engine:Engine):
        self.engine=engine



