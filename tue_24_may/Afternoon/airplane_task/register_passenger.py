class register_passenger:

    def __init__(self, ):
        self.first_name = f_name
        self.last_name = l_name
        self.new_passp_no = passp_no

    def add_to_p_list(self, f_name, l_name, passp_no):
        self.new_f_name = []
        self.new_l_name = []
        self.new_passp_no = []
        self.new_f_name.append(self.f_name)
        self.new_l_name.append(self.l_name)
        self.new_passp_no.append(self.passport_no)
        return self.new_f_name, self.new_l_name, self.new_passp_no


new_passenger = register_passenger().add_to_p_list()

print(new_passenger)