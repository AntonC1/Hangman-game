import random


def get_word():
    with open("words.txt") as f:
        word_list = f.read().splitlines()
    word_chosen = random.choice(word_list)
    return word_chosen.upper()


def lives():
    print("Let's play Hangman!\tDifficult levels:")
    print(
        "\t1. Normal (6 lives)\n\t2. Hard (4 lives)\n\t3. Hardcore (2 lives)\n\t4. Hell (1 lives)")
    user_setting = input("Type number of level you want to chose: ")
    if str(user_setting) == "1":
        number_of_lives = 6
        print("\nYou have chosen %s and will receive %d lives." % ("Normal", number_of_lives))
    elif str(user_setting) == "2":
        number_of_lives = 4
        print("\nYou have chosen %s and will receive %d lives." % ("Hard", number_of_lives))
    elif str(user_setting) == "3":
        number_of_lives = 2
        print("\nYou have chosen %s and will receive %d lives." % ("Hardcore", number_of_lives))
    elif str(user_setting) == "4":
        number_of_lives = 1
        print("\nYou have chosen %s and will receive %d lives." % ("Hell", number_of_lives))
    else:
        number_of_lives = 6
        print(
            "\nYou have made an incorrect selection and will automatically be at Normal level which means you will "
            "have "
            "%d life." % number_of_lives)
    return number_of_lives


def play(word_chosen, number_of_lives):
    word_completion = "_" * len(word_chosen)
    guessed = False
    guessed_letters = []
    guessed_words = []
    print(display_hangman(number_of_lives))
    print(word_completion)
    print("\n")
    while not guessed and number_of_lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word_chosen:
                print(guess, "is not in the word.")
                number_of_lives -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word_chosen) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word_chosen) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word_chosen:
                print(guess, "is not the word.")
                number_of_lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word_chosen
        else:
            print("Not a valid guess.")
        print(display_hangman(number_of_lives))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + "'" + word_chosen + "'" + ". Maybe next time!")


def display_hangman(number_of_lives):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """,
    ]
    return stages[number_of_lives]


def main():
    word_chosen = get_word()
    number_of_lives = lives()
    play(word_chosen, number_of_lives)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word_chosen = get_word()
        number_of_lives = lives()
        play(word_chosen, number_of_lives)


if __name__ == "__main__":
    main()
