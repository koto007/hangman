import random

def hangman(): 
    word_list = ["rose","green", "bleu"]
    random_number = random.randint(0,2)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["",
              "_____      ",
              "|    |     ",
              "|    |     ",
              "|    o     ",
              "|   /|\    ",
              "|   / \    ",
              "|          "
              ]
    remaining_letters = list(word)
    letter_board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    while wrong_guesses < len(stages) - 1:
        print("\n")
        guess = input("guess a letter")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print(" ".join(letter_board))
        e = wrong_guesses + 1
        print("\n".join(stages[0:e]))
        if "_" not in letter_board:
            print("T'as gangé! Le mot était")
            print(" ".join(letter_board))
            win = True
            break
    if not win:
         print("\n".join(stages[0:wrong_guesses]))
         print("T'as perdu, la réponse était {}.".format(word))

hangman()