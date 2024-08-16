import random
from flask import Flask

app = Flask(__name__)

rand_num = random.randint(0, 9)
# rand_num = 5 For testing purposes

@app.route("/")
def home_screen():
    return '<h1>Guess a Number between 0 and 9</h1>' \
           '<img src = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWFseHlqdmtmaGl3YmZqZzM2bmo0Njl2MzZyeXoyYTMwZmcxNzRwbCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26uflDxU6cEhrhmUg/200.webp">'

@app.route("/URL/<int:number>")
def guess_game(number):
    
    if number < rand_num:
        return '<h1 style="color:red;">Too low, Try again!</h1>' \
                '<img src="https://media0.giphy.com/media/2ALdBWhJpGcodDssuR/giphy.webp?cid=790b76110f3ygtqx8g4bgm2xm3sbmncbliww09e3w6k31jhe&ep=v1_gifs_search&rid=giphy.webp&ct=g">'
    
    elif number > rand_num:
        return '<h1 style="color:purple;">Too high, Try again!</h1>'\
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHc0MTFxbDVvd2t1aTRmcDcxaWR0NnEzYjMxNmdleG5uMjQ3NXdzeiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/0aQJL0nm32LTIXus5F/giphy.webp">'
                
    else:
        return '<h1 style="color:green;">You found me!</h1>'\
               '<img src = "https://media0.giphy.com/media/cruO3FTeoAxjiTVxPW/200.webp?cid=790b76114rnicpig0y9sdefxva13r2ohv601ogx6vi7cguyb&ep=v1_gifs_search&rid=200.webp&ct=g">'

if __name__ == "__main__":
    app.run(debug=True)