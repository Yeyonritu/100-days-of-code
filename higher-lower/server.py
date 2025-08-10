from flask import Flask
import random

app = Flask(__name__)
rand_num = random.randint(0, 10)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src = https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2RpbTg0M2IyN3d0YnNpaWg4ZzE1eWNxeW4yMHJqeWU4ZGVjbHdzMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PINwITJa3v5RJimYHA/giphy.gif>'

@app.route('/<int:number>')
def rand(number):
    if number < rand_num:
        return '<h1 style = "color: red">Too low! Try Again</h1>' \
                '<img src = https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNm5sYXE0Y3N1cTl1eDR3bTR2NjAwbWJmc2xjaXc0MnV3ejFueThkYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/s1MX7LfOn5nhTyb0dy/giphy.gif>'
    
    elif number > rand_num:
        return '<h1 style = "color: red">Too high! Try Again</h1>' \
                '<img src = https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3A1bG5hc2RzZmdmNXp3eW9iNmY4NWZiNnlub21pMHYwb29wcnRjdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2cei8MJiL2OWga5XoC/giphy.gif>'

    else:
        return '<h1 style = "color: green">Exactly Right</h1>' \
                '<img src = https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDcwdnMwYmp4cW9nNXV5YW80eXVleXppcmhyOXVleThpOTNrZTNwZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UAXK9VGoJTbdcPgmcJ/giphy.gif>'     

if __name__ == "__main__":
    app.run(debug=True)

