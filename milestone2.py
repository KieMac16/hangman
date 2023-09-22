import random

user_guess = input()
if user_guess.isalpha() and len(user_guess) == 1:
    print("Good Guess!")
else:
    print("Oops, that is not a valid input")

word_list = ['banana','apple','pineapple','strawberry','grape']
word = random.choice(word_list)

