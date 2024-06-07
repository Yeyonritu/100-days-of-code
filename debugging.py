""""
How to remove bugs from code.
1. Describe the Problem

"""
############DEBUGGING#####################

# # Describe Problem
#def my_function():
    #The problem here is that the range function can only start from 1 and stop at 19, the person needs
    #to add +1 to it to let the function work
#     for i in range(1, 20 + 1):
#      if i == 20:
#        print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# error_index = 6
# print(dice_imgs[dice_num])
# Error was reproduced by setting index to 6

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994: #This line was ">" 1994, it needed the ">="
#   print("You are a Gen Z.")

# Fix the Errors
# age = int(input("How old are you?")) no int
# if age > 18:
#     print(f"You can drive at age {age}.") no f

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) had ==
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)# was previously wrongly indented, wasn,t adding as it was multiplying
#   print(b_list)

# mutate([1,2,3,5,8,13])

# Take a Break
# Ask a Friend
# Run your code as often as possible(At every execution)
# Ask chatgpt, stack overflow as well as other helpful sites 