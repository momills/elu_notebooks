# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:41:47 2019

@author: momills

#LOADING DATA FOR MY ASSIGNMENT
"""
import json



students_dict = {'MDS1901001':{
                'Name':'Michael Odartei Mills',
                'Degree': 'Master of Data Science',
                'StartYear': '2019',
                'Courses':{
                    'Alper Utku':['Leadership 1', 'Leadership 2'],
                    'Ricardo Periera':['Intro to Jupyter Notebook', 'Advanced Python', 'Python for Data Science']}
                },
                'MCS1802001':{
                'Name':'Kwame Nyamekye Jnr',
                'Degree': 'Master of Cyber Security',
                'StartYear': '2018',
                'Courses':{
                    'Alper Utku':['Leadership 1', 'Team Management'],
                    'John Snow':['Intro to Hacking', 'Intrusion Prevention and Detection', 'White Hacking'],
                    'Simon Matthews':['Cyber Law 1', 'Cyber Law 2', 'IP Laws']}
                },
                'MDS1901002':{
                'Name':'McAndrew Saad',
                'Degree': 'Master of Data Science',
                'StartYear': '2019',
                'Courses':{
                    'Alper Utku':['Leadership 1', 'Leadership 2'],
                    'Ricardo Periera':['Intro to Jupyter Notebook', 'Advanced Python', 'Python for Data Science']}
                }
   }







# students_dict = {
#                     '201901001': ['Michael Odartei Mills', 
#                               'Master of Data Science', 
#                               2019, 
#                               {'Alper Utku':['Leadership 1', 'Leadership 2'], 
#                                 'Ricardo Periera':['Intro to Jupyter Notebook', 'Advanced Python', 'Python for Data Science']}],
                    
#                     '201902001': ['Kwame Nyamekye Jnr', 
#                               'Post Grad Dip. in Cyber Security', 
#                               2018, 
#                               {'Alper Utku':['Leadership 1'],
#                                'John Snow': ['Intrusion Detection', 'Hacking Principles'],
#                                 'Simon Johnson':['Cyber Law 1', 'Cyber Law 2', 'Fundamentals of IP Law']}],
#                     '201901003': ['McAndrew Saad', 
#                               'Master of Data Science', 
#                               2019, 
#                               {'Alper Utku':['Leadership 1', 'Leadership 2'], 
#                                 'Ricardo Periera':['Intro to Jupyter Notebook', 'Advanced Python', 'Python for Data Science']}],
#                     '201901004': ['Omar Zayed', 
#                               'Master of Data Science', 
#                               2019, 
#                               {'Alper Utku':['Leadership 1', 'Leadership 2'], 
#                                 'Ricardo Periera':['Intro to Jupyter Notebook', 'Advanced Python', 'Python for Data Science']}],
#                     '201901005': ['Mohammed Hakkim', 
#                               'Master of Data Science', 
#                               2019, 
#                               {'Alper Utku':['Leadership 1', 'Leadership 2'], 
#                                 'Ricardo Periera':['Intro to Jupyter Notebook', 'Advanced Python', 'Python for Data Science']}]
#                     }




with open('student_json.json', 'w', encoding='utf-8') as f:
  json.dump(student_dict, f, ensure_ascii=False, indent=4, sort_keys=True)


