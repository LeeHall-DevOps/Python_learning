from aircraft import Aircraft
from datetime import date

class Airplane(Aircraft):

    def __init__(self):
        super().__init__()
        self.origin = ["London", "Rome", "L.A", "Tokyo"]
        self.destination = ["London", "Rome", "L.A", "Tokyo"]
        self.date = date.today()

    def route_one(self):
        return f"{Aircraft().craft_one()}: {self.origin[0]} to {self.destination[-1]} Date: {self.date}"

    def route_two(self):
        return f"{Aircraft().craft_two()}: {self.origin[1]} to {self.destination[-2]} Date: {self.date}"

    def route_three(self):
        return f"{Aircraft().craft_three()}: {self.origin[2]} to {self.destination[-3]} Date: {self.date}"

    def available_flights(self):
        flight_one = Airplane().route_one()
        flight_two = Airplane().route_two()
        flight_three = Airplane().route_three()
        available_flights = f"{flight_one}\n{flight_two}\n{flight_three}"
        return available_flights


#print(Airplane().available_flights())

