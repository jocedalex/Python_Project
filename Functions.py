# import libraries
import json



#--------Check if the file already exist
def checkExist(file):
    try:
        with open(file, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def students_list(): #Students list creation as a string
    studentsR="ID - Name - Document - Email - Phone - \n\n"
    if (checkExist('database.json')) == True:
        with open('database.json') as json_file:
            db = json.load(json_file)
            if db['students']:
                for item in db['students']:
                    valList=list(item.values())
                    for element in valList:
                        studentsR += str(element) + ' - '
                    studentsR += '\n\n'

                return studentsR
            else:
                return studentsR
                
    else:
        return studentsR

def courses_list(): #Courses list creation as a string
    coursesR="ID - Name - Description - Classes - \n\n"
    if (checkExist('database.json')) == True:
        with open('database.json') as json_file:
            db = json.load(json_file)

            if db['courses']:
                for item in db['courses']:
                    valList=list(item.values())
                    for element in valList:
                        coursesR += str(element) + ' - '
                    coursesR += '\n\n'

                return coursesR
            else:
                return coursesR
                
    else:
        return studentsR

    
##-------------Add new students
def add_student(name,document,email,phone):
    if (checkExist('database.json')) == True:
        
        with open('database.json') as json_file:

            db = json.load(json_file)
            iD=0
            for item in db['students']:
                iD += 1
            
            data = {
                        'id':iD,
                        'name':name,
                        'document':document,
                        'email':email,
                        'phone':phone
                    }
            db['students'].append(data)
                 
            
            with open('database.json','w') as json_file:
                json.dump(db, json_file)
                
    else:
        
            db = {}
            db['students']=[]
            
            data = {
                        'id':0,
                        'name':name,
                        'document':document,
                        'email':email,
                        'phone':phone
                    }
            db['students'].append(data)
            
            with open('database.json','w') as json_file:
                json.dump(db, json_file)

##-------------Add new courses
def add_course(name,document,email,phone):
    if (checkExist('database.json')) == True:
        
        with open('database.json') as json_file:

            db = json.load(json_file)
            iD=0
            for item in db['students']:
                iD += 1
            
            data = {
                        'id':iD,
                        'name':name,
                        'document':document,
                        'email':email,
                        'phone':phone
                    }
            db['courses'].append(data)
            
            with open('database.json','w') as json_file:
                json.dump(db, json_file)
                
    else:
        
            db = {}
            db['courses']=[]
            
            data = {
                        'id':0,
                        'name':name,
                        'document':document,
                        'email':email,
                        'phone':phone
                    }
            db['courses'].append(data)
            
            with open('database.json','w') as json_file:
                json.dump(db, json_file) 
