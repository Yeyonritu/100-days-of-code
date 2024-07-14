from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Quiz Questions Here", width=280, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.score_label = Label()
        self.score_label.config(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        
        self.right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_img, highlightthickness=0, command=self.is_True)
        self.right_button.grid(column=0, row=2)
        
        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.is_False)
        self.wrong_button.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
        
    def is_True(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def is_False(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
         
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the End of the quiz!")
            self.is_True(state = "disabled")
            self.is_False(state = "disabled")