from number_game_art import logo
import random

hard_lives = 5
start = 1
end = 100
welcome_message = """Welcome to the Vault Number guessing Game, Guess right to get the priviledge of being in either a regular or premium vault.\nI'm thinking of a number between 1 and 100."""
random_number = random.randint(start, end)

#Function to determine the output of the wrong guesses
def wrong_guesses(user_guess, number, lives):
    
    if lives > 1 and user_guess < number:
        print(f"Too low.\nGuess again")
        
    if lives > 1 and user_guess > number:
        print(f"Too high.\nGuess again")
        
    if lives == 1 and user_guess < number:
        print(f"Too low. \nYou've run out of guesses, you lose, the number was {number}.")
        
    elif lives == 1 and user_guess > number:
        print(f"Too high. \nYou've run out of guesses, you lose, the number was {number}.")
        
    
print(logo)
print(welcome_message)
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    easy_lives = 10
    is_running = True
    while is_running:
        print(f"You have {easy_lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if easy_lives == 1:
            is_running = False
        
        if guess == random_number:
            print(f"You got it! the answer was {guess}")
            is_running = False
        
        else:
            wrong_guesses(guess, random_number, easy_lives)
    
        easy_lives -= 1

elif difficulty == "hard":
    hard_lives = 5
    is_running = True
    while is_running:
        print(f"You have {hard_lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if hard_lives == 1:
            is_running = False
        
        if guess == random_number:
            print(f"You got it! the answer was {guess}")
            is_running = False
        
        else:
            wrong_guesses(guess, random_number, hard_lives)
    
        hard_lives -= 1

