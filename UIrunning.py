from tkinter import *
from datetime import timedelta

root = Tk()
root.title('Running tools')
root.iconbitmap('C:/Users/Owner/Documents/Learning Python/Running tools/runner.ico')

#CompletedDistanceEntry
ecd = Entry(root,width=25,borderwidth=5) #width,bg,fg,borderwidth,32:00
ecd.pack()
ecd.insert(0, "4")

#CompletedDistanceUnit
def show():
    myLabel = Label(root, text=u1.get()).pack()
u1 = StringVar()
u1.set("km")
drop = OptionMenu(root, u1, "km","Miles","Meters")
drop.pack()

#CompletedDistanceTime
ecth = Entry(root,width=25,borderwidth=5)
ecth.pack()
ecth.insert(0, "0")

ectm = Entry(root,width=25,borderwidth=5)
ectm.pack()
ectm.insert(0, "13")

ects = Entry(root,width=25,borderwidth=5)
ects.pack()
ects.insert(0, "50")

#TargetDistanceEntry
etd = Entry(root,width=25,borderwidth=5)
etd.pack()
etd.insert(0, "5")

#TargetDistanceUnit
def show():
    myLabel = Label(root, text=u2.get()).pack()
u2 = StringVar()
u2.set("km")
drop = OptionMenu(root, u2, "km","Miles","Meters")
drop.pack()

#defining calculate button
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

    t_time=c_time*(t_dist/c_dist)**1.06
    #t_time=time(int(t_time))

#Testing I can call all variables and unit conversion is working
    myLabel_1 = Label(root, text="Completed distance: " + str(c_dist) + " km")
    myLabel_1.pack()
    myLabel_3 = Label(root, text=c_time)
    myLabel_3.pack()
    myLabel_4 = Label(root, text="Target distance: " +str(t_dist) + " km")
    myLabel_4.pack()
    myLabel_6 = Label(root, text=timedelta(seconds=int(t_time)))
    myLabel_6.pack()



Button_calculate = Button(root,text="Calculate equivalent times", command=button_calculate).pack()

root.mainloop()

