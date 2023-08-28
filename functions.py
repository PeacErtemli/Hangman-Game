from english_words import get_english_words_set
import random
import time
import keyboard


def find_indexes(word, letter):
    index_list = []

    for i in range(len(word)):
        if word[i] == letter:
            index_list.append(i)

    return index_list


hangman = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

           "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

           "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

           "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

           "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

           "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

           "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]  # 6 lives
