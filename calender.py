from cProfile import label
from tkinter import * 
import calendar

text= calendar.calendar(2022)
root=Tk()
root.geometry("500x600")
root.title("calender")
label1=Label(root,text="CALENDAR!",bg='blue',font= ("times",28,'bold'))
label1.grid(row=1,column=1)
root.config(background="white")
l1=Label(root,text=text,font="consolas 8 bold")
l1.grid(row=2,column=1,padx=20)
root.mainloop()
