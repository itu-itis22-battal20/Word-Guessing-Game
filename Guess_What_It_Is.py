# Aybike Battal
# 150200343
# Term Project - YZV104E

import random
import time
import sys
import colorama
from colorama import Fore
colorama.init(autoreset=True)  # After execution of each line reset the color settings to default

# Print the menu of the game.
# Take input from user unless user enters a valid number according to the commands.
# If user gives an input which is not valid, a warning will be printed.


def menu_of_the_game():
    print("***************************")
    print("WELCOME TO GUESS WHAT IT IS")
    print("***************************")
    print("Press 1 to Play the Game")
    print("Press 2 to Learn How to Play the Game")
    print("Press 3 to Exit the Game")
    while True:
        try:
            users_choice = int(input())
        except ValueError:
            print("Your command is not valid!")
        else:
            if users_choice == 1 or users_choice == 2 or users_choice == 3:
                return users_choice
            else:
                print("Your command is not valid!")


def game_options():  # Print the options in the game
    print()
    print("Choose your game mode and word option")
    print("*************************************")
    print("Game Modes:")
    print("1: One-Word Mode")
    print("2: Four-Word Mode")
    print("------------------")
    print("Word Options:")
    print("1: 4-lettered Word")
    print("2: 5-lettered Word")
    print("3: 6-lettered Word")
    print("------------------")
    print()


def how_to_play_the_game():  # Print the explanation of the game
    print("How to Play Guess What It is?")
    print()
    print("This is a word guessing game.")
    print("The game has two modes: One-Word Mode and Four-Word Mode.")
    print("In one-word mode you are trying to guess only one word.")
    print("In four-word mode you are trying to guess four words at the same time.")
    print("Each time you enter a word, you will see how close is your guess to the correct word.")
    print("If the the letter in your guess is present in the correct word and in the correct position,"
          " it will be printed green.")
    print("If the the letter in your guess is present, however not in the correct position,"
          " it will be printed yellow.")
    print("The game has 3 word options: 4-lettered Word, 5-lettered Word and 6-lettered Word")
    print("First you have to choose the game mode that you want to play.")
    print("Secondly you have to choose the word option that you want to play.")
    print("Then you will start by entering your guess and try to find the word/words correctly!")
    print("Be aware of that you will have limited guesses!")


# Initialize the file that will be used to provide the words, word number which is 1 or 4 according to player's
# choice of the game option, guess number which is the maximum number that player have to guess the word according
# to player's word option mode choice and letter number which is player's word option mode choice.


class WordGuessingGame:
    def __init__(self, filename, word_num, guess_num, letter_num):
        self.filename = filename
        self.word_num = word_num
        self.guess_num = guess_num
        self.letter_num = letter_num
        self.words_lst = self.read_file_and_create_wordlist()
        self.random_words_lst = self.choose_random_word()

# Open the file that will be used to provide the words. In each line of the .txt file, there is one word.
# For each line of the file, read the data and append the word to the words_lst which includes all the n-lettered
# words. n is 4, 5 or 6 according to player's choice and return the list.

    def read_file_and_create_wordlist(self):
        words_lst = []

        with open(self.filename, "r") as file:
            for line in file.readlines():
                line = line.strip()
                words_lst.append(line)

        return words_lst

