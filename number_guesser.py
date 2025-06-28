import random 

# Introduction
print("Welcome to the number guesser game! I will pick a number based on your bounds and you will have to guess. \n")

lower = int(input("What would you like to be the lower bound?: "))
upper = int(input("What would you like to be the upper bound?: "))
ans = random.randint(lower, upper)

print(f"I have chosen a number between {lower} and {upper}. You have 5 guesses. \n")

guess_amount = 5
# Number guessing logic
tries = 0

while tries < guess_amount:
    guess = int(input("What is your guess?: "))
    tries += 1
    if guess < lower or guess > upper:
        print("That is not in the range. Try again.")
        continue
    if guess < ans:
        print("Your answer was too low. Try again! \n")
        
    if guess > ans:
        print("Your answer was too high. Try again! \n")
        
    if guess == ans:
        print("You got it correct!! Good job.")
        break
else:
    print("Better luck next time! My number was: " + str(ans))            

# End of the game, results and what happened?