# YZV 104E - TERM PROJECT
# Guess What It Is: Word Guessing Game
## Summary of the project
**Guess What It Is** is a console application of a word guessing game. Basically it has 2 game modes.
1. One-word Mode: Player tries to guess only one word.
2. Four-word Mode: Player tries to guess four words at the same time.

There are 3 word options for both modes.
1. 4-lettered Word
2. 5-lettered Word
3. 6-lettered Word

As the first step, player should choose the game mode and word option. Then the game will start.

Player will begin by writing a guess, then the game will show if the letters in the guess are 
present in the word or not and for the present letters, if their positions are correct or not.
If the letter is in the correct position, the letter's color will be green. If the letter is 
present but not in the correct position, then the letter's color will be yellow.
In each guess, player will try to get closer to the target word/words and guess it correctly in a few tries.
For each word option, there will be different maximum guess numbers. Player will try to guess the word/words
correctly in these tries. If the player can guess the word/words correctly, the player will win, otherwise lose and see 
the correct word/words at the end of the game.

## How to Run the Code
1. Open the requirements.txt file and install the packages that are required to run the project. 
2. Open the terminal in your IDE (e.g. PyCharm)
3. Then navigate to the directory that the source code(python file) is located.
4. Write **python Guess_What_It_Is.py** command to the terminal.
5. Press enter to run the code.


**Note that** there are 3 .txt files (4_lettered_words.txt, 5_lettered_words.txt, 6_lettered_words.txt) 
that are used in this project.
The .txt files should be in the same folder with the .py (Guess_What_It_Is.py) file.


