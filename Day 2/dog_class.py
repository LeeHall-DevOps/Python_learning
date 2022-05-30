class Dog:

# __ dundar

    def __init__(self, name, colour):
        self.animal_kind = "canine"
        self.name = name
        self.color = colour
        self.bark()

    def bark(self):  # method, not a function
        return "woof"

fido = Dog("fido", "brown")
print(fido.name)
# print(fido.color)
# print(fido.bark())