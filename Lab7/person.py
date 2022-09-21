"""
Name: Thararat Sakweth
ID: 364211760011
Group: MIT221
"""

class Person:
    def __init__(self,name,age):
        self._name = name #protected member
        self._age = age   #protected member
    def __str__(self):
        print(f'Name: {self._name} Age: {self._age}')

class Student(Person):
    def __init__(self,name,age,major,):
        self.major = major # public member
        Person.__init__(self,name,age)
    def __str__(self):
        print(f'Name: {self._name} Age: {self._age} Major: {self.major}')

#object Person
p = Person("Thararat",22)
p.__str__()

p._name = "Wichan"
p.__str__()

#object Student
s = Student("Pornsri",40,"MIT")
s.__str__()

s._name = "Pronprasert"
s.__str__()