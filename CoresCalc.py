# CoresCalc - Day 4 (Final)

import tkinter as tk
from tkinter import ttk

# WINDOW SETUP

window = tk.Tk()
window.title("CoresCalc")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background="#f0f0f0", borderwidth=0)
style.configure("TNotebook.Tab", font=("Arial", 11, "bold"), padding=[20, 8])
style.map("TNotebook.Tab",
    background=[("selected", "#ffffff"), ("!selected", "#d0d0d0")],
    foreground=[("selected", "#000000"), ("!selected", "#555555")]
)

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

calc_frame = tk.Frame(notebook, bg="#f0f0f0")
area_frame = tk.Frame(notebook, bg="#f0f0f0")
data_frame = tk.Frame(notebook, bg="#f0f0f0")

notebook.add(calc_frame, text="  Calculator  ")
notebook.add(area_frame, text="  Area  ")
notebook.add(data_frame, text="  Data  ")

# TAB 1 — CALCULATOR

expression = ""

def update_display(value):
    display_text.set(value)

def press_number(num):
    global expression
    expression += str(num)
    update_display(expression)

def press_operation(op):
    global expression
    if expression == "" or expression[-1] in ["+", "-", "x", "/"]:
        return
    expression += op
    update_display(expression)

def calculate():
    global expression
    if expression == "":
        return
    try:
        actual_expression = expression.replace("x", "*")
        result = eval(actual_expression)
        if result == int(result):
            update_display(int(result))
            expression = str(int(result))
        else:
            update_display(round(result, 8))
            expression = str(round(result, 8))
    except ZeroDivisionError:
        update_display("Error: Div by 0")
        expression = ""
    except:
        update_display("Error")
        expression = ""

def press_clear():
    global expression
    expression = ""
    update_display("0")

def press_backspace():
    global expression
    expression = expression[:-1]
    if expression == "":
        update_display("0")
    else:
        update_display(expression)

def press_decimal():
    global expression
    parts = expression.replace("x", "+").replace("-", "+").replace("/", "+").split("+")
    last_part = parts[-1]
    if "." in last_part:
        return
    if expression == "" or expression[-1] in ["+", "-", "x", "/"]:
        expression += "0"
    expression += "."
    update_display(expression)

display_text = tk.StringVar()
display_text.set("0")

display = tk.Entry(
    calc_frame,
    textvariable=display_text,
    font=("Arial", 28),
    bg="#ffffff",
    fg="#000000",
    bd=2,
    relief="flat",
    justify="right",
    state="readonly"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=15, sticky="ew")

buttons = [
    ("C",  1, 0, "#e74c3c", "#ffffff", 1),
    ("←",  1, 1, "#e67e22", "#ffffff", 1),
    ("/",  1, 2, "#95a5a6", "#ffffff", 1),
    ("x",  1, 3, "#95a5a6", "#ffffff", 1),
    ("7",  2, 0, "#ffffff", "#000000", 1),
    ("8",  2, 1, "#ffffff", "#000000", 1),
    ("9",  2, 2, "#ffffff", "#000000", 1),
    ("-",  2, 3, "#95a5a6", "#ffffff", 1),
    ("4",  3, 0, "#ffffff", "#000000", 1),
    ("5",  3, 1, "#ffffff", "#000000", 1),
    ("6",  3, 2, "#ffffff", "#000000", 1),
    ("+",  3, 3, "#95a5a6", "#ffffff", 1),
    ("1",  4, 0, "#ffffff", "#000000", 1),
    ("2",  4, 1, "#ffffff", "#000000", 1),
    ("3",  4, 2, "#ffffff", "#000000", 1),
    ("=",  4, 3, "#2ecc71", "#ffffff", 2),
    ("0",  5, 0, "#ffffff", "#000000", 2),
    (".",  5, 2, "#ffffff", "#000000", 1),
]

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
        calc_frame,
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

# TAB 2 — AREA CONVERTER

