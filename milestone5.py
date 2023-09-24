import random

class Hangman:
    '''Define the necessary attributes, using self as the first parameter'''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list).lower()
        self.num_lives = num_lives
        self.word_guessed = ['_' if letter.isalpha() else letter for letter in self.word]
        self.num_letters = len(self.word)
        self.list_of_guesses = []
    
    def check_user_guess(self,user_guess):
        '''A function to check the users guess against the random word
        
        If the guess is correct, a message states this. If not, number of lives are reduced by 1'''
        if user_guess in self.word:
            print(f"Good guess! {user_guess} is in the word")
            for index, letter in enumerate(self.word):
                if letter == user_guess:
                    self.word_guessed[index] = user_guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {user_guess} is not in the word. Try again")
            print (f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''A function to ask for input that accepts a single alphabetical character and returns the check_user_guess function'''
        user_guess = input("Guess a letter: ")
        if not user_guess.isalpha or len(user_guess) != 1:
            print("Invalid letter. Please enter a single alphabetical character")
        elif user_guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_user_guess(user_guess)
            self.list_of_guesses.append(user_guess)

def play_game(word_list):
    hangman_game = Hangman(word_list,num_lives=5)
    while True:
        if hangman_game.num_lives == 0:
            print("You have lost!")
            break
        elif hangman_game.num_letters > 0:
            hangman_game.ask_for_input()
        else:
            hangman_game.num_lives > 0 and hangman_game.num_letters < 1
            print("Congratulations, you've won!")
            break

if __name__ == '__main__':        
    my_word_list = ['banana','apple','pineapple','strawberry','grape']
    play_game(my_word_list)