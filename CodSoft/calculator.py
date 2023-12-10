import tkinter as tk

def update_display(value):
    current = display_label.cget("text")
    if current == "0" and value != ".":
        display_label.config(text=value)
    else:
        display_label.config(text=current + str(value))

def clear_display():
    display_label.config(text="0")

def calculate():
    try:
        expression = display_label.cget("text")
        result = eval(expression)
        display_label.config(text=str(result))
    except Exception as e:
        display_label.config(text="Error")

# Create the main window
root = tk.Tk()
root.title("Interactive Calculator")

# Display
display_label = tk.Label(root, text="0", font=("Arial", 20), width=15, bd=5, relief="ridge", anchor="e")
display_label.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "C", "+"
]

row_val = 1
col_val = 0

for text in button_texts:
    if text != "C" and text != "=":
        tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: update_display(t)).grid(row=row_val, column=col_val)
    elif text == "C":
        tk.Button(root, text=text, padx=20, pady=20, command=clear_display).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=text, padx=20, pady=20, command=calculate).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
