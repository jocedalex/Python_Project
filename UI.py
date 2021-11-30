import tkinter as tk                    
from tkinter import ttk
from Functions import *

#Update list functions
def update():#students
    studentsR=students_list()
    studentsReg.config(state='normal')
    studentsReg.delete('1.0','end')
    studentsReg.insert(1.0,studentsR)
    studentsReg.config(state='disabled')

def update2():#courses
    studentsR=students_list()
    studentsReg.config(state='normal')
    studentsReg.delete('1.0','end')
    studentsReg.insert(1.0,studentsR)
    studentsReg.config(state='disabled')
    


#---User interface basic config
screen=tk.Tk()
#screen.resizable(0,0)
screen.title("Es Latino OS")
screen.iconbitmap("resources/logo.ico")


#----Tabs creation


tabControl = ttk.Notebook(screen)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Sign Up')
tabControl.add(tab2, text ='Courses')
tabControl.add(tab3, text ='Link')
tabControl.pack(expand = 1, fill ="both")

#-----Add elements to register TAB----------------------------------

#text variables
nameR=tk.StringVar()
idR=tk.StringVar()
emailR=tk.StringVar()
phoneR=tk.StringVar()
studentsR=students_list()
  
ttk.Label(tab1, text ="Name:").grid(column = 0, 
                               row = 0,
                               padx = 10,
                               pady = 10)
nameReg=ttk.Entry(tab1, textvariable=nameR).grid(column = 1, 
                               row = 0,
                               padx = 10,
                               pady = 10)#Name

ttk.Label(tab1, 
          text ="Document:").grid(column = 2, 
                               row = 0,
                               padx = 10,
                               pady = 10)
idReg=ttk.Entry(tab1, textvariable=idR).grid(column = 3, 
                               row = 0,
                               padx = 10,
                               pady = 10)#ID

ttk.Label(tab1, text ="Email:").grid(column = 0,
                               row = 1,
                               padx = 10,
                               pady = 10)
emailReg=ttk.Entry(tab1, textvariable=emailR).grid(column = 1, 
                               row = 1,
                               padx = 10,
                               pady = 10)#Email

ttk.Label(tab1, text ="Phone #:").grid(column = 2,
                               row = 1,
                               padx = 10,
                               pady = 10)
phoneReg=ttk.Entry(tab1, textvariable=phoneR).grid(column = 3, 
                               row = 1,
                               padx = 10,
                               pady = 10)#Phone

button = ttk.Button(tab1,text="Register",command=lambda:add_student(nameR.get(),idR.get(),emailR.get(),phoneR.get())).grid( 
                               row = 2,
                               padx = 10,
                               pady = 10,columnspan=4)


#----------Data showing------

ttk.Label(tab1, text ="---Students list---").grid(column = 0,
                               row = 3,
                               columnspan = 4, 
                               padx = 10,
                               pady = 10)
studentsReg= tk.Text(tab1, width = 50, height= 15)
studentsReg.insert(1.0,studentsR)
studentsReg.config(state='disabled')
studentsReg.grid(column = 0, 
                 row = 4,
                 padx = 10,
                 pady = 10,
                 columnspan=4)#Students list

scrollBar = tk.Scrollbar(tab1, command=studentsReg.yview)
scrollBar.grid(column = 4, 
               row = 4,
               sticky="nsew")

buttonText = ttk.Button(tab1,text="Update",command=lambda:update()).grid( 
                               row = 5,
                               padx = 10,
                               pady = 10,columnspan=4)#List update




#..Reg variables for registration tab

#---Add elements to courses TAB------------------------------------

#text variables
nameC=tk.StringVar()
descriptionC=tk.StringVar()
classesC=tk.StringVar()
coursesR=courses_list()
  
ttk.Label(tab2, text ="Name:").grid(column = 0, 
                               row = 0,
                               padx = 10,
                               pady = 10)
nameC=ttk.Entry(tab2, textvariable=nameR).grid(column = 1, 
                               row = 0,
                               padx = 10,
                               pady = 10)#Name

ttk.Label(tab2, 
          text ="Description:").grid(column = 2, 
                               row = 0,
                               padx = 10,
                               pady = 10)
descriptionC=ttk.Entry(tab2, textvariable=idR).grid(column = 3, 
                               row = 0,
                               padx = 10,
                               pady = 10)#ID

ttk.Label(tab2, text ="Classes #:").grid(column = 0,
                               row = 1,
                               padx = 10,
                               pady = 10)
classesC=ttk.Entry(tab2, textvariable=emailR).grid(column = 1, 
                               row = 1,
                               padx = 10,
                               pady = 10)#Email



button = ttk.Button(tab2,text="Register",command=lambda:add_student(nameR.get(),idR.get(),emailR.get(),phoneR.get())).grid( 
                               row = 2,
                               padx = 10,
                               pady = 10,columnspan=4)

#----------Data showing------

ttk.Label(tab2, text ="---Courses list---").grid(column = 0,
                               row = 3,
                               columnspan = 4, 
                               padx = 10,
                               pady = 10)
coursesReg= tk.Text(tab2, width = 50, height= 15)
coursesReg.insert(1.0,coursesR)
coursesReg.config(state='disabled')
coursesReg.grid(column = 0, 
                 row = 4,
                 padx = 10,
                 pady = 10,
                 columnspan=4)#Students list

scrollBar2 = tk.Scrollbar(tab2, command=coursesReg.yview)
scrollBar2.grid(column = 4, 
               row = 4,
               sticky="nsew")

buttonText2 = ttk.Button(tab1,text="Update",command=lambda:update2()).grid( 
                               row = 5,
                               padx = 10,
                               pady = 10,columnspan=4)#List update


#---Add elements to Link TAB------------------------------------

ttk.Label(tab3,
          text ="Lets dive into the\
          world of computers").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)









screen.mainloop()
