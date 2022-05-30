class Car:
    def __init__(self, current_speed, max_speed):
        self.current_speed = current_speed
        self.max_speed = max_speed

    def get_current_speed(self):
        return self.current_speed

    def set_decrease_current_speed(self):
        if self.current_speed <= 0:
            self.current_speed == 0
            print("The car has stopped")
        else:
            self.current_speed -= 5

    def set_increase_current_speed(self):
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
            print("You are at top speed")
        else:
            self.current_speed += 5

ford = Car(30, 100)
print(ford.current_speed)
ford.set_increase_current_speed()
print(ford.current_speed)
ford.set_decrease_current_speed()
print(ford.current_speed)

