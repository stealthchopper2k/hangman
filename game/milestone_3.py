import random

word_list = ["banana", "apple", "cherry", "raspberry", "blueberry"]

word = random.choice(word_list)    

def ask_for_input():
    while True:
        letter = input("Please guess a letter from the word im thinking off...")    
        if len(letter) == 1 and letter.isalpha():
            check_guess(letter)
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
        

def check_guess(letter):
    letter = letter.lower()

    if letter in word:
        print(f"Good Guess! {letter} is in the word")
    else:
        print(f"Sorry {letter} is not in the word. Try again")
        
        
ask_for_input()