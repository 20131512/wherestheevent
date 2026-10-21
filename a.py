
from tkinter import *


window = Tk()
window.title("Event Handler")
window.geometry("100x100")


def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

window.bind("<key>", handle_keypress)

def handel_click(event):
    print("\nthe button was clicked!")

button = Button(text="click me!")
button.pack

button.bind("<button-1>", handel_click)
window.mainloop()