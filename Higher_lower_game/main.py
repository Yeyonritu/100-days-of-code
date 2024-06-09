import game_data
import game_art
import random
import os

data = game_data.data
logo = game_art.logo

def select_candidate():
    random_data = data[random.randint(0, len(data) - 1)]
    return random_data
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def display_candidate(person, comparism_label):
    name = person["name"]
    description = person["description"]
    country = person["country"]
    print(f"{comparism_label}: {name}, a {description}, from {country}.")
    
def compare_candidate(person1, person2, user_input):

    follower_count1 = person1["follower_count"]
    follower_count2 = person2["follower_count"]
    
    if user_input == "A": 
        return follower_count1 > follower_count2
    
    elif user_input == "B":
        return follower_count2 > follower_count1 
    
    else:
        return False
    
# def lil_helper(person):
#     ggs = person["follower_count"]
#     print(f"psst... follower count is {ggs}")
     
      
is_running = True
celebrity1 = select_candidate()
final_score = 0

while is_running:
    
    print(logo)
    
    celebrity2 = select_candidate()
    
    if celebrity1 == celebrity2:
        celebrity2 = select_candidate()
    
    display_candidate(celebrity1, "Compare A")
    #lil_helper(celebrity1)
    print(game_art.vs)
    display_candidate(celebrity2, "Compare B")
    #lil_helper(celebrity2)
    
    more_popular = input("Who has more followers? Type 'A' or 'B': ").upper()
    compare_candidate(celebrity1, celebrity2, more_popular )
    
    if compare_candidate(celebrity1, celebrity2, more_popular) == True:
        cls()
        final_score +=1
        celebrity1 = celebrity2
        print(f"You're right! Final score: {final_score}")
        
    elif compare_candidate(celebrity1, celebrity2, more_popular ) == False:
        is_running = False
        print(logo)
        print(f"Sorry, that's wrong. Final score: {final_score}")
    
