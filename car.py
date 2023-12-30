from battery.battery import Battery
from engine.engine import Engine
from servicable import Servicable
from tire.tire import Tire


class Car(Servicable):
    engine: Engine
    battery: Battery
    tires: Tire

    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires =tires

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service():
            return True
        else:
            return False
