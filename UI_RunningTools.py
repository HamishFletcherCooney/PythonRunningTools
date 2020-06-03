from tkinter import *
from datetime import timedelta

root = Tk()
root.title('Running tools')
root.iconbitmap(r"C:\Users\Owner\Documents\GitHub\PythonRunningTools\runner.ico")

"""Program will create a window.
Ask user for an existing race performance then use physiological formulas to calculate an equivalent performance for a 
target distance"""

myLabel_1 = Label(root, text="Recent race result")
myLabel_1.grid(row=0,columnspan=3)

myLabel_2 = Label(root, text="Distance")
myLabel_2.grid(row=1,column=0)

#CompletedDistanceEntry
ecd = Entry(root,width=10,borderwidth=5)
ecd.grid(row=1,column=1)
ecd.insert(0, "completed distance") #4km in 13m50s is a recent race of mine, using as test, got bored of typing it in.

#CompletedDistanceUnit
def show():
    myLabel = Label(root, text=u1.get()).pack()
u1 = StringVar()
u1.set("km")
drop = OptionMenu(root, u1, "km","Miles","Meters")
drop.grid(row=1,column=2)

#CompletedDistanceTime
ecth = Entry(root,width=10,borderwidth=5)
ecth.grid(row=2,column=0)
ecth.insert(0, "h")

ectm = Entry(root,width=10,borderwidth=5)
ectm.grid(row=2,column=1)
ectm.insert(0, "mm")

ects = Entry(root,width=10,borderwidth=5)
ects.grid(row=2,column=2)
ects.insert(0, "ss")

myLabel_1 = Label(root, text="Target Race")
myLabel_1.grid(row=3,columnspan=3)

#TargetDistanceEntry
etd = Entry(root,width=10,borderwidth=5)
etd.grid(row=4,column=1)
etd.insert(0, "target distance")

myLabel_2 = Label(root, text="Distance")
myLabel_2.grid(row=4,column=0)

#TargetDistanceUnit
def show():
    myLabel = Label(root, text=u2.get()).pack()
u2 = StringVar()
u2.set("km")
drop = OptionMenu(root, u2, "km","Miles","Meters")
drop.grid(row=4,column=2)

#defining calculate button - it creates the t_time result
def button_calculate():
    completed_distance = ecd.get()
    global c_dist
    c_dist = float(completed_distance)
    global c_time
    c_time = int(ecth.get())*3600 + int(ectm.get())*60 + int(ects.get())
    global t_dist
    target_distance = etd.get()
    t_dist = float(target_distance)
    global t_time
    t_time =0

#Converting all distances to km
    if u1.get() == "Miles":
        c_dist = c_dist*1.60934
    if u1.get() == "Meters":
        c_dist = c_dist/1000
    if u2.get() == "Miles":
        t_dist = t_dist * 1.60934
    if u2.get() == "Meters":
        t_dist = t_dist / 1000

    t_time=c_time*(t_dist/c_dist)**1.06 #Formula to equate race times for different distances

#Output
    myLabel_1 = Label(root, text="Completed distance: " + str(c_dist) + " km")
    myLabel_1.grid(row=5,columnspan=3)
    myLabel_3 = Label(root, text=timedelta(seconds=int(c_time)))
    myLabel_3.grid(row=6,columnspan=3)
    myLabel_4 = Label(root, text="Target distance: " +str(t_dist) + " km")
    myLabel_4.grid(row=7,columnspan=3)
    myLabel_6 = Label(root, text=timedelta(seconds=int(t_time)))
    myLabel_6.grid(row=8,columnspan=3)

Button_calculate = Button(root,text="Calculate equivalent time", command=button_calculate).grid(row=9,columnspan=3)

root.mainloop()
