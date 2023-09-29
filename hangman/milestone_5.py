import random
import requests

class Game:
    def __init__(self, playing = True):
        self.playing = playing
        
    def get_words(self, word_num):
        response = requests.get(f"https://random-word-api.herokuapp.com/word?number={word_num}")
        
        if response.status_code == 200:
            words = response.json()
            return words
        else:
            print("Failed to fetch random words")
        
    def play_game(self, word_num, lives):
        words = self.get_words(word_num)
        while self.playing:
            hangman = Hangman(words, lives)
            hangman.ask_for_input()
            inp = input("Play again? (Y/N)").lower()
            if inp.isalpha() and ("y" in inp or "n" in inp):
                if inp == "n":
                    print("Thank you for playing!")
                    self.playing = False
    
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_word()
        self.word_guessed = self.fill_empty_list()
        self.num_letters = self.get_unique_letters() 
        self.list_of_guesses = []
    
    def choose_word(self):
        return random.choice(self.word_list)
    
    def fill_empty_list(self):
        return ["_"] * len(self.word)
    
    def get_unique_letters(self):
        return len(set(self.word))
     
    def check_guess(self, letter):
        letter = letter.lower()
        if letter in self.word:
            print(f"Good Guess! {letter} is in the word")
            self.correct_letter(letter)
        else:
            print(f"Sorry {letter} is not in the word.")
            self.check_lives()

        return letter

    # get all indexes where the letter is in word and change each index instance
    def correct_letter(self, letter):
        word = self.word
        letter_pos_array = [i for i in range(len(word)) if word[i] == letter]
        
        for idx, _ in enumerate(self.word_guessed):
            if idx in letter_pos_array:
                self.word_guessed[idx] = letter
        
        self.num_letters -=1
        print(f"Current Word: {self.word_guessed}")
        
    # Only time we need to check lives is if we decreased them
    def check_lives(self):
        self.num_lives -= 1
        if self.num_lives == 0:
            print("You have Lost all you lives! Play again...")
        else:
            print(f"You have {self.num_lives} left!")
                
    def check_outcome(self):
        if self.num_lives == 0:
            print("Better Luck Next Time!")
            print(f"The actual word was {self.word}!")
        else:    
            print("Congratulations you have won!")
    
    def ask_for_input(self):
        while ("".join(self.word_guessed) != self.word) and (self.num_lives != 0):
            letter = input("Please guess a letter from the word im thinking off...")    
            if not (len(letter) == 1 and letter.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")    
            elif letter in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
              guess = self.check_guess(letter)
              if guess not in self.list_of_guesses:
                  self.list_of_guesses.append(guess)
                  
        self.check_outcome()
    
    
game = Game()
game.play_game(10, 10)