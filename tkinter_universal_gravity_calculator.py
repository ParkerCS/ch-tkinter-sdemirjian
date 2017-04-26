# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a tkinter app with the following attributes:
# - use an App class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed.  Yay!
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 3 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.
from tkinter import *
from tkinter import font

class App():
    def __init__(self, master):
        self.font = font.Font(family="Helvetica Light", size=10)
        self.result = StringVar()
        self.result.set(3)
        self.m1_variable = DoubleVar()
        self.m2_variable = DoubleVar()
        self.r_variable = DoubleVar()

        #labels
        self.title = Label(master, text="Gravitational Force Calculator", font=self.font).grid(row=1, column=1, columnspan=4, sticky="e" + "w")
        self.m1 = Label(master, text="M1:", width=15, font=self.font, fg="blue").grid(row=2, column=1, columnspan=2, sticky="e" + "w")
        self.m2 = Label(master, text="M2:", font=self.font, fg="blue").grid(row=3, column=1, columnspan=2, sticky="e" + "w")
        self.r = Label(master, text="R:", font=self.font, fg="blue").grid(row=4, column=1, columnspan=2, sticky="e" + "w")
        self.result_label = Label(master, textvariable=self.result, font=self.font).grid(row=5, column=3, columnspan=2, sticky="e" + "w")

        #entries
        self.m1_entry = Entry(master, textvariable=self.m1_variable).grid(row=2, column=3, columnspan=2, sticky="e" + "w")
        self.m2_entry = Entry(master, textvariable=self.m2_variable).grid(row=3, column=3, columnspan=2, sticky="e" + "w")
        self.r_entry = Entry(master, textvariable=self.r_variable).grid(row=4, column=3, columnspan=2, sticky="e" + "w")

        #buttons
        self.calculate_button = Button(master, text="Calculate Force", bg="orange", command=lambda:self.result.set(self.calculate(self.m1_variable.get(), self.m2_variable.get(), self.r_variable.get())), font=self.font).grid(row=5, column=1, columnspan=2, sticky="e" + "w")

    def calculate(self, m1, m2, r):
        if r**2 == 0:
            return "Division by zero!"
        else:
            return (6.67e-11) * (m1 * m2) / r**2

if __name__ == "__main__":
    root = Tk()
    root.title("Universal Gravity Calculator")
    my_app = App(root)
    root.mainloop()