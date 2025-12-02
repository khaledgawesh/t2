class Super:
    def __init__(self, age):
        self.__age = age
        self.age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def get_all_info(self):
        return [self.__age, self.age]


age2 = Super(20)
print(age2.get_age())