# Choose random word/words using random function from the words_lst according to player's game mode choice.
# Add the random word/words to the random_word_lst and return the list.

    def choose_random_word(self):

        random_word_lst = random.sample(self.words_lst, self.word_num)

        return random_word_lst

    def players_guess(self):

        # Create an empty set that will include the words that player have guessed correctly.

        correct_words = set()

        # Initialize the guess number of the player with 1.
        # Take the guess of the player until player enters a valid word.
        # If the correct word/words are n-lettered, player must not enter less or more lettered words.
        # Player must enter letters instead of other characters such as punctuation marks and players must enter
        # real words rather than random letters. If the player do not obey these rules, an appropriate
        # warning will be given and the program will take the input guess again.
        # The procedure will be repeated as the number of maximum guess number. After each guess, guess parameter
        # will be increased by 1.

        guess = 1
        for i in range(self.guess_num):
            while True:
                players_guess = input(f"{guess}. Guess: ")
                players_guess = players_guess.upper()
                if len(players_guess) != self.letter_num:
                    print(f"Word must be {self.letter_num}-lettered!")
                elif not players_guess.isalpha():
                    print("Words must be consist of letters!")
                elif players_guess.lower() not in self.words_lst:
                    print("This word is not present in the word list!")
                else:
                    break

            guess += 1

            # Initialize i with 0. While comparing the letter in the guess and random word, we are checking if the
            # letter is in the correct position or not. i helps to compare the positions. When the program
            # is comparing the first letters i must be 0 and in each comparison i will be increased by 1 to check
            # the other letters' positions correctly.
            # Initialize correct_letter_num with 0. This parameter helps to find how many letters in the guess are
            # in the correct position of the random word.

            i = 0
            correct_letter_num = 0

            # Repeat the following steps as the number of word number which is 1 or 4 according to player's game mode
            # choice.
            # Create a word_string which will help to print the player's guess colorful.
            # random_words_lst consists of 1 or 4 words. If the random word is in correct word set which consists of
            # player's correct guesses, print the word and skip the checking process.

            for j in range(self.word_num):
                word_string = ""
                if self.random_words_lst[j] in correct_words:
                    print(Fore.GREEN + self.random_words_lst[j].upper(), end="     ")
                    continue

                # For each letter of the guess, first calculate how many letters in the guess are in the correct
                # position. Then check the letters respectively. If the letter is in the correct position,
                # add the letter to the string in green color. If the letter is present in the random word, but its
                # position is not correct, add the letter string in yellow color. However, the program will check
                # two more properties to print the letter in yellow. The number of corresponding letter in random word
                # should not be equal to the number of the letter in the word_string that we are building up.
                # Because for example, if there is one "A" in the random word but two "A"'s in the guess, just one
                # "A" should be printed in yellow. So, if the number of corresponding letter in random word and
                # in our string are equal, that means as many letters as the number of letters in the random word are
                # added colorfully, so we do not print the other "A"'s yellow, print normal.
                # Also, we have calculated how many letters in the guess are in the correct position of the random word
                # in correct_letter_num parameter. The number of corresponding letter in random word should not be equal
                # to that number. Because for example, if there are 2 "A"s in the random word and in the guess "3" A's,
                # if two A's have correct position, 3rd one should be printed normal not in yellow color.
                # If the letter does not satisfy above properties, add to the string in normal color.
                # After each turn, assign 0 to correct_letter_num, so that for every char, the program can calculate
                # the number of that char(letter) correctly.
                # Print the guess in colorful.

                for char in players_guess:
                    for k in range(self.letter_num):
                        if self.random_words_lst[j][k].upper() == players_guess[k].upper() == char:
                            correct_letter_num += 1

                    if char == self.random_words_lst[j][i].upper():
                        word_string += Fore.GREEN + char

                    elif char in self.random_words_lst[j].upper() \
                            and self.random_words_lst[j].upper().count(char) != word_string.count(char) \
                            and self.random_words_lst[j].upper().count(char) != correct_letter_num:
                        word_string += Fore.YELLOW + char
                    else:
                        word_string += Fore.RESET + char

                    i += 1
                    correct_letter_num = 0
                print(word_string, end="     ")
                i = 0
            print()

            # If the player find correctly any of the words in the random words list, add that word to the
            # correct_words set.

            for m in range(self.word_num):
                if players_guess == self.random_words_lst[m].upper():
                    correct_words.add(self.random_words_lst[m])
                    break

            # If correct words and random words are equal, that means player have found all the words correctly,
            # so finish the game and tell the player that he found the word. While comparing them, convert
            # the random_words_lst to set, so that we can compare the words.

            if correct_words == set(self.random_words_lst):
                print()
                print("CONGRATS!")
                if len(correct_words) == 1:
                    print("You have found the word!")
                elif len(correct_words) == 4:
                    print("You have found all the words!")
                break

            # If user have 1 last chance, warn the user.
            # After each guess, guess parameter increases by 1, so before taking the last guess from user,
            # guess and guess_num(which is the maximum guess) becomes equal.
            # After 2 seconds, the message will disappear.

            if self.guess_num == guess:
                print(Fore.RED + "THIS IS YOUR LAST CHANCE!")
                time.sleep(2)
                sys.stdout.write("\033[F")  # Turn back to the previous line
                sys.stdout.write("\033[K")  # Erase the line

            # When the guess number greater than guess_num(max guess), that means player has no more chances,
            # print the correct word/words, and for the 4 words game mode, print the number of words that player
            # guessed correctly.

            if self.guess_num < guess:
                if self.word_num == 1:
                    print()
                    print("You could not guess the word correctly!")
                    print(f"Correct word is: {self.random_words_lst[0].upper()}")
                    print()
                else:
                    print()
                    if len(correct_words) == 0:
                        print("You could not guess any of the words correctly!")
                    elif len(correct_words) == 1:
                        print(f"You have guessed {len(correct_words)} word correctly!")
                    elif len(correct_words) > 1:
                        print(f"You have guessed {len(correct_words)} words correctly!")
                    print("All the correct words are: ")
                    for word in self.random_words_lst:
                        print(word.upper(), end="     ")
                    print()


