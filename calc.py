import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "ERROR")
        

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, tk.END)

root = tk.Tk()

# Theme palette
BG_APP = "#e0e0e0"         # light grey app background
BG_DISPLAY = "#f5f5f5"     # lighter grey for display
FG_DISPLAY = "#222222"     # dark text
BTN_BG = "#0b3d91"         # dark blue buttons
BTN_FG = "#ffffff"         # white text
BTN_ACTIVE_BG = "#0a2f70"  # darker blue on press
BTN_ACTIVE_FG = "#ffffff"
BTN_FONT = ("Arial", 14)

root.configure(bg=BG_APP)
root.geometry("300x320")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24),
                      bg=BG_DISPLAY, fg=FG_DISPLAY, bd=0, relief="flat")
text_result.grid(columnspan=7, padx=10, pady=10)

# Helper to create consistently styled buttons
def make_btn(text, cmd, width=5):
    return tk.Button(root, text=text, command=cmd, width=width, font=BTN_FONT,
                     bg=BTN_BG, fg=BTN_FG, activebackground=BTN_ACTIVE_BG,
                     activeforeground=BTN_ACTIVE_FG, bd=0, relief="raised",
                     highlightthickness=0)

button1 = make_btn("1", lambda: add_to_calculation(1))
button1.grid(row=2, column=1, padx=5, pady=5)
button2 = make_btn("2", lambda: add_to_calculation(2))
button2.grid(row=2, column=2, padx=5, pady=5)
button3 = make_btn("3", lambda: add_to_calculation(3))
button3.grid(row=2, column=3, padx=5, pady=5)
button4 = make_btn("4", lambda: add_to_calculation(4))
button4.grid(row=3, column=1, padx=5, pady=5)
button5 = make_btn("5", lambda: add_to_calculation(5))
button5.grid(row=3, column=2, padx=5, pady=5)
button6 = make_btn("6", lambda: add_to_calculation(6))
button6.grid(row=3, column=3, padx=5, pady=5)
button7 = make_btn("7", lambda: add_to_calculation(7))
button7.grid(row=4, column=1, padx=5, pady=5)
button8 = make_btn("8", lambda: add_to_calculation(8))
button8.grid(row=4, column=2, padx=5, pady=5)
button9 = make_btn("9", lambda: add_to_calculation(9))
button9.grid(row=4, column=3, padx=5, pady=5)
button0 = make_btn("0", lambda: add_to_calculation(0))
button0.grid(row=5, column=1, padx=5, pady=5)

button_equal = make_btn("=", lambda: evaluate_calculation(), width=24)
button_equal.grid(row=6, column=1, columnspan=4, padx=5, pady=(5,10))

button_plus = make_btn("+", lambda: add_to_calculation("+"))
button_plus.grid(row=2, column=4, padx=5, pady=5)
button_minus = make_btn("-", lambda: add_to_calculation("-"))
button_minus.grid(row=3, column=4, padx=5, pady=5)
button_multiply = make_btn("*", lambda: add_to_calculation("*"))
button_multiply.grid(row=4, column=4, padx=5, pady=5)
button_divide = make_btn("/", lambda: add_to_calculation("/"))
button_divide.grid(row=5, column=4, padx=5, pady=5)
button_bracket_open = make_btn("(", lambda: add_to_calculation("("))
button_bracket_open.grid(row=5, column=2, padx=5, pady=5)
button_bracket_close = make_btn(")", lambda: add_to_calculation(")"))
button_bracket_close.grid(row=5, column=3, padx=5, pady=5)
button_clear = make_btn("C", lambda: clear_field(), width=24)
button_clear.grid(row=7, column=1, columnspan=4, padx=5, pady=(0,10))
root.mainloop()