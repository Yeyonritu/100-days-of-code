from tkinter import *

def to_km():
    user_input = float(miles_input.get())
    conv_km = round((user_input * 1.609), 2)
    calc_label.config(text = f"{conv_km}")
    
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

calc_label = Label(text=0)
calc_label.grid(column=1, row=1)


button = Button(text="Calculate", command= to_km)
button.grid(column=1, row=2)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


window.mainloop()