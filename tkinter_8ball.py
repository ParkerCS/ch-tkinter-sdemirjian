# MAGIC 8-BALL (25pts)
# Create a tkinter app which acts as a "Magic 8-ball" fortune teller
# The user asks a yes/no question that they want an answer to.
# Then the user clicks a button, and your program displays
# the "magic" random answer to their question.
# Your program will have the following properties:
# - Use an App class to create the tkinter app
# - Add a proper title (appears in the window tab)
# - Add a Label widget at the top to give the user instructions/intro.
# - Add an Entry widget so the user can enter their question.
# - Add a Button widget which will trigger the answer.
# - Add a Label widget to display the answer (set to a initial value of "Your Fortune Here" or "--" or similar)
# - Get your random answer message from a list of at least 10 possible strings. (e.g. ["Yes", "No", "Most Likely", "Definitely", etc...])
# - Add THREE or more other style modifications to make your app unique (font family, font size, color, padding, image, borders, justification, whatever you can find in tkinter library etc.)  Make a comment at the top or bottom of your code to tell me your 3 things you did. (Just to help me out in checking your assignment)
from tkinter import *
from tkinter import font
import random

class App():
    def __init__(self, master):
        #variables
        self.response = StringVar()
        self.list = ["Sure, why not", "Who cares?", "There can be no question.", "Definitely not", "Probably", "Try again later", "Only on Tuesdays", "Yes", "No", "It is certain", "That's the dumbest question I've ever been asked don't even think about asking that again or I swear to God I'll find where you live and make sure it never happens again."]

        #Labels
        self.intro_label = Label(master, text="Ask the 8-Ball a question!", bg="gold").grid(row=1, column=1, columnspan=4, sticky="e" + "w")
        self.response_label = Label(master, textvariable=self.response).grid(row=4, column=1, columnspan=4, sticky="e" + "w")

        #Entry:
        self.entry = Entry(master, text="Enter your question here.").grid(row=2, column=1, columnspan=4, sticky="e" + "w")

        #Buttons
        self.receive_fortune = Button(master, text="Receive Fortune", relief="raised", bg="blue", fg="yellow", command=lambda:self.response.set(self.list[random.randrange(len(self.list))])).grid(row=3, column=1, columnspan=4, sticky="e" + "w")


if __name__ == "__main__":
    root = Tk()
    root.title("Magic 8-Ball")
    my_app = App(root)
    root.mainloop()