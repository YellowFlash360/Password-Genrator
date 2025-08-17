#For password generating
"""import random 
a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1235467890~`!@#$%^&*()-=_+?><,./;':"
length=int(input("Enter Password Length "))
if length <=7 :
    print("Enter Greater than 7 ")
elif length>14:
    print("Choose number between 8 and 14 ")
else:
    b=""
    for _ in range(length):
        b=b+random.choice(a)
print("Password is : ",b)"""


# Password Generating with GUI

'''import tkinter as tk
from tkinter import messagebox
import random

def generate_password():
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1235467890~`!@#$%^&*()-=_+?><,./;':"
    try:
        length = int(entry_length.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer!")
        return

    if length <= 7:
        messagebox.showwarning("Invalid Length", "Enter Greater than 7")
    elif length > 14:
        messagebox.showwarning("Invalid Length", "Choose number between 8 and 14")
    else:
        b = ""
        for _ in range(length):
            b += random.choice(a)
        label_result.config(text=f"Password is: {b}")

# Set up the window
root = tk.Tk()
root.title("Password Generator")

# Widgets
label_intro = tk.Label(root, text="Enter Password Length (8-14):")
label_intro.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Run the GUI loop
root.mainloop()'''

# Password Generating with GUI along Security-Level

'''import tkinter as tk
from tkinter import messagebox
import random

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
    else: # High
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*()-=_+?><,./;':"
  
    if length <= 7:
        messagebox.showwarning("Invalid Length", "Enter greater than 7")
    elif length > 14:
        messagebox.showwarning("Invalid Length", "Choose number between 8 and 14")
    else:
        password = ''.join(random.choice(chars) for _ in range(length))
        label_result.config(text=f"Password is: {password}")

# Set up the window
root = tk.Tk()
root.title("Password Generator")

label_intro = tk.Label(root, text="Enter Password Length (8-14):")
label_intro.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

security_var = tk.StringVar(value="High")
label_security = tk.Label(root, text="Select Security Level:")
label_security.pack(pady=5)

frame_security = tk.Frame(root)
frame_security.pack()

radio_low = tk.Radiobutton(frame_security, text="Low", variable=security_var, value="Low")
radio_low.pack(side=tk.LEFT)
radio_medium = tk.Radiobutton(frame_security, text="Medium", variable=security_var, value="Medium")
radio_medium.pack(side=tk.LEFT)
radio_high = tk.Radiobutton(frame_security, text="High", variable=security_var, value="High")
radio_high.pack(side=tk.LEFT)

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()'''
import random
screat_number=random.randint(1,100)
attempt=7
print("Welcoe to play this game my friend")
print("I have choose a number for 1 to 100")
print(f" you have {attempt} chances to guess the number")
while attempt>0:
    guess=int(input("Enter the number: "))
    if guess==screat_number:
        print("congraluations You won the game")
        break
    elif guess<screat_number:
        print("Too Low")
    else:
        print("Too High")
    attempt-=1
    print(f"left chance :{attempt}")
if attempt==0:
    print("Your chances are completed")
    print("Better luck next time")