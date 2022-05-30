class Aircraft:

    def __init__(self):
        self.engine = True
        self.wings = True
        self.pilot = True
        self.owner = ["RyanAir", "EasyJet", "BA", "JapanAir"]

    def craft_name(self):
        for own in self.owner:
          print(own)



craft = Aircraft().craft_name()



