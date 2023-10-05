import random
import requests

class Game:
    def __init__(self, playing = True, difficulty = 2):
        self.playing = playing
        self.difficulty = difficulty
        
    def get_word(self):
        '''Return a specific number of words of a specific length from the random word API.
        
        Args:
            self.difficulty (int): Difficulty of the game. 1 = Easy, 2 = Medium, 3 = Hard
            
        Returns:
            words (list): list of words
        '''
        char_num = self.difficulty + 3 # scale up 3 letters per difficulty
            
        response = requests.get(f"https://random-word-api.herokuapp.com/word?length={char_num}")
        
        if response.status_code == 200:
            word = response.json()
            print(word[0])
            return word[0]
        else:
            print("Failed to fetch random words")
        
    def play_game(self, lives):
        '''Initiates Hangman game loop by asking for input and handling replay.
        
        Args:
            word_num (int): Random word fetched
            lives (int): How many attempts the play has to guess the word
            
        Returns:
            None
        '''
        while self.playing:
            word = self.get_word()
            hangman = Hangman(word, lives)
            hangman.ask_for_input()
            inp = input("Play again? (Y/N)").lower()
            if inp.isalpha() and ("y" in inp or "n" in inp):
                if inp == "n":
                    print("Thank you for playing!")
                    self.playing = False
    
class Hangman:
    def __init__(self, word, num_lives = 5):
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = self.fill_empty_list()
        self.num_letters = self.get_unique_letters() 
        self.list_of_guesses = []
    
    def fill_empty_list(self):
        '''Returns a list of underscores the same length as the word.'''
        return ["_"] * len(self.word)
    
    def get_unique_letters(self):
        '''Returns the number of unique letters in the word.'''
        return len(set(self.word))
     
    def check_guess(self, letter):
        '''Checks if the letter is in the word and update the word_guessed list or decrease lives.
        
        Args:
            letter (str): letter to check in word
         
        Returns:
            letter (str): letter to add to list of guesses
        '''
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
        '''Changes the underscore values to the letter if the letter is in the word (even multiple times)
        
        Args:
            letter (str): The letter guessed by player
            
        Returns:
            None
        '''
        word = self.word
        letter_pos_array = [i for i in range(len(word)) if word[i] == letter]
        
        for idx, _ in enumerate(self.word_guessed):
            if idx in letter_pos_array:
                self.word_guessed[idx] = letter
        
        self.num_letters -=1
        print(f"Current Word: {self.word_guessed}")
        
    # Only time we need to check lives is if we decreased them
    def check_lives(self):
        '''Decreases the number of lives and alerts the player of quantity of lives or loss.
        
        Args:
            self.num_lives (int): The number of lives the player has left
          
        Returns:
            None
        '''
        self.num_lives -= 1
        if self.num_lives == 0:
            print("You have Lost all you lives! Play again...")
        else:
            print(f"You have {self.num_lives} left!")
                
    def check_outcome(self):
        '''Checks if the player has won or lost and alerts them of the outcome and word to guess.'''
        if self.num_lives == 0:
            print("Better Luck Next Time!")
            print(f"The actual word was {self.word}!")
        else:    
            print("Congratulations you have won!")
    
    def ask_for_input(self):
        '''Loops user input until word has been guessed or lives has been lost.
        
        Args:
            self.word_guessed (list): list of underscores and filled letters
            self.word (str): word to guess
            self.num_lives (int): number of lives the player has left
        
        Returns:
            None
        '''
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
    
if __name__ == '__main__':
  game = Game(1)
  game.play_game(10)