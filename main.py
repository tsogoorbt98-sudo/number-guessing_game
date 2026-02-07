import random

def main():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    #  Set the number of guesses allowed
    guess_count = 7
    #  Start the game loop
    # guess = int(input("Guess the number between 1 and 100: "))
    while guess_count > 0:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess == random_number:
            print("Congratulations! You guessed the number! Number: ", random_number)
            break
        else:
            if guess < random_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        guess_count -= 1
        print("You have", guess_count, "guesses left.")

    # Check if the user guessed the number correctly
    if guess != random_number:
        # Inform the user that they ran out of guesses
        print("You ran out of guesses. The number was:", random_number)
# Run the game
main()
# Ask the user if they want to play again
try_again = input("Do you want to play again? (y/n): ")
# If the user wants to play again, call the main function again
if try_again.lower() == "y":
    main()