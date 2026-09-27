# Python Hangman Game

An interactive command-line Hangman game built in Python featuring randomized word selection, input validation, a warning system, and score calculation.

## Overview

This project implements the classic Hangman word game in Python. A word is randomly selected from a word list, and the player attempts to reveal the word by guessing one letter at a time.

The program tracks guesses, validates user input, displays remaining letters, and calculates a final score when the player successfully completes the word.

## Features

- Random word selection from a word list
- Interactive command-line gameplay
- Tracks guessed and available letters
- Displays partially completed words
- Accepts uppercase and lowercase guesses
- Handles invalid and repeated inputs with a warning system
- Different penalties for incorrect vowels and consonants
- Calculates a score based on remaining guesses and unique letters
- Option to play again after each game

## How It Works

The game is organized using several helper functions:

- `is_word_guessed()` — determines whether the player has completed the word
- `get_guessed_word()` — displays the current state of the hidden word
- `get_available_letters()` — tracks letters that have not yet been guessed
- `hangman()` — controls the main game logic and user interaction

## Technologies

- Python
- Python Standard Library (`random`, `string`)

## Running the Game

1. Clone or download this repository.
2. Make sure `hangman_ovalle.py` and `words.txt` are in the same directory.
3. Open a terminal in that directory.
4. Run:

   python hangman_ovalle.py

5. Follow the prompts to play.
