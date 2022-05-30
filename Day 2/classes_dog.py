class Dog:

    animal_kind = "canine" # class variable which returns an attribute of String

    # self means i'm refering this class

    def bark(self): # method, not a function
        return "woof"
# print(Dog.animal_kind)
# print(Dog.bark())

fido = Dog()
lassie = Dog()
rex = Dog()
daisy = Dog()
tom = Dog()


# print(type(fido))
# print(type(lassie))
# print(fido.animal_kind)
# print(lassie.animal_kind)
# print(fido.bark())
# print(lassie.bark())
