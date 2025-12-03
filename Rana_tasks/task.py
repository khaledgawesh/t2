class Car():
    def __init__(self,speed):
        self.__speed = speed
        
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

c1 = Car(70)
print(c1.get_speed())
c1.set_speed(80)
print(c1.get_speed)
print(c1.get_speed())  
