# CoresCalc - Day 3

import tkinter as tk

window = tk.Tk()
window.title("CoresCalc")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

display_text = tk.StringVar()
display_text.set("0")

display = tk.Entry(
    window,
    textvariable=display_text,
    font=("Arial", 28),
    bg="#ffffff",
    fg="#0B1156",
    bd=2,
    relief="flat",
    justify="right",
    state="readonly"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=15, sticky="ew")

current_number = ""
first_number = None
operation = None
fresh_start = False

def press_number(num):
    global current_number, fresh_start
    if fresh_start:
        current_number = ""
        fresh_start = False
    current_number += str(num)
    display_text.set(current_number)

def press_operation(op):
    global current_number, first_number, operation, fresh_start
    if current_number == "" and first_number is None:
        return
    if current_number != "":
        if first_number is None:
            first_number = float(current_number)
        else:
            calculate()
            first_number = float(display_text.get())
    operation = op
    current_number = ""
    fresh_start = False
    display_text.set(display_text.get() + " " + op)

def calculate():
    global current_number, first_number, operation, fresh_start
    if first_number is None or current_number == "" or operation is None:
        return
    second_number = float(current_number)
    if operation == "+" :
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "x":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            display_text.set("Error: Div by 0")
            current_number = ""
            first_number = None
            operation = None
            return
        result = first_number / second_number
    if result == int(result):
        display_text.set(int(result))
    else:
        display_text.set(round(result, 8))
    current_number = ""
    first_number = None
    operation = None
    fresh_start = True

def press_clear():
    global current_number, first_number, operation, fresh_start
    current_number = ""
    first_number = None
    operation = None
    fresh_start = False
    display_text.set("0")

def press_decimal():
    global current_number
    if "." in current_number:
        return
    if current_number == "":
        current_number = "0"
    current_number += "."
    display_text.set(current_number)

buttons = [
    ("C", 1, 0, "#e74c3c", "#ffffff", 1),
    ("←", 1, 1, "#e67e22", "#ffffff", 1),
    ("/", 1, 2, "#b7c1c2", "#ffffff", 1),
    ("x", 1, 3, "#b7c1c2", "#ffffff", 1),
    ("7", 2, 0, "#ffffff", "#000000", 1),
    ("8", 2, 1, "#ffffff", "#000000", 1),
    ("9", 2, 2, "#ffffff", "#000000", 1),
    ("-", 2, 3, "#b7c1c2", "#ffffff", 1),
    ("4", 3, 0, "#ffffff", "#000000", 1),
    ("5", 3, 1, "#ffffff", "#000000", 1),
    ("6", 3, 2, "#ffffff", "#000000", 1),
    ("+", 3, 3, "#b7c1c2", "#ffffff", 1),
    ("1", 4, 0, "#ffffff", "#000000", 1),
    ("2", 4, 1, "#ffffff", "#000000", 1),
    ("3", 4, 2, "#ffffff", "#000000", 1),
    ("=", 4, 3, "#2ecc71", "#ffffff", 2),
    ("0", 5, 0, "#ffffff", "#000000", 2),
    (".", 5, 2, "#ffffff", "#000000", 1),
]

def press_backspace():
    global current_number
    if current_number != "":
        current_number = current_number[:-1]
        if current_number == "":
            display_text.set("0")
        else:
            display_text.set(current_number)

for (text, row, col, bg_color, fg_color, rowspan) in buttons:
    if text.isdigit():
        action = lambda t=text: press_number(t)
    elif text in ["+", "-", "x", "/"]:
        action = lambda t=text: press_operation(t)
    elif text == "=":
        action = calculate
    elif text == "C":
        action = press_clear
    elif text == "←":
        action = press_backspace
    elif text == ".":
        action = press_decimal
    else:
        action = lambda: None

    btn = tk.Button(
        window,
        text=text,
        font=("Arial", 18, "bold"),
        bg=bg_color,
        fg=fg_color,
        width=4,
        height=2,
        relief="flat",
        cursor="hand2",
        command=action
    )
    btn.grid(row=row, column=col, rowspan=rowspan, padx=4, pady=4, sticky="nsew")

window.mainloop()