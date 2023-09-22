import random

guess = input()
if guess.isalpha() and len(guess) == 1:
    print("Good Guess!")
else:
    print("Oops, that is not a valid input")

word_list = ['banana','apple','pineapple','strawberry','grape']
word = random.choice(word_list)

