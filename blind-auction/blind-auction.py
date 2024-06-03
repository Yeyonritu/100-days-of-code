import arts as art
import os

print(art.logo)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    #from stack overflow 

is_Gone = True #it's a bid... going...going...gone

sealed_auction = {} 

def bid_winner(bidders_secret):
    
     highest_bid = 0
     winner = ""
     for bidder in bidders_secret:
       bid_amount = bidders_secret[bidder]
       if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = bidder 
           print(f"The winner of the auction is {winner} with a bid of ${highest_bid}")

while is_Gone:
    
    auction_bidders = input("What is your name?: ")
    bid_price = int(input("How much do you want to bid?: $"))
    
    sealed_auction[auction_bidders] = bid_price
    
    other_bidders = input("Are there any other bidders? Enter 'yes' or 'no': \n")
    
    if other_bidders == "yes":
        cls()
        
    elif other_bidders == "no":
        cls()
        is_Gone = False
        bid_winner(bidders_secret = sealed_auction)
        
        
        
        
        