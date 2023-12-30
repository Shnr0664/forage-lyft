from tire.tire import Tire


class CarriganTire(Tire):

    def __init__(self, tire_wear):
        self.wear = tire_wear

    def needs_service(self):
        for i in self.wear:
            if i >= 0.9:
                return True
        return False
