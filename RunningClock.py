# Importing Clock.py
import get_time as gt
from tkinter import Tk, Label

# Initialize the Tkinter Application Window
window = Tk()
window.title("Running Clock")
window.iconbitmap("hourglass.ico")

# Application styling
label = Label(bg="black", fg="#25BF15", font=("roboto", 24, "italic"), cursor="cross")

# Function to display running clock
def myDisplay():
    label.config(text=gt.myClock())
    # Center displayed text in the window
    label.pack(anchor='center')
    label.after(1000, myDisplay)

# Function call to display text
myDisplay()

window.mainloop()