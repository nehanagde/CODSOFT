import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 6:
            messagebox.showwarning("Invalid Length", "Password length should be at least 6 characters.")
        else:
            password = generate_password(length)
            label_result.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

window = tk.Tk()
window.title("Neha's Password Generator")

window.geometry("400x300")

label = tk.Label(window, text="Enter the desired length for your password:")
label.pack(pady=10)

entry_length = tk.Entry(window, width=10)
entry_length.pack(pady=10)

generate_button = tk.Button(window, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

label_result = tk.Label(window, text="Generated Password: ", font=("Arial", 12))
label_result.pack(pady=20)

window.mainloop()
