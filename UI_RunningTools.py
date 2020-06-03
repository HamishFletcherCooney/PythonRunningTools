from tkinter import *
from datetime import timedelta

root = Tk()
root.title('Running tools')
root.iconbitmap(r"C:\Users\Owner\Documents\GitHub\PythonRunningTools\runner.ico")

"""Program will create a window.
Ask user for an existing race performance then use physiological formulas to calculate an equivalent performance for a 
target distance. Split into 3 functions: The users inputs; The layout of the inputs; The calculation using the Riegel 
Formula"""

#defines all variables given by user: previous distance & time. Target distance.
def userinput():
    #CompletedDistanceEntry
    global ecd
    ecd = Entry(root, width=10, borderwidth=5)
    ecd.insert(0, "4") #4km in 13m50s is a recent race of mine, using as test, got bored of typing it in.

    #CompletedDistanceUnit
    global u1
    u1 = StringVar()
    u1.set("km")
    global cunit
    cunit = OptionMenu(root, u1, "km","Miles","Meters")

    #CompletedDistanceTime
    global ecth
    ecth = Entry(root,width=10,borderwidth=5) #hours
    ecth.insert(0, "0") #will be h
    global ectm
    ectm = Entry(root,width=10,borderwidth=5) #minutes
    ectm.insert(0, "13") #will be mm
    global ects
    ects= Entry(root,width=10,borderwidth=5) #seconds
    ects.insert(0, "50") #will be ss

    #TargetDistanceEntry
    global etd
    etd = Entry(root,width=10,borderwidth=5)
    etd.insert(0, "TargetDistance")

    #TargetDistanceUnit
    global u2
    u2= StringVar()
    u2.set("km")
    global tunit
    tunit = OptionMenu(root, u2, "km","Miles","Meters")

userinput()

#Layout of inputs
def interface():
    myLabel_1 = Label(root, text="Recent race result")
    myLabel_1.grid(row=0,columnspan=3)

    myLabel_2 = Label(root, text="Distance")
    myLabel_2.grid(row=1,column=0)
    ecd.grid(row=1,column=1)
    cunit.grid(row=1,column=2)

    ecth.grid(row=2,column=0)
    ectm.grid(row=2,column=1)
    ects.grid(row=2,column=2)

    myLabel_1 = Label(root, text="Target Race")
    myLabel_1.grid(row=3,columnspan=3)

    myLabel_2 = Label(root, text="Distance")
    myLabel_2.grid(row=4, column=0)
    etd.grid(row=4,column=1)
    tunit.grid(row=4,column=2)

interface()

#defining calculate button - creates the target time result - 'prints' summary
def button_calculate():
    completed_distance = ecd.get()
    global c_dist
    c_dist = float(completed_distance)
    global c_time
    c_time = int(ecth.get()) * 3600 + int(ectm.get()) * 60 + int(ects.get())
    global t_dist
    target_distance = etd.get()
    t_dist = float(target_distance)
    global t_time
    t_time = 0

    # Converting all distances to km
    if u1.get() == "Miles":
        c_dist = c_dist * 1.60934
    if u1.get() == "Meters":
        c_dist = c_dist / 1000
    if u2.get() == "Miles":
        t_dist = t_dist * 1.60934
    if u2.get() == "Meters":
        t_dist = t_dist / 1000

    t_time=c_time*(t_dist/c_dist)**1.06 #Formula to equate race times for different distances

#Output
    myLabel_6 = Label(root, text="Completed distance: " + str(c_dist) + " km")
    myLabel_6.grid(row=5,columnspan=3)
    myLabel_7 = Label(root, text=timedelta(seconds=int(c_time)))
    myLabel_7.grid(row=6,columnspan=3)
    myLabel_8 = Label(root, text="Target distance: " +str(t_dist) + " km")
    myLabel_8.grid(row=7,columnspan=3)
    myLabel_9 = Label(root, text=timedelta(seconds=int(t_time)))
    myLabel_9.grid(row=8,columnspan=3)

Button_calculate = Button(root,text="Calculate equivalent time", command=button_calculate).grid(row=9,columnspan=3)

root.mainloop()
