class Student:
  def __init__(self, name, age):
    self.__name = name
    self.age = age

  def get_name(self):
      return self.__name
  
  def set_name(self, name):
      self.__name = name
    
std1 = Student("ahmed", 20)
print(std1.age)
