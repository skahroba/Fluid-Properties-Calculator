# import CoolProp.CoolProp as CP
from Tkinter import *
#
# fields = ('Fluid Name', 'Pressure [Bar]', 'Temperature [C]',
#           'Density [kg/m3]', 'Viscosity [cP]', 'Compressibility [1/bar]')
#
# def fluid_properties(entries):
#    flu   = entries['Fluid Name'].get()
#    press = float(entries['Pressure [Bar]'].get()) * 1e5
#    temp  = float(entries['Temperature [C]'].get()) + 273.15
#
#    dens = CP.PropsSI("D", "T", temp, "P", press, flu)
#    visc = CP.PropsSI("V", "T", temp, "P", press, flu) * 1000
#    comp = CP.PropsSI("ISOTHERMAL_COMPRESSIBILITY", "T", temp, "P", press, flu) * 1e5
#
#    # print(visc)
#    # dens = ("%8.2f" % dens).strip()
#    # visc = ("%8.2f" % visc).strip()
#
#    entries['Density [kg/m3]'].delete(0,END)
#    entries['Density [kg/m3]'].insert(0, dens)
#    print("Density: %f" % float(dens))
#
#    entries['Viscosity [cP]'].delete(0, END)
#    entries['Viscosity [cP]'].insert(0, visc)
#    print("Viscosity: %f" % float(visc))
#
#    entries['Compressibility [1/bar]'].delete(0, END)
#    entries['Compressibility [1/bar]'].insert(0, comp)
#    print("Compressibility: %f" % float(comp))
#
# def makeform(root, fields):
#    entries = {}
#    for field in fields:
#       row = Frame(root)
#       lab = Label(row, width=22, text=field+": ", anchor='w')
#       ent = Entry(row)
#       ent.insert(0,"0")
#       row.pack(side=TOP, fill=X, padx=5, pady=5)
#       lab.pack(side=LEFT)
#       ent.pack(side=RIGHT, expand=YES, fill=X)
#       entries[field] = ent
#    return entries
#
# if __name__ == '__main__':
#    root = Tk()
#    ents = makeform(root, fields)
#    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
#    # b1 = Button(root, text='Final Balance',
#    #        command=(lambda e=ents: final_balance(e)))
#    # b1.pack(side=LEFT, padx=5, pady=5)
#    b2 = Button(root, text='Calculate',
#           command=(lambda e=ents: fluid_properties(e)))
#    b2.pack(side=LEFT, padx=5, pady=5)
#    b3 = Button(root, text='Quit', command=root.quit)
#    b3.pack(side=LEFT, padx=5, pady=5)
#    root.mainloop()
#
# # variable = StringVar(master)
# # variable.set("one") # default value
# #
# # w = OptionMenu(master, variable, "one", "two", "three")
# # w.pack()
import Tkinter as tk
# import tkinter as tk
from Tkinter import simpledialog


win = tk.Tk()
win.geometry("100x50")

def take_user_input_for_something():
    user_input = simpledialog.askstring("Pop up for user input!", "What do you want to ask the user to input here?")
    if user_input != "":
        print(user_input)

menubar = tk.Menu(win)
dropDown = tk.Menu(menubar, tearoff = 0)
dropDown.add_command(label = "Do something", command = take_user_input_for_something)

# this entry field is not really needed her.
# however I noticed you did not define this widget correctly
# so I put this in to give you an example.
my_entry = tk.Entry(win)
my_entry.pack()

menubar.add_cascade(label = "Drop Down", menu = dropDown)
win.config(menu = menubar)

win.mainloop()