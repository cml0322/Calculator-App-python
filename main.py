import tkinter as tk
window = tk.Tk()
window.title("Calculator App")

entry = tk.Entry(window, width=20, borderwidth=5, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error, invalid input")


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_num = 1
col_num = 0

for button_text in buttons:
    if button_text == '=':
        button = tk.Button(window, text=button_text, padx=40, pady=20, command=button_equal)
    else:
        button = tk.Button(window, text=button_text, padx=40, pady=20, command=lambda b=button_text: button_click(b))
    button.grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1


button_clear = tk.Button(window, text='C', padx=40, pady=20, command=button_clear)
button_clear.grid(row=5, column=0, columnspan=4, sticky="we")

#wow
window.mainloop()