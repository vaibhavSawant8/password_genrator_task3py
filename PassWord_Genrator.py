import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import string
import random

class Password_Generator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator Using Python Task No 4")
        self.password_length = tk.IntVar()
        self.use_special_chars = tk.BooleanVar()
        self.generated_password = tk.StringVar()
        self.password_length.set(12)
        self.use_special_chars.set(True)
        self.create_widgets()

    def create_widgets(self):
        length_label = ttk.Label(self.root, text="Password Length:")
        length_label.grid(row=0, column=0, padx=10, pady=5)

        self.length_entry = ttk.Entry(self.root, textvariable=self.password_length)
        self.length_entry.grid(row=0, column=1, padx=10, pady=5)

        special_chars_check = ttk.Checkbutton(self.root, text="Include Special Characters", variable=self.use_special_chars)
        special_chars_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        
        generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.password_label = ttk.Label(self.root, textvariable=self.generated_password, font=("Arial", 12), wraplength=300)
        self.password_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def generate_password(self):
        length = self.password_length.get()
        use_special_chars = self.use_special_chars.get()

        charset = string.ascii_letters + string.digits
        if use_special_chars:
            charset += string.punctuation

        try:
            password = ''.join(random.choice(charset) for _ in range(length))
            self.generated_password.set(password)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = Password_Generator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
