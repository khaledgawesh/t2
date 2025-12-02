# Encapsulation
class Student():
    def __init__(self, name, age, gender):
        self.__name = name      # private
        self.__age = age        # private
        self._gender = gender   # protected
        #public : age , name , gender

    # Getter name
    def get_name(self):
        return self.__name

    # Setter name
    def set_name(self, name):
        self.__name = name

    # Getter age
    def get_age(self):
        return self.__age

    # Setter age
    def set_age(self, age):
        self.__age = age
        
    #get all info
    def get_all_info(self):
        return self.__name,self.__age
    
    #set all info
    def set_all_info(self,name,age):
        self.__name = name
        self.__age = age
        

std1 = Student("rana", 20, "female")

print(std1.get_name())  # rana
print(std1.get_age())   # 20

std1.set_name("rana mohamed")
std1.set_age(21)

print(std1.get_name())  # rana mohamed
print(std1.get_age())   # 21

std2 = Student("mono",3,"male")

print(std2.get_all_info())
std2.set_all_info("mono",4)
print(std2.get_all_info())

