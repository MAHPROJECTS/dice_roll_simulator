from tkinter import *
from PIL import Image, ImageTk
import random

# List of image filenames (no folder path needed if images are in same folder)
dice_images = [
    'dice_1.png',
    'dice_2.png',
    'dice_3.png',
    'dice_4.png',
    'dice_5.png',
    'dice_6.png'
]

# GUI setup
root = Tk()
root.title("Dice Roll Simulator")

# Load default image
current_image = ImageTk.PhotoImage(Image.open(dice_images[0]))
label = Label(root, image=current_image)
label.pack()

# Roll function
def roll_dice():
    new_image = ImageTk.PhotoImage(Image.open(random.choice(dice_images)))
    label.config(image=new_image)
    label.image = new_image

# Button
roll_button = Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

root.mainloop()

