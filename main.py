import tkinter as tk
from tkinter import ttk
import time

window = tk.Tk()
window.title("Calculator App")

#secret number is 12345 followed by enter

entry = tk.Entry(window, width=20, borderwidth=5, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def secret_timer():
    progress = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=300, mode="determinate")
    progress.pack(padx=10, pady=10)
    progress.start()
    for i in range(100):
        time.sleep(1)
        progress['value'] = 1
        window.update_idletasks()
    progress.stop()


def button_equal():
    #secret area access
    expression = entry.get()
    if expression == "12345":
        entry.delete(0, tk.END)
        #entry.insert(0, "This is the secret area.")
        clear_window()
        window.geometry("1280x720")
        secret_timer()



    else:
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


window.mainloop()