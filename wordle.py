#!/usr/bin/env python3

from colorama import Fore, Back, Style


top_n_words = 50
num_guesses = 6

with open("sherlock.txt", "rt") as f:
    content = f.read()

words = content.split()

import re

m = re.compile(r"[a-z]+$")

words = [word.lower() for word in words if len(word) == 5]
words = [word for word in words if m.match(word)]

from collections import Counter

words = [word[0] for word in Counter(words).most_common(top_n_words)]
words[:5]

import random


import pdb


def check(guess, word):
    result = [0] * len(word)
    letters = list(word)
    correct = 0
    for a in range(len(letters)):

        if guess[a] not in letters:
            result[a] = "X"
        elif guess[a] == letters[a]:
            result[a] = "Y"
            letters[a] = " "
            correct += 1
        else:
            result[a] = "O"
            # Remove the first occurance of this letter from
            # letters to prevent it being flagged as O a subsequent time
            for a in range(len(letters)):
                if letters[a] == result[a]:
                    letters[a] = " "
                    break

    return result, correct


def format_result(result):
    colors = {
        "X": Fore.RED,
        "Y": Fore.GREEN,
        "O": Fore.YELLOW,
    }
    return " ".join([colors[k] + k for k in result] + [Fore.WHITE])


print(
    f"""You get {num_guesses} guesses\n
5 letter words only\n
Y means letter in the right place\n
O means correct letter, wrong place\n
X means miss.
++++++++++++++++++++++++++++++++++++\n\n"""
)
while True:
    word = random.choice(words)
    # word = "while"
    for turn in range(num_guesses):
        guess = input("5 letter word, don't mess it up: ")

        if guess == "!":
            print(word)
            continue
        if len(guess) != 5:
            print("I said five letters!!")
            break
        result, num_correct = check(guess, word)
        print(format_result(result))
        if num_correct == len(word):
            print("Congratluations!!!")
            break
