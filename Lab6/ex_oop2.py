"""
Name: Thararat Sakweth
ID: 364211760011
Group: MIT221
"""

class Student:
    #class attributes
    uni = "RUTS"

    def __init__(self,name,id,major):
        #object attributes
        self.name = name
        self.id = id
        self.major = major

    def introduce(self):
        print(f'My name is {self.name}, my id is {self.id},and I am studying in {self.major} major.')

s1 = Student("Thararat Sakweth","011","MIT221")
s1.introduce()

s2 = Student("Wichan Sakweth","0123","wc")
s2.introduce()

s1.major = "LM"
s1.introduce()

print(s1.uni)
print(s2.uni)

Student.uni = "PSU"
print(s1.uni)
print(s2.uni)