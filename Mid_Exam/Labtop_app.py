"""
Name: Thararat Sakweth
ID: 364211760011
Group: MIT221
"""
from Labtop import Labtop

# display
def display_labtop():
    if len(my_labtop) ==0:
        print("You had no labtop data.")
    else:
        print(f'You had {len(my_labtop)} following:')
        for x in my_labtop:
            x.display_labtop()
        print("\n")


# option
def display_option_system():
    select = 0
    print("Welcome to Loptop System")
    print("1.เพิ่มข้อมูล Laptop")
    print("2.แสดงข้อมูล Laptop")
    print("3.ออกจากระบบ")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_laptop_data()
    elif select == 2:
        display_labtop()
    elif select == 3:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")


# input data
def input_laptop_data():
    No = int(input("Enter laptop No: "))
    Brand = input("Enter laptop Brand: ")
    Model = input("Enter laptop Model: ")
    CPU = input("Enter laptop CPU: ")
    RAM = int(input("Enter laptop RAM(GB): "))
    Display = float(input("Enter laptop Display(inch): "))
    Storage = int(input("Enter laptop Storage(GB): "))
    Price = int(input("Enter laptop Price: "))


    my_labtop.append(Labtop(No,Brand,Model,CPU,RAM,Display,Storage,Price))
    print("\n---------------------------------------------------")
    print("Already add loptop to store.")
    print("\n---------------------------------------------------")

my_labtop = []
s = 0
while s == 0:
    display_option_system()