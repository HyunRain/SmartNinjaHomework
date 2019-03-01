# 1.Übung: mood checking program
# if mood = happy, response: It is great to see you happy!
# elif mood = nervous, response: Take a deep breath 3 times.
# make 3 more elif statements for sad, excited and relaxed.
# end it with else: I dont recognize this mood.
user_name = input("What is your name, friend?: ")
user_mood = input("What is your current mood " + user_name + "?: ")

if user_mood == "happy":
    print("It is great to see you happy!")
elif user_mood == "nervous":
    print("Take a deep breath 3 times.")
elif user_mood == "sad":
    print("I hope things will get better for you in the future.")
elif user_mood == "excited":
    print("If I would take part in a competition, I would be excited aswell.")
elif user_mood == "relaxed":
    print("Enjoy your well earned day off.")
else: print("I dont recognize this mood.")

# 2.Übung: Game called: guess the secret number.
# hard-code a variable which is the number to be guessed.
# user inputs a guess, store the input to a variable called users_guess.
# check if users guess is correct
# if users guess is false, tell him/her.
# if users guess is correct, congratulate him/her.

secret_number = 8
users_guess1 = int(input("Guess a number between 1 and 10 to win the grand prize! You have 3 guesses available: "))
if users_guess1 == secret_number:
    print("Congratulations, you won the grand prize of 1 Euro and 20 Cents!")
else:
    print("This number is incorrect.")
users_guess2 = int(input("Take a second guess: "))
if users_guess2 == secret_number:
    print("Congratulations, you won the grand prize of 1 Euro and 20 Cents!")
else:
    print("This number is incorrect.")
users_guess3 = int(input("Take your 3rd and last guess for the chance to win the grand prize: "))
if users_guess3 == secret_number:
    print("Congratulations, you won the grand prize of 1 Euro and 20 Cents!")
else:
    print("Sadly you did not win, maybe you have better luck next time!")

# 3.Übung: Simple Calculator:
# Ask for 2 numbers
# Ask what operations to use
# give out the solution

first_input = int(input("Please enter your first number!: "))
second_input = int(input("Please enter your second number!: "))
third_input = input("Please choose your operation(+,-,*,/): ")

if third_input == "+":
    print(first_input + second_input)
elif third_input == "-":
    print(first_input - second_input)
elif third_input == "*":
    print(first_input * second_input)
elif third_input == "/":
    print(first_input / second_input)
else:
    print("This calculator is not smart enough to know this operation.")


