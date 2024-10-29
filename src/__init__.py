import hashlib
import tkinter as tk
from tkinter import messagebox


def generate_password(keyphrase, description=""):
    combined_input = keyphrase + description
    hashed = hashlib.sha256(combined_input.encode('utf-8')).hexdigest()
    return hashed[:20]  # First 20 characters


def show_password():
    keyphrase = key_entry.get()
    description = desc_entry.get()
    if keyphrase:
        password = generate_password(keyphrase, description)
        messagebox.showinfo("Generated Password", f"Password: {password}")
    else:
        messagebox.showwarning("Input Error", "Please enter a key phrase")


def show_info():
    messagebox.showinfo("How to Use", "This app helps you manage passwords. "
                                       "Enter a key phrase and an optional description, then click 'Generate Password'.")

window = tk.Tk()
window.title("Password Manager")
window.minsize(800, 600)
window.maxsize(800, 600)

frame = tk.Frame(window)
frame.grid(row=0, column=0, padx=20, pady=20)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

input_frame = tk.Frame(frame)
input_frame.pack(pady=(0, 20))

tk.Label(input_frame, text="Key Phrase:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
key_entry = tk.Entry(input_frame)
key_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Description:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
desc_entry = tk.Entry(input_frame)
desc_entry.grid(row=1, column=1, padx=5, pady=5)

button_frame = tk.Frame(frame)
button_frame.pack()

generate_btn = tk.Button(button_frame, text="Generate Password", command=show_password)
generate_btn.grid(row=0, column=0, pady=(10, 0))

info_button = tk.Button(button_frame, text="INFO", command=show_info)
info_button.grid(row=0, column=1, padx=10)

window.mainloop()