if __name__ == '__main__':

    # Print the menu of the game.

    users_choice = menu_of_the_game()

    # According to player's choice, quit the game, give information about the game or start the game.

    while True:

        if users_choice == 3:
            print("You are Quitting the Game!")
            break

        # If player choose to take information about the game, print how to play the game and ask the player
        # if he wants to start the game or exit the game unless the player enters a valid number, otherwise print
        # appropriate warning.

        if users_choice == 2:
            print()
            how_to_play_the_game()
            print()
            print("Press 1 to Start the Game")
            print("Press 3 to Exit the Game")
            while True:
                try:
                    users_choice = int(input())
                except ValueError:
                    print("Your command is not valid!")
                else:
                    if users_choice == 1 or users_choice == 3:
                        break
                    else:
                        print("Your command is not valid!")

        # If user choose to start the game, take game mode and word option choices of the player unless the player
        # enters a valid mode number, otherwise print the appropriate warning.

        if users_choice == 1:

            game_options()

            while True:
                try:
                    game_mode = int(input("Choose the Game Mode That You Want to Play: "))
                except ValueError:
                    print("Please Enter a Valid Number for the Game Mode!")
                else:
                    if game_mode == 1 or game_mode == 2:
                        break
                    else:
                        print("Please Enter a Valid Number for the Game Mode!")

            while True:
                try:
                    word_option = int(input("Choose the Word Option for the Game: "))
                except ValueError:
                    print("Please Enter a Valid Number for the Word Option That You Want to Play!")
                else:
                    if word_option == 1 or word_option == 2 or word_option == 3:
                        break
                    else:
                        print("Please Enter a Valid Number for the Word Option That You Want to Play!")

            # Game mode 1 is one-word mode. According to user's word option choice, send the file,
            # 1 which is the word number, maximum number of guesses and word's letter number to the
            # WordGuessingGame function and start the game.

            if game_mode == 1:

                if word_option == 1:
                    print()
                    print("You have 5 chances to guess the word!")
                    game = WordGuessingGame("4_lettered_words.txt", 1, 5, 4)
                    game.players_guess()
                elif word_option == 2:
                    print()
                    print("You have 6 chances to guess the word!")
                    game = WordGuessingGame("5_lettered_words.txt", 1, 6, 5)
                    game.players_guess()
                elif word_option == 3:
                    print()
                    print("You have 7 chances to guess the word!")
                    game = WordGuessingGame("6_lettered_words.txt", 1, 7, 6)
                    game.players_guess()

            # Game mode 2 is one-word mode. According to user's word option choice, send the file,
            # 4 which is the word number, maximum number of guesses and word's letter number to the
            # WordGuessingGame function and start the game.

            if game_mode == 2:

                if word_option == 1:
                    print()
                    print("You have 7 chances to guess the words!")
                    game = WordGuessingGame("4_lettered_words.txt", 4, 7, 4)
                    game.players_guess()
                elif word_option == 2:
                    print()
                    print("You have 9 chances to guess the words!")
                    game = WordGuessingGame("5_lettered_words.txt", 4, 9, 5)
                    game.players_guess()
                elif word_option == 3:
                    print()
                    print("You have 11 chances to guess the words!")
                    game = WordGuessingGame("6_lettered_words.txt", 4, 11, 6)
                    game.players_guess()

            # After the game finished, ask the player if he wants to start a new game or exit the game unless
            # the player enters a valid command, otherwise give the appropriate warning to the player.

            print()
            print("Press 1 to Start a New Game")
            print("Press 2 to Exit the Game")
            while True:
                try:
                    new_choice = int(input())
                except ValueError:
                    print("Please enter a valid command!")
                else:
                    if new_choice == 1 or new_choice == 2:
                        break
                    else:
                        print("Please enter a valid command!")

            if new_choice == 2:
                print("You are Quitting the Game!")
                break
