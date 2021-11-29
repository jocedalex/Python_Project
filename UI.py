import tkinter as tk                    
from tkinter import ttk
from Functions import *


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

nameR=tk.StringVar()
idR=tk.StringVar()
emailR=tk.StringVar()
phoneR=tk.StringVar()
  
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

button = ttk.Button(tab1,text="Register",command=add_student(nameR.get(),idR.get(),emailR.get(),phoneR.get())).grid( 
                               row = 2,
                               padx = 10,
                               pady = 10,columnspan=4)

#..Reg variables for registration tab

#---Add elements to courses TAB------------------------------------

ttk.Label(tab2,
          text ="Lets dive into the\
          world of computers").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)


#---Add elements to Link TAB------------------------------------

ttk.Label(tab3,
          text ="Lets dive into the\
          world of computers").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)









screen.mainloop()
