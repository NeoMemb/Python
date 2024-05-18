from tkinter import *
from PIL import ImageTk, Image

root = Tk()

image1 = ImageTk.PhotoImage(Image.open("Daniel.jpg"))
image2 = ImageTk.PhotoImage(Image.open("Ferrari.jpg"))
image3 = ImageTk.PhotoImage(Image.open("mansa_musa.jpg"))
image4 = ImageTk.PhotoImage(Image.open("sonyProduct.jpg"))
image5 = ImageTk.PhotoImage(Image.open("Zeus.jpg"))

image_list = [image1, image2, image3, image4, image5]

myLabel = Label(root, image=image3)
next_button = Button(root, text=">>", padx=20, pady=20, bg="black", fg="white", command=lambda:nextButton(2))
prev_button = Button(root, text="<<", bg="black", fg="white", padx=20, pady=20, command=lambda:prevButton())
myLabel.grid(row=0, column=0, columnspan=3)
next_button.grid(row=1, column=2)

def nextButton(image_number):
    myLabel.grid_forget()
    myLabel = Label(root, image=image_list[image_number - 1])
    next_button = Button(root, text=">>", padx=20, pady=20, bg="black", fg="white", command=lambda:nextButton(2))

    myLabel.grid(row=0, column=0, columnspan=3)
    next_button.grid(row=1, column=2)

def prevButton():
    return

root.mainloop()