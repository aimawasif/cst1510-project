class Person:
    def __init__(self,name,gender,age,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
    def personDetails(self):
        print(f'Name:{self.name} Age :{self.age} Address :{self.address}')

class Student(Person):
     #course, misis no, academic_year
     def __init__(self, name,gender,age,address,course,misis no,academic_year):
         super()__init__(name,gender,age,address)
         self.course= course
         self.misis= misis
         self.ay = academic_year

    
    

