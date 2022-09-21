"""
Name: Thararat Sakweth
ID: 364211760011
Group: MIT221
"""

class Student:
    def __init__(self,name,id):
        #attributes
        self.name = name
        self.id = id
    def __str__(self):
        print(f'Name: {self.name} ID: {self.id}')