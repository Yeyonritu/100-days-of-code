import random
import hangman_words as list
import hangman_art as art
#Day 7 

word_list = list.word_list
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
end_of_game = False
lives = 6
print(art.logo)

#Create blanks
display = []

for letter in chosen_word:

    display.append("_")

while not end_of_game:

    user_guess = input("Guess the letter: ")
    guess = user_guess.lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        
        lives -= 1 
        print(f"You're guess {guess} is not a letter in the given word. You've lost a life")
        if lives == 0:
            end_of_game = True
            
            print("You lose.")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
        
    print(art.stages[lives])
