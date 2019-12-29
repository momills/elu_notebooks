'''
students = {'Name':{
                 'ID': int,
                 'Degree': string,
                 'StartYear': int,
                 'Courses':{'Lecturer1_Name':['Course 1','Course 2' ...],'Lecturer2_Name':['Course 3'...]}
                 }
                 ....
                 ....
     }
'''


students = {'Peter Smith':{
                "ID":101,
                'Degree': 'MSc Computer Science',
                'StartYear': 2019,
                'Courses':{'Dr Mark':['Algorithms', 'Intro to Network Security'],'Prof Stevens':['Embedded Systems', 'Advanced Programming']}
                },
                "Paul Jenkings":{
                'ID':401,
                'Degree': 'MA Polical Science',
                'StartYear': 2019,
                'Courses':{'Prof Salma':['Polical Psychology', 'People Psychology'],
                            'Prof Steven Barnes':['Intro to Polical Strategy', 'Governance 482'],'Dr Kwame Nyamekye':['Polical Systems of the World']}
                }
   }



import json
with open('kwame.json', 'r') as file:
    students_from_json = json.load(file)

print(students_from_json.keys())
