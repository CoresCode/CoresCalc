# CoresCalc
A Python calculator built in 4 days — from terminal to polished GUI.

## Progress
- Day 1 - Basic terminal calculator (2 numbers, 4 operations)
- Day 2 - Chained operations, loop, error handling
- Day 3 - GUI calculator with Tkinter
- Day 4 - Polished tabbed GUI, BODMAS fix, Area & Data converter

## Features
### Day 1
- Takes 2 numbers as input
- Supports Add, Subtract, Multiply, Divide
- Handles divide by zero

### Day 2
- Chain as many numbers as you want
- Picks operation between each number
- Handles invalid inputs without crashing
- Ask to calculate again after result

### Day 3
- Full graphical calculator window
- Number buttons, operation buttons, equals
- Backspace button to delete last digit
- Clear button to reset
- Decimal point support
- Chained operations (2 + 6 + 9 works)
- Handles divide by zero gracefully

### Day 4
- Tabbed interface (Calculator, Area, Data)
- BODMAS correctly followed using eval()
- Area Converter — km², m², cm², mm², Hectare, Acre
- Data Converter — Bit, Byte, KB, MB, GB, TB

## How to run
```bash
python "Python Calculator.py"
```

## Built with
- Python 3.x
- Tkinter (built-in GUI library)
- ttk (Themed Tkinter widgets)

## What I learned
- Terminal input/output and basic Python logic
- While loops, error handling with try/except
- Building GUIs with Tkinter and ttk
- Event-driven programming
- Dictionary-based unit conversion
- BODMAS evaluation using Python's eval()
