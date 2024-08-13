# Name shouldn't be confused with what is imported
import time
from flask import Flask

app = Flask(__name__)

@app.route("/")#Python Decorator
def hello_world():
    return "Hello, World!"

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()
 
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