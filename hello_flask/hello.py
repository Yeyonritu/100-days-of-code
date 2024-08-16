# Name shouldn't be confused with what is imported
#Day 54
import time
from flask import Flask

app = Flask(__name__)

@app.route("/")#Python Decorator
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
            '<p>This is a paragraph</p>' \
            '<img src="https://media3.giphy.com/media/JhqJUTyFPubQs/200.webp?cid=790b7611q1st860k25d7n775o9ofa3ty5mkjj1fn4b5jgmab&ep=v1_gifs_search&rid=200.webp&ct=g" width=200>'

def make_bold(function):
    
    def inner_function():
        return f'<b>{function()}</b>'
        
    return inner_function

def make_emphasis(function):
    
    def inner_function():
        return f'<em>{function()}</em>'
    
    return inner_function

def make_underlined(function):
    
    def inner_function():
        return f'<u>{function()}</u>'
    
    return inner_function

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

#Make sure to stop and refresh the server after a change is made
#Using a debug mode, makes this easier, saving the file is necessary
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you're {number} years old"

if __name__ == "__main__":
    app.run(debug=True)
    

 
#Python Decorator Function   
# def vic_decorator(function):
    
#     def inner_function():
#         time.sleep(5)
#         function()
#         function()
        
#     return inner_function


# @vic_decorator
# def say_dop():
#     print("Drunk on Power part III: Cruyff edition")

# say_dop()
