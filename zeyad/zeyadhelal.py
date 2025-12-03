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

class Person:
    def __init__(self, age):
        self.__age = age
        self.age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def get_all_info(self):
        return [self.__age, self.age]


age2= Person(21)
print(age2.get_age())