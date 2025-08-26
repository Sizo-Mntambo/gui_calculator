import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    pass

def evaluate_calculation():
    pass

def clear_field():
    pass

root = tk.Tk()
root.geometry("300x300")
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=3)
root.mainloop()