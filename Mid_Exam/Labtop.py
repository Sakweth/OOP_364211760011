"""
Name: Thararat Sakweth
ID: 364211760011
Group: MIT221
"""
class Labtop:
    #class attribute
    my_labtop = []

    def __init__(self,No,Brand,Model,CPU,RAM,Display,Storage,Price):
        self.No = No
        self.Brand = Brand
        self.Model = Model
        self.CPU = CPU
        self.RAM = RAM
        self.Display = Display
        self.Storage = Storage
        self.Price = Price
        self.my_labtop.append(self)

    def display_labtop(self):
        print(f'No:{self.No} '
              f'Brand:{self.Brand} '
              f'Model:{self.Model} '
              f'CPU:{self.CPU} '
              f'RAM:{self.RAM}'
              f'Display:{self.Display} '
              f'Storage:{self.Storage} '
              f'Price:{self.Price}')

