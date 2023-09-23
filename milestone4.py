import random

my_word_list = ['banana','apple','pineapple','strawberry','grape']
random_word = random.choice(my_word_list)

class Hangman:
    '''Define the necessary attributes'''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(self.word_list).lower()
        self.num_lives = num_lives
        self.word_guessed = ['_' if letter.isalpha() else letter for letter in self.word]
        self.num_letters = len(self.word)
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_user_guess(self,user_guess):
        '''A function to check the users guess against the random word'''
        if user_guess in random_word:
            print(f"Good guess! {user_guess} is in the word")
        else:
            print(f"Sorry, guess is not in the word. Try again")

    def ask_for_input(self):
        '''A function to ask for input that accepts a single alphabetical character'''
        while True:
            user_guess = input("Guess a letter: ")
            if user_guess.isalpha and len(user_guess) == 1:
                break
            elif user_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                print("Invalid letter. Please enter a single alphabetical character")
    check_user_guess

