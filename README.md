# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Gameplay

1. The game will prompt the user for a single character input.
2. If the guess is incorrect the user will lose a life.
3. If the guess is correct the user will be shown the word with the correctly guessed letters filled in.
4. At the end the user will be shown the word and whether they won or lost.

## Current functionality

1. Random word on every game.
2. Difficulty levels for more or less characters.
3. Iteravely ask the user for a guess.
4. Check whether its in the word or not.
5. If it is in the word, fill in the blanks and show current progress.

## How to Play Linux/Unix

1. Make an environment ```python -m venv /path/to/new/virtual/environment```
2. In Bash/Zsh terminal run env ```source <venv>/bin/activate```
3. and Download ```python -m pip install -r requirements.txt```
4. ```cd ./game``` Run ```./hangman.milestone_5.py```

