import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:/Users/myvp1/Documents/CV/US_States_Game/50_states.csv")
state_data = data["state"]
total_states = len(state_data)

guess_num = 0
correct_guesses = []
# answer_state = screen.textinput(title= "Guess the State", prompt="What's another state's name?").title()

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title= f"{guess_num}/{total_states} States Correct", prompt="What's another state's name?").title()
    
    for state in state_data:
        if state == answer_state:
            t =turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.color("black")
            x_cor = int(data[data.state == state].x)
            y_cor = int(data[data.state == state].y)
            t.goto(x_cor, y_cor)
            t.write(f"{state}", True, "center", font = ("Arial", 6, "normal"))
            correct_guesses.append(state)
            guess_num += 1
            
    if answer_state == "Exit":
        break
                   
    if guess_num == 50:
        game_is_on = False
            
print(correct_guesses)

data_dict = {}
to_csv = []
for state in state_data:
    
    if state not in correct_guesses:
        to_csv.append(state)
        data_dict = {
            "Remaining States": to_csv
            }

csv_file = pandas.DataFrame(data_dict)
csv_file.to_csv("states_to_learn.csv")