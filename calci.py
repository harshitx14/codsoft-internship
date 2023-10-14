import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x400")

        self.result_var = tk.StringVar()


        tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4).grid(row=0, column=0, columnspan=4)

       
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 1, 0
        for button in buttons:
            tk.Button(self, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        current = self.result_var.get()
        if char == '=':
            try:
                self.result_var.set(eval(current))
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(current + char)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()