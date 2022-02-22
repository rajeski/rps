#Import the following 

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
    elif player == 'Paper':
        if computer == 'Scissors':
            print('You lose!', computer, 'cuts', player)
        else: 
            print('You win!', computer, 'covers', computer)
    elif player == 'Scissors':
        if computer == 'Rock':
            print('You lose!', computer, 'crushes', player)
        else:
            print('You win!', player, 'cuts', computer) 
    else:
        print('That is not a valid option. Please check your spelling!')
    #Player set to True, but to create a loop False allows it to
    #continue
    player = False
    computer = t[randint(0,2)]  
    
