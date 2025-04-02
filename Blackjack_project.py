#Blackjack project

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


#def win_condition(your_score, computer_score):
 #   print(f'Your score is {your_score}, the computers score is {computer_score}') 
  #  if your_score > computer_score and your_score < 21:
   #     print(f'Your total score is {your_score}, computer score is {computer_score} you win!') 
   # elif your_score > 21 and computer_score <= 21: 
   #     print(f'haha you loseeeer score {your_score}, computer wins score {computer_score}')
   # elif your_score == 21:
   #     print(f'yay you win! your score: {your_score}, computer score: {computer_score}')
   # else: 
   #     print(f'You lose! your score: {your_score}, computer score: {computer_score}')
    
    #def more_cards():
    #    play_again = input('Do you want another card, you greedy bastard? y/n')
    #    if play_again == 'y':
    #        update_cards()
    #    else: 
    #        winner()

'''make a while loop for the computer cards, if computer_score < 17 then check if score is > 21 '''                      


'''===================================================START HERE ============================================================================'''

import random
 
def draw_card():                                            #select two random cards 
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
    
def update_score(cardy):                                    #calculate the sum of cards ###of the whole list????
    return sum(cardy)

winner = 'none'

                                           #main function, hands out cards, appends cards to hand, updates score after each round 
your_cards = [draw_card(), draw_card()]
your_score = update_score(your_cards)
another_card = ""
    
computer_cards = [draw_card(), draw_card()]
computer_score = update_score(computer_cards)

def Blackjack(another_card, winner, your_score): 
    
    def computer_turn(computer_cards, winner):
        while computer_cards < 17:
            computer_cards.append(draw_card())
            computer_score = update_score(computer_cards)
        if computer_score > 21: 
            winner = 'you'
        else:
            winner = 'computer'
              
    def update_cards(your_score):        
        your_cards.append(draw_card())
        your_score = update_score(your_cards)
    
    def early_win(winner):                                            #check if someone already has 21
        if your_score == 21:
            winner = 'you'
        elif computer_score == 21: 
            winner = 'computer '    

    def ace(your_score, your_cards):                                #check if score is > 21 and makes 11 into 1 
        if 11 in your_score and your_cards > 21:
            your_new_score = your_score-10 

        update_cards(your_new_score)
        early_win(your_new_score)
        ace(your_new_score)
    
    early_win(winner)    
    update_cards(your_score)

    def get_another_card(another_card):
        another_card = input(f' your cards are {your_cards}, your total score is {your_score}, computer card is {computer_cards[0]}, do you want another card? y/n')
    
    get_another_card(another_card)
    
    while another_card == 'y':                          #if you want another card, do it again 
        update_cards(your_score)
        another_card = get_another_card()
        computer_turn()
        print(another_card)
        

def win_condition(your_score, computer_score):
    if your_score > computer_score:
       winner = 'you'
    elif your_score > 21:
        winner = 'computer'
    else: 
        winner = 'computer'

    
    def winner(your_score, computer_score):
        if winner == 'you':
            print(f'You win, your score is {your_score}, computer score is {computer_score}')
        elif winner == 'computer':
            print(f'you loseeeeeee, your score is{your_score}, computer score is {computer_score}') 
        else:
            print('Its a draw!')

def main():
    play = input('Do you want to play a game of Blackjack? y/n \n')
    if play == 'y':
        Blackjack(another_card, winner, your_score)
    else:
        pass
        
if __name__ == '__main__':
    main()




















##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.