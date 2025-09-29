# Password Generating along with Security-Level

import tkinter as tk
from tkinter import messagebox
import random
import platform

def generate_password():
    length_str = entry_length.get()
    try:
        length = int(length_str)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for length!")
        return

    security = security_var.get()
    
    if security == "Low":
        chars = "abcdefghijklmnopqrstuvwxyz"
    elif security == "Medium":
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    else:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*()-=_+?><,./;':"
    
    if length <= 7:
        messagebox.showwarning("Invalid Length", "Enter a length greater than 7")
    elif length > 14:
        messagebox.showwarning("Invalid Length", "Choose a number between 8 and 14")
    else:
        password = ''.join(random.choice(chars) for _ in range(length))
        label_result.config(text=f"Generated Password: {password}")

# Set up the window
root = tk.Tk()
root.title("Password Generator")

# Make the window fullscreen based on the operating system
if platform.system() == "Windows":
    root.state('zoomed')
else:
    root.attributes('-fullscreen', True)

# Set up the GUI components
label_intro = tk.Label(root, text="Enter Password Length (8-14):", font=("Arial", 16))
label_intro.pack(pady=15)

entry_length = tk.Entry(root, font=("Arial", 14), justify='center')
entry_length.pack(pady=10, ipady=5)

security_var = tk.StringVar(value="High")
label_security = tk.Label(root, text="Select Security Level:", font=("Arial", 16))
label_security.pack(pady=15)

frame_security = tk.Frame(root)
frame_security.pack()

radio_low = tk.Radiobutton(frame_security, text="Low", variable=security_var, value="Low", font=("Arial", 12))
radio_low.pack(side=tk.LEFT, padx=10)
radio_medium = tk.Radiobutton(frame_security, text="Medium", variable=security_var, value="Medium", font=("Arial", 12))
radio_medium.pack(side=tk.LEFT, padx=10)
radio_high = tk.Radiobutton(frame_security, text="High", variable=security_var, value="High", font=("Arial", 12))
radio_high.pack(side=tk.LEFT, padx=10)

button_generate = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 14))
button_generate.pack(pady=20, ipadx=10, ipady=5)

label_result = tk.Label(root, text="", font=("Courier", 18, "bold"), fg="blue")
label_result.pack(pady=10)

# Add an exit button for fullscreen mode
button_exit = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12))
button_exit.pack(pady=20)

root.mainloop()
