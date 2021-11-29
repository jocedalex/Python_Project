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

    
##-------------Add new students
def add_student(name,document,email,phone):
    if (checkExist('database.json')) == True:
        
        with open('database.json') as json_file:

            db = json.load(json_file)
            
            data = {
                        'name':name,
                        'id':document,
                        'email':email,
                        'phone':phone
                    }
            db['students'].append(data)
            
            with open('database.json','w') as json_file:
                json.dump(db, outfile)
                
    else:
        
            db = {}
            db['students']=[]
            
            data = {
                        'name':name,
                        'id':document,
                        'email':email,
                        'phone':phone
                    }
            db['students'].append(data)
            
            with open('database.json','w') as json_file:
                json.dump(db, json_file)

#----------Create new courses
def add_course(name,sessions,start,end,time):
    if (checkExist('database.json')) == True:
        
        with open('database.json') as json_file:

            db = json.load(json_file)
            
            data = {
                        'name':name,
                        'id':document,
                        'email':email,
                        'phone':phone
                    }
            db['courses'].append(data)
            
            with open('database.json','w') as json_file:
                json.dump(db, outfile)
                
    else:
        
            db = {}
            db['students']=[]
            
            data = {
                        'name':name,
                        'id':document,
                        'email':email,
                        'phone':phone
                    }
            db['students'].append(data)
            
            with open('database.json','w') as json_file:
                json.dump(db, outfile)  
