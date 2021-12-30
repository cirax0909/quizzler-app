from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class Graphical_Ui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 20))
        self.label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=300, highlightthickness=0)

        self.questions = self.canvas.create_text(150, 150, width=280, text='', font=("Arial", 20, "italic"))

        self.canvas.grid(pady=15, column=0, row=1, columnspan=2)
        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false, highlightthickness=0, bg=THEME_COLOR, command=self.check_answer_true)
        self.false_button.grid(padx=20, pady=20, column=1, row=2)
        true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true, highlightthickness=0, bg=THEME_COLOR, command=self.check_answer_true)
        self.true_button.grid(padx=20, pady=20, column=0, row=2)

        self.nxt_question()

        self.window.mainloop()

    def nxt_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            self.label.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions, text=q_text)
        else:
            self.canvas.itemconfig(self.questions, text="You have reached the end of the quiz.")
            self.true_button.configure(state="disabled")
            self.false_button.configure(state="disabled")

    def check_answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def check_answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg='green')
        elif not is_right:
            self.canvas.configure(bg='red')

        self.window.after(1000, func=self.nxt_question)
