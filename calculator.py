import tkinter 
from  tkinter import *
from tkinter import font
from turtle import clear

from click import command

root =Tk()
root.title("CALCULATOR")
root.geometry("500x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

equation=" "

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation=""
    label_result.config(text=equation)
    
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="Error"
            equation=""
    label_result.config(text=result)
    


label_result=Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

Button(root,text="C",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=5,y=100)
Button(root,text="/",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("/")).place(x=135,y=100)
Button(root,text="%",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=260,y=100)
Button(root,text="*",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("*")).place(x=385,y=100) 

Button(root,text="7",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("7")).place(x=5,y=200)
Button(root,text="8",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=135,y=200)
Button(root,text="9",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=260,y=200)
Button(root,text="-",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=385,y=200) 

Button(root,text="4",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("4")).place(x=5,y=300)
Button(root,text="5",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=135,y=300)
Button(root,text="6",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=260,y=300)
Button(root,text="+",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=385,y=300) 

Button(root,text="1",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("1")).place(x=5,y=400)
Button(root,text="2",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=135,y=400)
Button(root,text="3",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=260,y=400)
Button(root,text=" = ",width=5,height=3,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda:calculate()).place(x=385,y=400) 

Button(root,text="0",width=12,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=3,y=500) 
Button(root,text=".",width=5,height=1,font=("arial",25, "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show(".")).place(x=260,y=500)
root.mainloop()


