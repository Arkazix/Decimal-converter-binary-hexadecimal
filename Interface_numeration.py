from tkinter import *

window = Tk()
color = "#4065A4"
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("pi-PassWord.ico")


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
    label1.insert(END, input_decimal.get())
    label2.insert(END, a)
    label3.insert(END, b)
    label1.insert(END, "\n")
    label2.insert(END, "\n")
    label3.insert(END, "\n")


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
    label1.insert(END, a)
    label2.insert(END, input_binary.get())
    label3.insert(END, b)
    label1.insert(END, "\n")
    label2.insert(END, "\n")
    label3.insert(END, "\n")


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
    label1.insert(END, a)
    label2.insert(END, b)
    label3.insert(END, input_hexadecimal.get())
    label1.insert(END, "\n")
    label2.insert(END, "\n")
    label3.insert(END, "\n")


def title_box(place, text, column):
    return Label(place, bg=color, text=text, fg="white", font=("Helvetica", 15)) \
        .grid(column=column, row=0, ipady=10, ipadx=70)


def button_box(text, command, column):
    return Button(frame_conversion, bg=color, text=text, font=("Helvetica", 11), fg="white", activeforeground="white",
                  activebackground=color, bd=1, overrelief=SUNKEN, command=command)\
        .grid(column=column, row=2, ipady=10, pady=10, padx=50)


# INPUT BOX
def input_box_launch(place, row):
    global input_decimal
    global input_binary
    global input_hexadecimal

    input_decimal = Entry(place, bg="#414141", fg="white", font=("Helvetica", 11))
    input_decimal.grid(column=0, row=row, ipady=10, ipadx=36, padx=70)
    input_decimal.insert(0, 0)

    input_binary = Entry(place, bg="#414141", fg="white", font=("Helvetica", 11))
    input_binary.grid(column=1, row=row, ipady=10, pady=5, ipadx=41, )
    input_binary.insert(0, 0)

    input_hexadecimal = Entry(place, bg="#414141", fg="white", font=("Helvetica", 11))
    input_hexadecimal.grid(column=2, row=row, ipady=10, ipadx=20, padx=70)
    input_hexadecimal.insert(0, 0)


# BUTTON BOX
def button_box_launcher():
    global button_decimal
    global button_binary
    global button_hexadecimal

    button_decimal = button_box("Convert to binary and hexadecimal", input_decimal_function, 0)

    button_binary = button_box("Convert to decimal and hexadecimal", input_binary_function, 1)

    button_hexadecimal = button_box("Convert to decimal and binary", input_hexadecimal_function, 2)


# TITLE BOX
def title_box_launch():
    global label_decimal
    global label_binary
    global label_hexadecimal

    label_decimal = title_box(frame_conversion, "Decimal", 0)

    label_binary = title_box(frame_conversion, "Binary", 1)

    label_hexadecimal = title_box(frame_conversion, "Hexadecimal", 2)


def title_box_launch_history():
    global label_decimal
    global label_binary
    global label_hexadecimal

    label_decimal = title_box(frame_history, "Decimal", 0)

    label_binary = title_box(frame_history, "Binary", 1)

    label_hexadecimal = title_box(frame_history, "Hexadecimal", 2)


def clear():
    global label1
    global label2
    global label3
    label1.delete(1.0, END)
    label2.delete(1.0, END)
    label3.delete(1.0, END)


window_state = 0
frame_conversion = Frame(window, bg=color)
frame_history = Frame(window, bg=color)
label1 = Text(frame_history, bg="#414141", width=20, height=40, font=("Helvetica", 15))
label2 = Text(frame_history, bg="#414141", width=20, height=40, font=("Helvetica", 15))
label3 = Text(frame_history, bg="#414141", width=20, height=40, font=("Helvetica", 15))
button_delete = Button(frame_history, bg=color, text="clear", font=("Helvetica", 11), fg="white",
                       activeforeground="white", activebackground=color, bd=1, overrelief=SUNKEN, command=clear)


def launch_main_conversion_window():
    global window_state
    if window_state == 0:
        frame_history.pack_forget()
        window_state = 1
        window.title("Decimal converter, binary, hexadecimal")
        window.config(bg="#4065A4")

        # FRAME CREATE
        global frame_conversion

        title_box_launch()
        input_box_launch(frame_conversion, 1)
        button_box_launcher()

        # FRAME PACK
        frame_conversion.pack(expand=TRUE)

        # task barre
        menu_bar = Menu(window)
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="History", command=launch_second_window_history)
        file_menu.add_command(label="Conversion", command=launch_main_conversion_window)
        window.config(menu=menu_bar)

    window.mainloop()


def launch_second_window_history():
    global window_state
    global frame_conversion
    global label1
    global label2
    global label3
    global button_delete
    if window_state == 1:
        window_state = 0
        frame_conversion.pack_forget()
        frame_history.pack()
        title_box_launch_history()
        label1.grid(column=0, row=1, padx=15)
        label2.grid(column=1, row=1)
        label3.grid(column=2, row=1)
        button_delete.grid(column=3, row=0)


# WINDOW LAUNCH
launch_main_conversion_window()
