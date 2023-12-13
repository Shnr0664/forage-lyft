from battery.battery import Battery
from engine.engine import Engine
from servicable import Servicable


class Car(Servicable):
    engine: Engine
    battery: Battery

    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False
