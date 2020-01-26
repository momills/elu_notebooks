# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:29:58 2019

@author: momills
"""


'''
Assignment Title: First Glance at Python Data Structures

Assignment steps: Step 1: Create a structure to store multiple students’ data 
using Python’s basic data structures. Make sure each student will have the following features:
    Name, ID, Degree, StartYear. Each student will have multiple courses taken from a 
    specific lecturer (e.g., each student can take N different courses from M different lecturer, 
    each of the information must be defined)

Step 2: Show the structure that you have designed in JSON format.

Step 3: Use the necessary library to load the JSON data from a JSON file to the Python 
environment. Submit the Python files of your codes as well as the JSON file.

Note: You can create the above dataset for 2-5 students (as example)
''' 

#STEP 1
# students_dict = {'ID':{
#                 'Name':'Student_Name',
#                 'Degree': 'Degree_Name',
#                 'StartYear': 'year',
#                 'Courses':{
#                     'Lecturer1_Name':['Course 1','Course 2' ...],
#                     'Lecturer2_Name':['Course 3'...]}
#                 }
#                 ....
#                 ....
#     }

students_dict = {'MDS1901001':{
                'Name':'Michael Odartei Mills',
                'Degree': 'Master of Data Science',
                'StartYear': '2019',
                'Courses':{
                    'Alper Utku':['Leadership 1', 'Leadership 2'],
                    'Ricardo Periera':['Intro to Jupyter Notebook', 
                                       'Advanced Python', 'Python for Data Science']}
                },
                'MCS1802001':{
                'Name':'Kwame Nyamekye Jnr',
                'Degree': 'Master of Cyber Security',
                'StartYear': '2018',
                'Courses':{
                    'Alper Utku':['Leadership 1', 'Team Management'],
                    'John Snow':['Intro to Hacking', 'Intrusion Prevention and Detection', 
                                 'White Hacking'],
                    'Simon Matthews':['Cyber Law 1', 'Cyber Law 2', 'IP Laws']}
                },
                'MDS1901002':{
                'Name':'McAndrew Saad',
                'Degree': 'Master of Data Science',
                'StartYear': '2019',
                'Courses':{
                    'Alper Utku':['Leadership 1', 'Leadership 2'],
                    'Ricardo Periera':['Intro to Jupyter Notebook', 'Advanced Python', 
                                       'Python for Data Science']}
                }
   }


#STEP2
#Kindly find the JSON file submitted 
import json

with open('M2_students_json.json', 'w') as f:
  json.dump(students_dict, f, indent=4, sort_keys=True)


#STEP3
# import json /as in STEP 2/
with open('M2_students_json.json', 'r') as f:
    loaded_students_dict = json.load(f)

# EXAMPLE: to print all ids and student names
print('All Students List:')
print('******************************* \n')
for std_id, student in loaded_students_dict.items():
    print(std_id, student['Name'])
print('\n *******************************')
print(f'TOTAL: {len(loaded_students_dict)} students. \n')
