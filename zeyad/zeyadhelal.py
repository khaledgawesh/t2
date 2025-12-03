class Car:
    def __init__(self, speed):
        self.__speed = speed
        self.speed = speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def get_all_info(self):
        return [self.__speed, self.speed]


speed2= Car(90)
print(speed2.get_speed())