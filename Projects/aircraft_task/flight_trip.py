"""
1. list flights available date and time of origin departure and destination
2. list ticket sales - prices for adult or child
3. list passengers on flight
4. list passengers not on flight (first name, last name, passport number)
5. add new passenger to passport list
6. list
"""
from aircraft import Aircraft


class FlightTrip(Aircraft):
    def __init__(self):
        super().__init__()
        self.flights_available = "1"
        self.ticket_sales = "2"
        self.flight_passengers = "3"
        self.passengers_waiting = "4"
        self.add_passenger = "5"
        self.date_time_O_D = "6"


    def task_ui(self):
        print("1. flights available\n" 
                "2. list ticket sales\n" 
                "3. list passengers on flight\n" 
                "4. Waiting list\n" 
                "5. add new passenger\n" 
                "6. list date and time of origin departure and destination")
        first_choice = input("please enter option number").isdigit()

        if first_choice == "1":
            return print(f"{Aircraft().flight_one()}\n{Aircraft().flight_two()}\n{Aircraft().flight_three()}\n{Aircraft().flight_four()}")




FlightTrip().task_ui()
