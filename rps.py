#Import

from random import randint 

#Create option-list 
t = ['Rock', 'Paper', 'Scissors']

#Assign random play to computer 

#Set player to false 
player = False 

while player == False:
    #Set player to True
    player = input('Rock, Paper, Scissors?')
    if player == computer: 
        print('Tie!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('You lose!', computer, 'covers', player)
        else: 
            print('You win!', player, 'crushes' computer)
    
