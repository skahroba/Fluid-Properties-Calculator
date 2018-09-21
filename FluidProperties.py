import CoolProp.CoolProp as CP
from Tkinter import *
#
fields = ('Pressure [Bar]', 'Temperature [C]',
          'Density [kg/m3]', 'Molar density [mol/m3]',
          'Viscosity [cP]', 'Compressibility [1/bar]',
          'Thermal conductivity [W/m/K]')

def fluid_properties(entries):
   flu   = entries['Fluid'].get()
   press = float(entries['Pressure [Bar]'].get()) * 1e5
   temp  = float(entries['Temperature [C]'].get()) + 273.15


   dens = CP.PropsSI("D", "T", temp, "P", press, flu)
   visc = CP.PropsSI("V", "T", temp, "P", press, flu) * 1000
   comp = CP.PropsSI("ISOTHERMAL_COMPRESSIBILITY", "T", temp, "P", press, flu) * 1e5
   cond = CP.PropsSI("L", "T", temp, "P", press, flu)
   mold = CP.PropsSI("DMOLAR", "T", temp, "P", press, flu)

   entries['Density [kg/m3]'].delete(0,END)
   entries['Density [kg/m3]'].insert(0, dens)
   print("Density: %f" % float(dens))

   entries['Viscosity [cP]'].delete(0, END)
   entries['Viscosity [cP]'].insert(0, visc)
   print("Viscosity: %f" % float(visc))

   entries['Compressibility [1/bar]'].delete(0, END)
   entries['Compressibility [1/bar]'].insert(0, comp)
   print("Compressibility: %f" % float(comp))

   entries['Thermal conductivity [W/m/K]'].delete(0, END)
   entries['Thermal conductivity [W/m/K]'].insert(0, cond)
   print("Thermal conductivity [W/m/K]: %f" % float(cond))

   entries['Molar density [mol/m3]'].delete(0, END)
   entries['Molar density [mol/m3]'].insert(0, mold)
   print("Molar density [mol/m3]: %f" % float(mold))

def makeform(root, fields):
   entries = {}
   var = StringVar(root)
   var.set('FLUID NAME')
   choices = ['water','CarbonDioxide','CarbonMonoxide','Nitrogen','Air','Benzene',
              'n-Decane','CycloPropane',
              'Toluene','Xenon','CycloHexane',
              'Cyclopentane','Deuterium','DimethylEther',
              'Helium','Hydrogen','HydrogenChloride',
              'HydrogenSulfide','Methane', 'Methanol',
              'Propyne', 'n-Dodecane', 'n-Heptane',
              'n-Hexane','n-Nonane','n-Octane','n-Pentane',
              'n-Propane']
   choices = sorted(choices)
   option = OptionMenu(root, var, *choices)
   option.pack(side=TOP, fill = X , expand = YES, padx=5, pady=5)
   entries['Fluid'] = var
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=25, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries


if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))

   b2 = Button(root, text='Calculate',
          command=(lambda e=ents: fluid_properties(e)))
   b2.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(root, text='Quit', command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)
   root.title("Fluid Properties Calculator")
   root.mainloop()
