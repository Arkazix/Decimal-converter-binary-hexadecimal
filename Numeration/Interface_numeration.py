from tkinter import *

window = Tk()
color = "#4065A4"

window.title("Decimal converter, binary, hexadecimal")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("pi-PassWord.ico")
window.config(bg="#4065A4")

# CREATE FUNCTION


def input_decimal_function():
    a = input_decimal.get()
    b = input_decimal.get()
    a = "{0:b}".format(int(a))
    b = "{0:x}".format(int(b))
    input_binary.delete(0, END)
    input_hexadecimal.delete(0, END)
    input_binary.insert(0, a)
    input_hexadecimal.insert(0, b)


def input_binary_function():
    a = input_binary.get()
    b = input_binary.get()
    a = int(a, 2)
    b = int(b, 2)
    b = "{0:x}".format(int(b))
    input_decimal.delete(0, END)
    input_hexadecimal.delete(0, END)
    input_decimal.insert(0, a)
    input_hexadecimal.insert(0, b)


def input_hexadecimal_function():
    a = input_hexadecimal.get()
    b = input_hexadecimal.get()
    a = int(a, 16)
    b = int(b, 16)
    b = "{0:b}".format(int(b))
    input_decimal.delete(0, END)
    input_binary.delete(0, END)
    input_decimal.insert(0, a)
    input_binary.insert(0, b)



# FRAME CREATE
frame = Frame(window, bg=color, height=20)

# TITLE BOX
label_decimal = Label(frame, bg=color, text="Decimal", fg="white", font=("Helvetica", 15)) \
    .grid(column=0, row=0, ipady=10)

label_binary = Label(frame, bg=color, text="Binary", fg="white", font=("Helvetica", 15)) \
    .grid(column=1, row=0, ipady=10)

label_hexadecimal = Label(frame, bg=color, text="Hexadecimal", fg="white", font=("Helvetica", 15)) \
    .grid(column=2, row=0, ipady=10)

# BUTTON BOX
button_decimal = Button(frame, bg=color, text="Convert to binary and hexadecimal", font=("Helvetica", 11), fg="white",
                        activeforeground="white", activebackground=color, bd=1, overrelief=SUNKEN,
                        command=input_decimal_function).grid(column=0, row=2, ipady=10, pady=10)

button_binary = Button(frame, bg=color, text="Convert to decimal and hexadecimal", font=("Helvetica", 11), fg="white",
                       activeforeground="white", activebackground=color, bd=1, overrelief=SUNKEN,
                       command=input_binary_function).grid(column=1, row=2, ipady=10, pady=10)

button_hexadecimal = Button(frame, bg=color, text="Convert to decimal and binary", font=("Helvetica", 11), fg="white",
                            activeforeground="white", activebackground=color, bd=1, overrelief=SUNKEN,
                            command=input_hexadecimal_function).grid(column=2, row=2, ipady=10, pady=10)

# INPUT BOX
input_decimal = Entry(frame, bg="#414141", fg="white", font=("Helvetica", 11))
input_decimal.grid(column=0, row=1, ipady=10, ipadx=36)

input_binary = Entry(frame, bg="#414141", fg="white", font=("Helvetica", 11))
input_binary.grid(padx=50, column=1, row=1, ipady=10, ipadx=41, )

input_hexadecimal = Entry(frame, bg="#414141", fg="white", font=("Helvetica", 11))
input_hexadecimal.grid(column=2, row=1, ipady=10, ipadx=20)


# FRAME PACK
frame.pack(expand=TRUE)

# WINDOW LAUNCH
window.mainloop()