area_units = {
    "km²":      1e6,
    "m²":       1,
    "cm²":      1e-4,
    "mm²":      1e-6,
    "Hectare":  1e4,
    "Acre":     4046.856,
}

def convert_area(event=None):
    try:
        value = float(area_input.get())
        from_unit = area_from.get()
        to_unit = area_to.get()
        value_in_m2 = value * area_units[from_unit]
        result = value_in_m2 / area_units[to_unit]
        if result == int(result):
            area_result.set(f"{int(result)} {to_unit}")
        else:
            area_result.set(f"{round(result, 6)} {to_unit}")
    except ValueError:
        area_result.set("Invalid input")

tk.Label(area_frame, text="Area Converter", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=15)

tk.Label(area_frame, text="Enter value:", font=("Arial", 11), bg="#f0f0f0").pack()
area_input = tk.Entry(area_frame, font=("Arial", 14), justify="center", relief="flat", bd=2)
area_input.pack(pady=5, ipady=5, padx=40, fill="x")

tk.Label(area_frame, text="From:", font=("Arial", 11), bg="#f0f0f0").pack(pady=(10,0))
area_from = ttk.Combobox(area_frame, values=list(area_units.keys()), font=("Arial", 12), state="readonly")
area_from.set("m²")
area_from.pack(pady=5)

tk.Label(area_frame, text="To:", font=("Arial", 11), bg="#f0f0f0").pack(pady=(10,0))
area_to = ttk.Combobox(area_frame, values=list(area_units.keys()), font=("Arial", 12), state="readonly")
area_to.set("km²")
area_to.pack(pady=5)

tk.Button(
    area_frame,
    text="Convert",
    font=("Arial", 12, "bold"),
    bg="#2ecc71",
    fg="#ffffff",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=8,
    command=convert_area
).pack(pady=15)

area_result = tk.StringVar()
area_result.set("")
tk.Label(area_frame, textvariable=area_result, font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#2c3e50").pack()

# TAB 3 — DATA CONVERTER

data_units = {
    "Bit":      1,
    "Byte":     8,
    "KB":       8 * 1024,
    "MB":       8 * 1024 ** 2,
    "GB":       8 * 1024 ** 3,
    "TB":       8 * 1024 ** 4,
}

def convert_data(event=None):
    try:
        value = float(data_input.get())
        from_unit = data_from.get()
        to_unit = data_to.get()
        value_in_bits = value * data_units[from_unit]
        result = value_in_bits / data_units[to_unit]
        if result == int(result):
            data_result.set(f"{int(result)} {to_unit}")
        else:
            data_result.set(f"{round(result, 6)} {to_unit}")
    except ValueError:
        data_result.set("Invalid input")

tk.Label(data_frame, text="Data Converter", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=15)

tk.Label(data_frame, text="Enter value:", font=("Arial", 11), bg="#f0f0f0").pack()
data_input = tk.Entry(data_frame, font=("Arial", 14), justify="center", relief="flat", bd=2)
data_input.pack(pady=5, ipady=5, padx=40, fill="x")

tk.Label(data_frame, text="From:", font=("Arial", 11), bg="#f0f0f0").pack(pady=(10,0))
data_from = ttk.Combobox(data_frame, values=list(data_units.keys()), font=("Arial", 12), state="readonly")
data_from.set("MB")
data_from.pack(pady=5)

tk.Label(data_frame, text="To:", font=("Arial", 11), bg="#f0f0f0").pack(pady=(10,0))
data_to = ttk.Combobox(data_frame, values=list(data_units.keys()), font=("Arial", 12), state="readonly")
data_to.set("GB")
data_to.pack(pady=5)

tk.Button(
    data_frame,
    text="Convert",
    font=("Arial", 12, "bold"),
    bg="#2196f3",
    fg="#ffffff",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=8,
    command=convert_data
).pack(pady=15)

data_result = tk.StringVar()
data_result.set("")
tk.Label(data_frame, textvariable=data_result, font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#2c3e50").pack()

# START

window.mainloop()