"""
Name: Thararat Sakweth
ID: 364211760011
Group: MIT221
"""

class Labtop:
    def __init__(self,Brand,Model,CPU,RAM,Display,Storage,Price):
        #attributes
        self.__Brand  = Brand #private member
        self.__Model = Model  # private member
        self.__CPU = CPU  # private member
        self.__RAM = RAM  # private member
        self.__Display = Display  # private member
        self.__Storage = Storage  # private member
        self.__Price = Price  # private member

    #getter and setter
    def get_Brand(self):
        return self.__Brand
    def set_Brand(self,Brand):
        self.__Brand = Brand


    def get_Model(self):
        return self.__Model
    def set_Model(self,Model):
        self.__Model = Model


    def get_CPU(self):
        return self.__CPU
    def set_CPU(self,CPU):
        self.__CPU = CPU


    def get_RAM(self):
        return self.__RAM
    def set_RAM(self,RAM):
        self.__RAM = RAM


    def get_Display(self):
        return self.__Display
    def set_Display(self,Display):
        self.__Display = Display


    def get_Storage(self):
        return self.__Storage
    def set_Storage(self,Storage):
        self.__Storage = Storage


    def get_Price(self):
        return self.__Price
    def set_Price(self,Price):
        self.__Price = Price


    def __str__(self):
        print(f'Brand: {self.__Brand} '
              f'Model: {self.__Model} '
              f'CPU: {self.__CPU} '
              f'RAM: {self.__RAM}'
              f'Display: {self.__Display} '
              f'Storage: {self.__Storage} '
              f'Price: {self.__Price}')

Lab = Labtop("ASUS","Vivobook 15X","Intel Core i5-12500H","8","15.6","512","27,990")
Lab.__str__()
print("------------------------------------------------")
print(Lab.get_Brand())

Lab.set_Brand("Lenovo")
print(Lab.get_Brand())
print("------------------------------------------------")

print(Lab.get_Model())

Lab.set_Model("IdeaPad Gaming3")
print(Lab.get_Model())
print("------------------------------------------------")

print(Lab.get_CPU())

Lab.set_CPU("Intel Core i5-11320H")
print(Lab.get_CPU())
print("------------------------------------------------")
