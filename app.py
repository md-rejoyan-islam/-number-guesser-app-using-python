import random ; # import random module

# guess number function between low and high number
def random_number(low, high):
    return random.randint(low, high)



low = 1
high = 50

# generate a random number between low and high
correct_answer = None   ;

# user get chances to guess the number
get_chances = 5

# game restart function
def game_restart(get_chances,correct_answer):
    restart = input("Would you like to play again? (Y/N): ")
    if restart.lower() == "y":
        game_start(get_chances)
    else:
        print("\nThanks for playing!")
        # if user can't guess the number in 5 chances then print the correct answer
        print(f"Sorry, you lose. The number was {correct_answer}.\n")
        exit()



# game start function
def game_start(get_chances = 5):

    # correct answer
    correct_answer = random_number(low, high)
    print(correct_answer)
# loop thrpugh 5 times because we have 5 chances to guess the number correctly 
    for i in range(get_chances):
        # get a guess number
        guess_number = input(f"\nGuess a number between {low} and {high}:")

        # check if guess number is valid
        if guess_number.isnumeric():
            guess_number = int(guess_number)
        else:
            print("Numbers only, please!\n")
            exit()

        # check if guess number is in range
        if guess_number < low or guess_number > high:
            print(f"Must be between {low} and {high}\n")
            exit()

        # check if guess number is correct
        if guess_number == correct_answer:
            print("You win!\n")
            exit()

        # check if guess number is too high
        elif guess_number > correct_answer:
            print("\nToo high!")

        # check if guess number is too low
        elif guess_number < correct_answer:
            print("\nToo low!")
        
        # if user can't guess the number in 5 chances then print the correct answer
        if i == int(get_chances) - 1:
            print(f"Sorry, you lose. The number was {correct_answer}.\n")

            # restart the game
            game_restart(get_chances=5,correct_answer=correct_answer)
        
        # print the remaining chances
        else:
            print(f"You have {get_chances - (i + 1)} guesses left.\n")

        


# game start function call
game_start(get_chances=5)


