from snake import Snake


class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large =True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("elephats taste good")

    def constrict(self):
        print("squeeze")

    def climb(self):
        print("up go up")

    def shed_skin(self):
        print("I'm growing out of my skin")

peter = Python()
peter.breath()