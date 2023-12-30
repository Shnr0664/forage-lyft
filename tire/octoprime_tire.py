from tire.tire import Tire
class OctoprimeTire(Tire):

    def __init__(self, tire_wear):
        self.wear = tire_wear

    def needs_service(self):
        wear_sum = 0
        for i in self.wear:
            wear_sum+=i
        if wear_sum >= 3:
            return True
        else:
            return False