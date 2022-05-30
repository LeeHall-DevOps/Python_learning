class BankingApp:

    def __init__(self, money_in):
        self.money_in = money_in

    def __str__(self):
        return f"You paid in £{self.money_in}"

    def __format__(self, format_spec):
        if format_spec == "money":
            return f"You paid in £{self.money_in: .2f}"
        else:
            return self.__str__()

customer_1 = BankingApp(100000)

print(f"{customer_1}")
print(f"{customer_1:money}")