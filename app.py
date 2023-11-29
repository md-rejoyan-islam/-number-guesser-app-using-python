import random ; # import random module

# guess number function between low and high number
def random_number(low, high):
    return random.randint(low, high)



low = 1
high = 50

# generate a random number between low and high
correct_answer = random_number(low, high)

print(correct_answer)
# loop thrpugh 5 times because we have 5 chances to guess the number correctly 
for i in range(5):
    # get a guess number
    guess_number = input(f"Guess a number between {low} and {high}: ")

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
        print("Too high!\n")

    # check if guess number is too low
    elif guess_number < correct_answer:
        print("Too low!\n")

# if user can't guess the number in 5 chances then print the correct answer
print(f"Sorry, you lose. The number was {correct_answer}.\n")
