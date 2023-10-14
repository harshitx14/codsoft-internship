import tkinter as tk
from tkinter import messagebox

class QuizGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MCQ Quiz")
        self.geometry("400x300")

        self.question_index = 0
        self.score = 0

        self.questions = [
            {
                "question": "what is opposite of come",
                "options": ["go", "here", "far", "play"],
                "answer": 0
            },
            {
                "question": "what is the capital of INDIA",
                "options": ["delhi", "chennai", "nagpur", "mumbai"],
                "answer": 0
            },
            {
                "question": "Who is the prime minister of india",
                "options": ["narender modi", "rahul gandhi", "lalu yadav", "arvind kejriwal"],
                "answer": 0
            },

        ]

        self.question_label = tk.Label(self, text="", wraplength=350, font=("Arial", 12))
        self.question_label.pack(pady=20)

        self.options = []
        for i in range(4):
            var = tk.IntVar(value=0)
            btn = tk.Radiobutton(self, text="", variable=var, value=1, font=("Arial", 12))
            btn.pack(pady=5)
            self.options.append((var, btn))

        self.next_button = tk.Button(self, text="Next", command=self.check_answer)
        self.next_button.pack(pady=20)

        self.display_question()

    def display_question(self):
        if self.question_index < len(self.questions):
            q = self.questions[self.question_index]
            self.question_label.config(text=q["question"])
            for i in range(4):
                self.options[i][1].config(text=q["options"][i], state=tk.NORMAL)
                self.options[i][0].set(0)
        else:
            self.finish_quiz()

    def check_answer(self):
        correct_answer = self.questions[self.question_index]["answer"]
        if self.options[correct_answer][0].get() == 1:
            self.score += 1

        self.question_index += 1
        self.display_question()

    def finish_quiz(self):
        self.next_button.config(state=tk.DISABLED)
        for i in range(4):
            self.options[i][1].config(state=tk.DISABLED)
        messagebox.showinfo("Quiz Finished", f"Your score is {self.score}/{len(self.questions)}!")
        self.destroy()

if __name__ == "__main__":
    app = QuizGame()
    app.mainloop()
