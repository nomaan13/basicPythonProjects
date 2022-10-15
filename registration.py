from tkinter import*
from unicodedata import name
from winreg import SetValue

from pyparsing import col
root  = Tk()


root.geometry("500x300")
root["bg"] = "white"



def submit_value():
    print("your information have been saved successfuly")
    
    
Label(root,text="Registration form ", font="times 15 bold").grid(row=0,column=3)

name_user = Label(root,text="Student name")
name_user.grid(row=1,column=2)
branch_user = Label(root,text="Branch")
branch_user.grid(row=2,column=2) 
gender_user=Label(root, text="Gender")
gender_user.grid(row=3,column=2)
phone_user = Label(root, text="Contact number")
phone_user.grid(row=4,column=2)
country_user =Label(root,text="Country")
country_user.grid(row=5,column=2)


name_value=StringVar
branch_value=StringVar
gender_value=StringVar
phone_value=StringVar
country_value=StringVar
check_value = IntVar


name_box= Entry(root,textvariable=name_value)
name_box.grid(row=1,column=3)
branch_box = Entry(root,textvariable=branch_value)
branch_box.grid(row=2,column=3)
gender_box=Entry(root,textvariable=gender_user)
gender_box.grid(row=3,column=3)
phone_box=Entry(root,textvariable=phone_value)
phone_box.grid(row=4,column=3)
country_box = Entry(root,textvariable=country_value)
country_box.grid(row=5,column=3)

check_box =Checkbutton(text= "Remember me!! ",variable=check_value)
check_box.grid(row=6,column=3)

Button(text="Submit", command=submit_value).grid(row=7,column=3)









 








root.mainloop()