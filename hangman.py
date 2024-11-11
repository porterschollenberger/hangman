import random
import os

def main():
    # Initialize all important variables
    possible_words = ["catfish", "juxtaposition", "horrible", "pyramid", "faint", "insurance", "symptom", "wine", "freeze", "cat"]
    selected_word = random.choice(possible_words)
    running_guess = ["_" for _ in range(len(selected_word))]
    correct_count = 0
    incorrect_count = 0
    incorrect_guesses = []
    guessed = set()

    print("Welcome to Hangman!")
    print(f"The word you will be guessing has {len(selected_word)} letters\n")

    while True:
        guessed_letter = input("Please guess a letter: ").lower()

        # Make sure the user only guesses one letter
        if len(guessed_letter) > 1:
            print("Hang on now! You can only guess one letter at a time!\n")
            continue
        elif not guessed_letter.isalpha():
            print("Oops! That isn't a letter! Try that one again!\n")
            continue
        elif guessed_letter in guessed: # Don't let the user guess the same thing multiple times
            print(f"You have already guessed the letter {guessed_letter}.\n")
            continue

        # Clear the screen after each guess to make the game look more readable
        os.system('clear' if os.name == "posix" else 'cls')

        # See if letter was correct
        if guessed_letter in selected_word:
            print(f"Correct! The word has {selected_word.count(guessed_letter)} {guessed_letter}{'s' if selected_word.count(guessed_letter) > 1 else ''}!\n")
            
            # Go through the word and find all indices where the guessed letter occurs
            for i, letter in enumerate(selected_word):
                if letter == guessed_letter:
                    running_guess[i] = guessed_letter

            correct_count += 1
        else:
            print(f"Sorry! {guessed_letter} is not in the word!\n")
            incorrect_guesses.append(guessed_letter)
            incorrect_count += 1

        # This technically goes against the spec, but because I clear the screen, I want to always show
        # the user their current word and incorrect letters because it's easier to play that way
        # instead of only showing them each when they get it correct or incorrect
        print(''.join(running_guess))
        print("Incorrect letters:", ' '.join(sorted(incorrect_guesses)))

        guessed.add(guessed_letter)

        print(f"Your guesses: {correct_count+incorrect_count} total, {correct_count} correct, {incorrect_count} incorrect.\n\n")

        # Check if the user has guessed the entire word
        if "_" not in running_guess:
            print(f"Congratulations! You've guessed the word {selected_word} in {correct_count+incorrect_count} guesses!\n")
            
            # Get a valid response from the user
            response = ""
            while True:
                response = input("Would you like to keep playing? [Yes/Quit] ").lower()
                if response == "yes" or response == "quit":
                    break
            
            if response == "quit":
                print("Thanks for playing!")
                exit(0)
            elif response == "yes":
                print("Awesome! Let's run it again!\n")

                # Reset all the variables used to play again
                selected_word = possible_words[random.randint(0,9)]
                running_guess = ["_" for _ in range(len(selected_word))]
                correct_count = 0
                incorrect_count = 0
                incorrect_guesses = []
                guessed = set()

                print("Welcome to Hangman!")
                print(f"The word you will be guessing has {len(selected_word)} letters\n")


if __name__ == "__main__":
    main()