# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## Table of Contents:
- Milestone 1: Set up the environment
- Milestone 2: Create the variables for the game
- Milestone 3: Check if the guessed character is in the word
- Milestone 4: Create the game class
- Milestone 5: Putting it all together

### Project description:

1. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.
1. I've learnt how to define a class and the importance of __init__.
1. I've also learnt how to create a for loop to flick through each letter and check if the user's guess is in the randomly chosen letter.
1. I've learnt how to build up the else block and how easy it is to reduce number of lives by 1, given the number of lives were defined in the parameters of __init__.
1. I've realised that the **while** loop only needed to be in play_game as this allowed me to **break** if the user won or lost, or re-entered the user_guess if they still had lives. I had a **while** loop in user_guess which created an infinite loop with no way for the user to break out.

### Installation Instructions
Either run the code using the 'play' button or shift+enter if you're in the file, or by calling the file 'python milestone5.py'.

### Usage Instructions
Number of lives = 5
Choose a random letter of your choice and press enter. Don't worry if you choose the same letter twice, as this doesn't take a life away and you'll be prompted to choose a different letter. 

#### Milestone 1
A task to set up gitHub for this task and ensure the local and remote versions of these repos are up-to-date.

#### Milestone 2
How to use the .random function with a [list] of words that I've defined. Ask the user for an input, checking that the input is a single character.

#### Milestone 3
Iteratively check if the guess is valid, using a **while** loop. If the guess is valid use **break** and, if not, print an error message. If the code is a mess, define functions to help but be careful with the order of functions, calling one function in another to make sure they both run.

#### Milestone 4
I've now created the Hangman class with the attributes and methods needed to run the Hangman game. I have defined what to do if the letter is guessed correctly (a message to say it's in the word), and what to do if it is guessed incorrectly (a message whilst reducing the number of lives from 5).

#### Milestone 5
Putting it all together - This is where we coded the logic of the game to allow the user to enter a **while** loop that either told them they won, told them they lost or called the user_guess function to continue with the game.

##### License - ?