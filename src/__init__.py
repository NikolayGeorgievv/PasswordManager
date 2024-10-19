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


# Create GUI with Tkinter
window = tk.Tk()
window.title("Password Manager")
window.minsize(800, 600)
window.maxsize(800, 600)

# Key phrase input
tk.Label(window, text="Key Phrase:").grid(row=0, column=0)
key_entry = tk.Entry(window)
key_entry.grid(row=0, column=1)

# Description input (optional)
tk.Label(window, text="Description:").grid(row=1, column=0)
desc_entry = tk.Entry(window)
desc_entry.grid(row=1, column=1)

# Generate Password Button
generate_btn = tk.Button(window, text="Generate Password", command=show_password)
generate_btn.grid(row=2, column=1)

window.mainloop()
