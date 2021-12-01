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
            if 'students' in db.keys():
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

            if 'courses' in db.keys():
                for item in db['courses']:
                    valList=list(item.values())
                    for element in valList:
                       coursesR += str(element) + ' - '
                    coursesR += '\n\n'

                return coursesR
            else:
                return coursesR
                
    else:
        return coursesR

    
##-------------Add new students
def add_student(name,document,email,phone):
    if (checkExist('database.json')) == True:
        
        with open('database.json') as json_file:

            db = json.load(json_file)
            iD=0
            if 'students' in db.keys():
                for item in db['students']:
                    iD += 1
                
                data = {
                            'id':iD,
                            'name':name,
                            'document':document,
                            'email':email,
                            'phone':phone
                        }

            else:
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
def add_course(name,description,classes):
    if (checkExist('database.json')) == True:
        
        with open('database.json') as json_file:

            db = json.load(json_file)
            iD=0
            if 'courses' in db.keys():
                for item in db['courses']:
                    iD += 1
                
                data = {
                            'id':iD,
                            'name':name,
                            'document':description,
                            'email':classes,
                        }
            else:
                db['courses']=[]
            
                data = {
                            'id':0,
                            'name':name,
                            'document':description,
                            'email':classes,
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
                        'document':description,
                        'email':classes,
                    }
            db['courses'].append(data)
            
            with open('database.json','w') as json_file:
                json.dump(db, json_file)

#------Adding students to courses
def sign_up(name,course):
    if (checkExist('database.json')) == True:
        
        with open('database.json') as json_file:

            db = json.load(json_file)
            iD=0
            if 'link' in db.keys():
                for item in db['link']:
                    iD += 1
                
                data = {
                            'id':iD,
                            'name':name,
                            'course':course
                        }
            else:
                db['link']=[]
            
                data = {
                            'id':0,
                            'name':name,
                            'course':course
                        }

                
            db['link'].append(data)
            
            with open('database.json','w') as json_file:
                json.dump(db, json_file)
                
    else:
        
            db = {}
            db['link']=[]
            
            data = {
                        'id':0,
                        'name':name,
                        'course':course
                    }
            db['link'].append(data)
            
            with open('database.json','w') as json_file:
                json.dump(db, json_file)


#-----Courses' name list for dropdown menu----
def courses_listname():  
    coursesR=[]
    if (checkExist('database.json')) == True:
        with open('database.json') as json_file:
            db = json.load(json_file)

            if 'courses' in db.keys():
                for item in db['courses']:
                    coursesR.append(item['name'])
                    

                return coursesR
            else:
                return coursesR
                
    else:
        return coursesR

    
#-----Students' name list for dropdown menu----
def students_listname(): #Students list creation as a string
    studentsR=[]
    if (checkExist('database.json')) == True:
        with open('database.json') as json_file:
            db = json.load(json_file)
            if 'students' in db.keys():
                for item in db['students']:
                    studentsR.append(item['name'])

                return studentsR
            else:
                return studentsR
                
    else:
        return studentsR

#-------Students list for an specific course
def check_course(course): #Students list creation as a string
    studentsR=""
    if (checkExist('database.json')) == True:
        with open('database.json') as json_file:
            db = json.load(json_file)
            if 'link' in db.keys():
                for item in db['link']:
                    if item['course'] == course:
                        studentsR += str(item['name']) 
                        studentsR += '\n\n'

                return studentsR
            else:
                return studentsR
                
    else:
        return studentsR

print(check_course('Salsa'))
