import random

my_word_list = ['banana','apple','pineapple','strawberry','grape']
random_word = random.choice(my_word_list)

def check_user_guess(user_guess):
    if user_guess in random_word:
        print(f"Good guess! {user_guess} is in the word")
    else:
        print(f"Sorry, guess is not in the word. Try again")

def ask_for_input():
    while True:
        user_guess = input("Guess a letter: ")
        if user_guess.isalpha and len(user_guess) == 1:
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character")
    check_user_guess(user_guess)

ask_for_input()