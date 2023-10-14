import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("400x250")


        ttk.Label(self, text="Password Generator", font=("Arial", 16)).pack(pady=10)


        ttk.Label(self, text="Username:").pack(pady=5)
        self.username_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.username_var).pack(pady=5)


        ttk.Label(self, text="Password Length:").pack(pady=5)
        self.length_var = tk.IntVar(value=12)
        ttk.Spinbox(self, from_=4, to_=32, textvariable=self.length_var, width=5).pack(pady=5)


        ttk.Button(self, text="Generate Password", command=self.generate_password).pack(pady=20)


        self.result_var = tk.StringVar()
        ttk.Label(self, textvariable=self.result_var, font=("Arial", 12)).pack(pady=5)

    def generate_password(self):
        username = self.username_var.get()
        length = self.length_var.get()

        if not username:
            self.result_var.set("Please enter a username!")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.result_var.set(f"Username: {username}\nPassword: {password}")

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()

