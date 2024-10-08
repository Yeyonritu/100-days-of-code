#Catching exceptions

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdfsdf"])
    
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
    
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist. ")
    
# else:
#     content = file.read()
#     print(content)
    
# finally:
#     raise TypeError("This is an error i made up") #Final TypeError
    
# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height shouldn't be over 3 metres.")

# bmi = weight / height ** 2
# print(bmi)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

stop = True
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while stop:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
        
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    
    else:
        stop = False
    


    



