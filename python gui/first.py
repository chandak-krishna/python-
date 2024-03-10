import tkinter
from tkinter import *
#defining window 
m=tkinter.Tk()
m.title("first gui python program ")#title window 
m.iconbitmap('IMG_7218.JPG')#to add icon of the app
#resize the window 
m.geometry("750x500")
m.resizable(1,0)#1 allow to resize and 0 do not allow to resize 
m.config(bg='green')
#create wiget 
name_lable_1=tkinter.Label(m,text="krishna ")
name_lable_1.pack(padx=50,pady=50)
name_lable_2=tkinter.Label(m,text="krishna is my name  ")
name_lable_2.pack(padx=10,pady=10,anchor='w',fill='both')

# second window 
root=tkinter.Toplevel()
root.geometry('200x250+900+50')
# button and grid
name_button=tkinter.Button(root,text="enetr your name ")
name_button.grid(row=2,column=5)
name_button1=tkinter.Button(root,text="enetr ")
name_button1.grid(row=5,column=2)
#root window 
m.mainloop()