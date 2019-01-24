"""
Hangman.

Authors: Trey Kline and Zane Blair.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
import random

def main():
    num = int(input('Enter the minimum length of the secret word:'))
    secret_word = select_word(num)
    list = []
    for k in range(len(secret_word)):
        list.append('_')
    print(list)
    number_of_guesses = int(input('How many incorrect guesses will you allow yourself? '))
    guess_time(number_of_guesses,secret_word,list)

def select_word(min_letter):
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    while True:
        r = random.randrange(0, len(words))
        item = words[r]
        if(len(item) > min_letter):
            break
    return item

def guess_time(n,word,list):
    incorrect_list =[]
    incorrect_guesses = 0
    while True:
        guess = input('Guess a letter: ')
        n = check_letters(guess,word,n,list,incorrect_list)
        print('Guesses left:', n)
        end = check_victory(list, word)
        if(end == True):
            break
        print('Incorrect letters:' ,incorrect_list,'\n')
        if n == incorrect_guesses:
            game_over(word)
            break

def check_letters(guess,word,n,list,incorrect):
    correct = False
    for k in range(len(word)):
        if(guess == word[k]):
            print('Correct!')
            list[k] = word[k]
            print(list)
            correct = True
    if(correct == False):
        print('Incorrect!')
        print(list)
        incorrect.append(guess)
        n -= 1
    return n

def check_victory(list, word):
    counter = 0
    for k in range(len(list)):
        if str(list[k]) == word[k]:
            counter = counter+1
    if counter == len(word):
        print('Congratulations you have won!!!')
        again = input('Would you like to play again? ')
        if again == 'yes' or again=='Yes':
            print('Playing again \n')
            main()
            return True
        if again == 'No' or again=='no':
            print('See ya! \n')
            return True

def game_over(word):
    print('Game over man!')
    print('The word was:', word)
    again = input('Would you like to play again? ')
    if again == 'yes' or again == 'Yes' or again == 'y':
        print('Playing again \n')
        main()
        return True
    if again == 'No' or again == 'no' or again == 'n':
        print('See ya! \n')
        return True
main()