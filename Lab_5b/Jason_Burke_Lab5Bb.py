#import the random function
import random

#define the main method
def main():
    #set to y to enter the while loop
    play_again = 'y'

    #generate a random number and set total_guesses
    rand_num = random.randint(1, 1000)
    total_guesses = 1 
    #while user wants to continue game,
    #get imput from user trying to guess the random number generated
    while play_again == 'Y' or play_again == 'y':
      

        #get guess from user
        guess = int(input("\nI'm thinking of a number between 1 and 1000."
                          ' Try and guess it! '))
        #output a message to user giving them a hint as to how
        #close they are to the generated number
        if guess >= rand_num + 10:
            print('Too High!')
        elif guess > rand_num and guess < rand_num + 10:
            print('Getting warm but still high!')
        elif guess <= rand_num - 10:
            print('Too Low!')
        elif guess < rand_num and guess > rand_num - 10:
            print('Getting warm but still Low!')
        elif guess == rand_num:
            print('You rock!  You guessed the number in',
                  total_guesses, 'tries!')
            play_again = str(input('\nWould you like to play again? Enter '\
                                   'Y for yes and N for no: '))
            if play_again == 'n' or play_again == 'N':
                print('Good Bye!')
            elif play_again == 'y' or play_again == 'Y':
                #generate new random number and reset guess counter
                rand_num = random.randint(1, 1000)
                total_guesses = 0
        #track the total guesses
        total_guesses+=1

main()
