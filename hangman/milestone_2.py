import random

word_list = ["banana", "apple", "cherry", "raspberry", "blueberry"]

word = random.choice(word_list)    

guess = input("Please input a single character...")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")
    
print(word_list)
print(word)