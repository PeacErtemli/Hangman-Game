from english_words import get_english_words_set
import random
from functions import *

word_list = list(get_english_words_set(["gcide"], lower=True))

chosen_word = random.choice(word_list)
display_blanks = "_" * len(chosen_word)

print()
print(chosen_word)
print(len(chosen_word))
print()

print(f"Generated word: {display_blanks}")
guess_letter = input("Guess a letter: ").lower()
print()

if guess_letter in chosen_word:
    index_list = find_indexes(chosen_word, guess_letter)

    display_blanks_list = list(display_blanks)

    for i in index_list:
        display_blanks_list[i] = guess_letter

    display_blanks = "".join(display_blanks_list)
else:
    print(f"None")

print(display_blanks)
