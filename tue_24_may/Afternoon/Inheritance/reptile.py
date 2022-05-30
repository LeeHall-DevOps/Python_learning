from animal import Animal


class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("It's chilly out there")

    def hunt(self):
        print("Wait to ponce")

    def use_vernom(self):
        print("Im made with poison")

    def attract_mat_with_smell(self):
        print("smell me!")

jeremy = Reptile()
print(jeremy.hunt())