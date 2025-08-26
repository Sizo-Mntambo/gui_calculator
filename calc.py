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
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "ERROR")
        

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, tk.END)

root = tk.Tk()
root.geometry("300x300")
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)
root.mainloop()