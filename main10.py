#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') # displays "Greetings!"
colors = ['red','orange','yellow','green','blue','violet','purple'] #creates a list of colors
play_again = '' #instansiates a variable to whether the player wants to play again
best_count = sys.maxsize # creates a holder for the least amount of guesses it took

while (play_again != 'n' and play_again != 'no'): #loops the indented code if play_again != 'n' AND 'no'
    match_color = random.choice(colors) # assigns a random value from the colors list to the variable
    count = 0 # creates a variable for counting guesses
    color = '' # creates a holder for player input 
    while (color != match_color): # loops while player hasn't guessed the chosen color
        color = input("\nWhat is my favorite color? ") #displays 'What is my favorite color' on a new line
        color = color.lower().strip() #converts color to lowercase and removes all spaces from sides
        count += 1 #adds one to the counting variable
        if (color == match_color): #if the guess is correct...
            print('Correct!')   #display correct
        else:   #else...
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #display a try again statement    
  
      print('\nYou guessed it in {} tries!'.format(count)) # prints the final number of tries correct guess was made

    if (count < best_count):    #if guess was lower then the value of the previous variable...
        print('This was your best guess so far!') #display best guess and...
        best_count = count  #reassign the best_count variable to know the least tries

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #asks if player would like to play again

print('Thanks for playing!') #thanks player for playing