"""
Name: Thararat Sakweth
ID: 364211760011
Group: MIT221
"""

from model import Person,Student,Vaccine,Vaccine_Passport

p1 = Person("Thararat",22,50.0,169)

v1 = Vaccine("Sinopharm")
d1 = "10/7/2565"

vp1 = Vaccine_Passport(p1)

vp1.vaccine_passport_info()

vp1.add_vaccine(v1)
vp1.add_date(d1)

vp1.vaccine_passport_info()

v2 = Vaccine("Pfizer")
d2 = "10/8/2565"

vp1.add_vaccine(v2)
vp1.add_date(d2)

vp1.vaccine_passport_info()

# Student
s1 = Student("Wichan",49,80,170,"MIT")

v3 = Vaccine("Pfizer")
d3 = "11/8/2565"

vp2 = Vaccine_Passport(s1)
vp2.add_vaccine(v3)
vp2.add_date(d3)

vp2.vaccine_passport_info()
