from functions import *

print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)

time.sleep(0.5)

word_list = list(get_english_words_set(["gcide"], lower=True))
chosen_word = random.choice(word_list)

display_blanks = "_" * len(chosen_word)
guessed_list = []

end_of_game = False
lives = 6

while not end_of_game:

    print("-----------------------------------------------------------------------------------------------------------")
    print(hangman[6 - lives])
    print(f"Generated word: {display_blanks}")
    print("=========")
    print("Guessed list: ", end="")
    print(*guessed_list, sep=", ")
    guess_letter = input("Guess a letter: ").lower()

    os.system('cls')

    if guess_letter == "help":
        print("                                  ")
        print(chosen_word)
        print(len(chosen_word))
        continue

    if len(guess_letter) == 1:
        if guess_letter not in guessed_list:
            guessed_list.append(guess_letter)
        else:
            print("                                  ")
            print("                                  ")
            print("                                  ")
            print("                                  ")
            print("                                  ")
            print("                                  ")
            print("You already guessed it.")
            print("                                  ")
            time.sleep(1)
            continue
    else:
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("Please enter a letter, not a word.")
        print("                                  ")
        time.sleep(2)

    if guess_letter in chosen_word:
        index_list = find_indexes(chosen_word, guess_letter)

        display_blanks_list = list(display_blanks)

        for i in index_list:
            display_blanks_list[i] = guess_letter

        display_blanks = "".join(display_blanks_list)
    else:
        lives -= 1
        if lives == 0:
            print(hangman[6])
            print()
            print("You lost.")
            print(f"The word was: {chosen_word}")
            end_of_game = True

    if "_" not in display_blanks:
        print("You've won!")
        print(f"The word was: {chosen_word}")
        end_of_game = True
