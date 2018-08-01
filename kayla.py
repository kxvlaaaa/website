    print("Enter a number i will determine if its odd or even.")
aRandomNumber = randint(1, 20
def
    print(aRandomNumber)
guess = input("Guess a number between 1 and 20 (inclusive):")
if not guess.isnumeric(): # checks if a string is only digits 0 to 9

    print("That's not an even number, try again!")

else:
    guess = int(guess) # converts a string to an integer
if aRandomNumber == guess:
    print("you own congrats")
