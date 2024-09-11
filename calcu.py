import tkinter as tk
from tkinter import messagebox

def button_click(item):
    current = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, current + str(item))

def clear_display():
    entry_field.delete(0, tk.END)

def calculate():
    try:
        expression = entry_field.get()
        result = str(eval(expression))
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def apply_styles():
    window.config(bg="black")
    entry_field.config(bg="black", fg="white", bd=5, font=('Arial', 18), justify='right')

    for btn in button_list:
        btn.config(bg="#333333", fg="white", activebackground="gray", relief="flat")
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg="gray"))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#333333"))

window = tk.Tk()
window.title("Calculator")

entry_field = tk.Entry(window, width=16)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

button_list = []
row = 1
col = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(window, text=button, width=5, height=2, font=('Arial', 12),
                        command=calculate)
    elif button == 'C':
        btn = tk.Button(window, text=button, width=5, height=2, font=('Arial', 12),
                        command=clear_display)
    else:
        btn = tk.Button(window, text=button, width=5, height=2, font=('Arial', 12),
                        command=lambda b=button: button_click(b))
    
    btn.grid(row=row, column=col, padx=5, pady=5)
    button_list.append(btn)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

apply_styles()

entry_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

window.mainloop()