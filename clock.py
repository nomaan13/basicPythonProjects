from tkinter import*
from tkinter.ttk import*

from time import strftime


root=Tk()
root.title("Digital Clock")
def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(100,time)
    
label=Label(root,font=("ds-digital",50),background="black",foreground="green")
label.pack(anchor='center')
time()

mainloop()


