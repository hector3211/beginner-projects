import random


def pick_number():
    number = random.randint(1,101)
    return number


def play():
    number = pick_number()
    number_of_guesses = 0
    difficulty = input("do you want 'easy' or 'hard' :\n ")
    if difficulty == 'easy':
        number_of_guesses = 10
    elif difficulty == 'hard':
        number_of_guesses = 5
        
    while number_of_guesses != 0:
        user_input = int(input("enter a number you think it is! : \n"))
        if user_input == number:
            print("You won! \n")
            break
        elif user_input < number:
            print("TO LOW! \n")
            number_of_guesses -= 1
            print(f"you have {number_of_guesses} guesses left \n")
        elif user_input > number:
            print("TO HIGH! \n")
            number_of_guesses -= 1
            print(f"you have {number_of_guesses} guesses left \n")
    if number_of_guesses == 0:
        print(f"you lost!, you have {number_of_guesses} guesses left")

        
while input("Do you wan to play the number guessing game? type 'yes' or 'no': \n") == 'yes':
    play()