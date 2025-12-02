class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age =  age
        
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
        
    def get_all_info(self):
        return[self.__name, self.__age]
        
std1 = Student("sara", 20)    
std_name = std1.get_name
print(std_name())
std1.set_name("sara elshamy")
print(std_name())
std2_age = std1.get_age
print(std2_age())
std1.set_age(23)
print(std2_age())
print(std1.get_all_info())
