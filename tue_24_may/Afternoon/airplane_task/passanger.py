from airplane import Airplane


class Passenger(Airplane):
    def __init__(self):
        super().__init__()
        self.p_first_name = ["Robin", "Sarah", "David"]
        self.p_last_name = ["Hood", "Homes", "Atinbough"]
        self.p_passport_no = ["444", "002", "007"]

    def p_list(self):
        # need to loop through all p_lists to get each element
       # for i in
            for first in self.p_first_name:
                    print(first)
            for j in self.p_last_name:
                    print(j)
            for k in self.p_passport_no:
                    print(k)
            return f"{first} {j} {k} \n"


person = Passenger().p_list()
(person)


