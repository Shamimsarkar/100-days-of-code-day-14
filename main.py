from art import logo, vs
from game_data import data
import random

def format_data(account):
#Takes the account data and output printable format
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(user_guess, follower_a, follower_b):
#Take the user guess, number of follower a and b get output if they got it right
    if follower_a > follower_b:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)

score = 0

account_b = random.choice(data) # Generate a random account from the game data
game_should_continue = True


while game_should_continue: # Make the game repeatable.

    account_a = account_b # Making account at position B become the next account at position A.
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")

    print(vs)

    account_b = random.choice(data)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    follower_count_a = account_a["follower_count"]
    print(follower_count_a)
    follower_count_b = account_b["follower_count"]
    print(follower_count_b)
    is_correct = check_answer(guess,follower_count_a,follower_count_b)
    print(is_correct)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

