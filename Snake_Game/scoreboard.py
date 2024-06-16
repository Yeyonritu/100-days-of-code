from turtle import Turtle
class Scoreboard(Turtle):
    def __init__ (self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Your Score: {self.score} ", True, "center", font = ("Arial", 15, "normal"))        
    
    def score_increase(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Your Score: {self.score} ", True, "center", font = ("Arial", 15, "normal"))
          
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, "center", font = ("Arial", 15, "normal") )
        