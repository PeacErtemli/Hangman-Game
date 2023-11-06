def find_indexes(word, letter):  # Finds the index of the letter in the word
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
