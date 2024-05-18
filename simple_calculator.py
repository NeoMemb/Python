from tkinter import *

screen = Tk()
screen.title("Abdulrofii's Calculator")
#screen.iconbitmap(".ico")

display = Entry(screen, width=55, borderwidth=3, fg="blue", bg="#FFFACA")
display.grid(row=0, column=0, columnspan=3)

# displayClick function
def displayClick(number):
    current_display = display.get() # <-- collect the display number
    display.delete(0, END) # <--  after deletion of the display
    display.insert(0, str(current_display) + str(number)) # replace it with deleted data and the inputed data

    
# clear button function
def displayClear():
    display.delete(0, END)


# + {plus} function
def addArithemetric():
    fisrt_numb = display.get()
    global first_int
    global calc
    calc = "addition"
    first_int = int(fisrt_numb)
    display.delete(0, END)
    
# EqualTo function
def equalTo():
    global second_number
    second_number = display.get()
    sec_digit = int(second_number)
    display.delete(0, END)
    if calc == "addition":
        display.insert(0, first_int + sec_digit)
    if calc == "substraction":
        display.insert(0, first_int - sec_digit)
    if calc == "multiplication":
        display.insert(0, first_int * sec_digit)
    if calc == "division":
        try:
            display.insert(0, first_int / sec_digit)
        except ZeroDivisionError:
            indefinite = "Infinity"
            display.insert(0, indefinite)


# Multiply Function
def multiplyFunction():
    fisrt_numb = display.get()
    global first_int
    first_int = int(fisrt_numb)
    global calc
    calc = "multiplication"
    display.delete(0, END)


# Division function
def divisionFunction():
    fisrt_numb = display.get()
    global  first_int
    global calc
    calc = "division"
    first_int = int(fisrt_numb)
    display.delete(0, END)


# Substract Function
def substractFunction():
    fisrt_numb = display.get()
    global  first_int
    global calc
    calc = "substraction"
    first_int = int(fisrt_numb)
    display.delete(0, END)


# All the display button
button_1 = Button(screen, text="1", bg="white", padx=50, pady=30, command=lambda: displayClick("1"))
button_2 = Button(screen, text="2", bg="white", padx=50, pady=30, command=lambda: displayClick("2"))
button_3 = Button(screen, text="3", bg="white", padx=50, pady=30, command=lambda: displayClick("3"))
button_4 = Button(screen, text="4", bg="white", padx=50, pady=30, command=lambda: displayClick("4"))
button_5 = Button(screen, text="5", bg="white", padx=50, pady=30, command=lambda: displayClick("5"))
button_6 = Button(screen, text="6", bg="white", padx=50, pady=30, command=lambda: displayClick("6"))
button_7 = Button(screen, text="7", bg="white", padx=50, pady=30, command=lambda: displayClick("7"))
button_8 = Button(screen, text="8", bg="white", padx=50, pady=30, command=lambda: displayClick("8"))
button_9 = Button(screen, text="9", bg="white", padx=50, pady=30, command=lambda: displayClick("9"))
button_0 = Button(screen, text="0", bg="white", padx=50, pady=30, command=lambda: displayClick("0"))
button_clear = Button(screen, text="C", bg="red", padx=50, pady=30, command=lambda: displayClear())
button_add = Button(screen, text="+", bg="#27FF00", padx=50, pady=30, command=lambda: addArithemetric())
button_equal = Button(screen, text="=", bg="orange",padx=50, pady=30, command=lambda: equalTo())
button_multiply = Button(screen, text="X", bg="blue", padx=50, pady=30, command=lambda: multiplyFunction())
button_divide = Button(screen, text="/", bg="indigo", padx=50, pady=30, command=lambda: divisionFunction())
button_substract = Button(screen, text="-", bg="brown", padx=50, pady=30, command=lambda: substractFunction())
button_quit = Button(screen, text="Quit", bg="red", padx=50, pady=30, command=screen.quit)

# Buttons grids
button_1.grid(row=1, column=0)
button_2.grid(row=1,column= 1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1)
button_multiply.grid(row=4, column=2)
button_divide.grid(row=5, column=2)
button_substract.grid(row=6, column=0)
button_quit.grid(row=6, column=1)



screen.mainloop()