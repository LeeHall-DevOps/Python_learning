from passanger import Passenger
from airplane import Airplane


class FlightTrip(Passenger, Airplane):
    def __init__(self):
        super().__init__()

    def flight_list(self):
        return f"{self.flight_one}\n{self.flight_two}\n{self.flight_three}"



#print(Passenger().list())
#print(Airplane().available_flights())
#print(Passenger().register())
#print(Passenger().p_list())
