from tkinter import *

root = Tk()
root.title('Running tools')
root.iconbitmap('C:/Users/Owner/Documents/Learning Python/Running tools/runner.ico')

#EntryWidget
e = Entry(root,width=50,borderwidth=5)
#width,bg,fg,borderwidth,32:00
e.pack()
e.insert(0, "Some default text")

#Drop down box

def show():
    myLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("km")

drop = OptionMenu(root, clicked, "km","Miles","Meters")
drop.pack()

myButton = Button(root,text="Calculate equivalent times", command=show).pack()

#Creating a label widget
mylabel1 = Label(root, text="Hello World!")
mylabel2 = Label(root, text="My Name is Hamish Fletcher-Cooney")

def myClick():
    thepoint= e.get() + " pointless"
    myLabel=Label(root, text=thepoint)
    myLabel.pack()

myButton = Button(root, text="Pointless Button", command=myClick,)
#padx pady is sizing
#fg bg colours 27:50 hex codes or colour names

#Shoving it onto the screen
mylabel1.pack()
mylabel2.pack()

root.mainloop()