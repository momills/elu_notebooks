# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 23:38:16 2020

@author: momills
"""


'''
Step 1: Write a class of “Person”, which is the parent class of Lecturer and Student. 
The Student and Lectures classes inherit from the Person class. In this class, the instance 
attributes should be number of legs, which should be initialised 2 and a 
boolean variable - is_alive, that should be initialised as True. 

Step 2: Write a class 'Student' which stores information about a student. 
The class must have the following instance attributes controlled by the user: Name, Grade, Number.

Step 3: Write a class which stores information about a “Lecturer”. 
The class must have the following instance attributes, also controlled by the user: Name, Number

In Step 2 and Step 3, both object should inherit the instance attributes from the Person object.

Hint: super().<name of the method you want to call from parent class>()
'''


#Parent Class: Person
class Person:
    
    def __init__(self):
        self.number_of_legs = 2
        self.is_alive = True
        
#SubClass: Student        
class Student(Person):
    
    def __init__(self, name, grade, number):
        super().__init__()
        self.name = name
        self.grade = grade
        self.number = number
    
#SubClass: Lecturer   
class Lecturer(Person):
    
    def __init__(self, name, number):
        super().__init__()
        self.name = name
        self.number = number
    
#**********************************************************
#EXAMPLE
    
#initialize a person, a student and a lecturer and accessing their attributes, including inherited ones
person = Person()
print('\n Parent Class')
print(f"I have {person.number_of_legs} legs so I'm alive: {person.is_alive}")
print('**************************************************\n')

student = Student('Michael', 'A', '20190001')
print('\n Student Class')
print(f'My name is {student.name}, grade {student.grade} student with ID {student.number}')
print(f"I inherited {student.number_of_legs} legs and {student.is_alive}'ly' alive from Person class")
print('**************************************************\n')

lecturer = Lecturer('Violeta', 'L001')
print('\n Lecturer Class')
print(f'My name is {lecturer.name} lecturer with ID {lecturer.number}')
print(f"I inherited {lecturer.number_of_legs} legs and {lecturer.is_alive}'ly' alive from Person class")
print('**************************************************\n')




