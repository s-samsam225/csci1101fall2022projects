import re
import random

# Get the answer.
pool_file = open("hangman-sample-answer-pool.txt")

pool_answers = []

pool_answer_line = pool_file.readline()

while pool_answer_line:
    pool_answers.append(pool_answer_line)

    pull_answer_line = pool_file.readline()

pool_file.close()

answer = random.choice(pool_answers)

#answer.upper capitilizes everything
answer = answer.upper()


#Pre-game setup.
answer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        answer_guessed.append(False)
    else: 
        answer_guessed.append(True)


# Game Logic.
num_of_incorrect_guesses = 5
current_incorrect_guesses = 0

letters_guessed = []


# User Game Play Logic.

while current_incorrect_guesses < num_of_incorrect_guesses and False in answer_guessed:
    # Display game summary.
    print(f"Number of incorrect guesses remaining: {num_of_incorrect_guesses - current_incorrect_guesses}")

    print(f"Guessed Letters: ", end="")

    for current_letter_guessed in letters_guessed:
        print(current_letter_guessed, end=" ")

    #here we are not in for loop, but still in while
    print()

    #Display puzzle board
    for current_answer_index in range(len(answer)):
        if answer_guessed[current_answer_index]:
            print(answer[current_answer_index], end=" ")

        else: 
            print("_", end="")

    print()

    #Let user guess the letter.
    letter = input("Enter a letter: ", )

    letter = letter.upper()

    #Check if user entered a valid letter.
    if re.search("^[A-Z]$", letter) and len(letter) == 1 and letter not in letters_guessed:

        # Insert the letter guessed by the user (insertion sort)
        current_letter_index = 0

        for current_letter_guessed in letters_guessed:
            if letter < current_letter_guessed:
                break #break stops the for loop 


            current_letter_index += 1 
        
        letters_guessed.insert(current_letter_index, letter)


        # Check if letter is in the puzzle.
        if letter in answer:
            for current_answer_index in range(len(answer)):
                if letter == answer [current_answer_index]:
                    answer_guessed[current_answer_index] = True

        else:
            current_incorrect_guesses += 1


#Post game summary. 
if current_incorrect_guesses < num_of_incorrect_guesses:
    print("Congratulations, you won!")
else:
    print(f"Sorry, you lost, The answer was {answer}")
        

