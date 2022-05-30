# 1. list flights available owner/date/time/origin/destination


class Aircraft():
    def __init__(self):
        self.wing = True
        self.seat = True
        self.pilot = True
        self.own = ["RyanAir", "EasyJet", "BritAir", "JAirway"]
        self.date = ["27/05/22", "27/05/22","27/05/22","27/05/22"]
        self.time = ["09.00", "09.30", "10.00", "10.30"]
        self.o_from = ["Rome", "Paris", "London", "Tokyo"]
        self.to = ["Tokyo", "London", "Paris", "Rome"]

    def flight_one(self):
        return f"Flight:{self.own[0]}|Date:{self.date[0]}|Time:{self.time[0]}|From:{self.o_from[0]}|To:{self.to[0]}"

    def flight_two(self):
        return f"Flight:{self.own[1]}|Date:{self.date[1]}|Time:{self.time[1]}|From:{self.o_from[1]}|To:{self.to[1]}"

    def flight_three(self):
        return f"Flight:{self.own[2]}|Date:{self.date[2]}|Time:{self.time[2]}|From:{self.o_from[2]}|To:{self.to[2]}"

    def flight_four(self):
        return f"Flight:{self.own[3]}|Date:{self.date[3]}|Time:{self.time[3]}|From:{self.o_from[3]}|To:{self.to[3]}"


print(f"{Aircraft().flight_one()}\n{Aircraft().flight_two()}\n{Aircraft().flight_three()}\n{Aircraft().flight_four()}")


#dd =
    # Aircraft().depart_time()
    # Aircraft().origins()
    # Aircraft().destin()



