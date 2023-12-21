
'''
1. display art
2. generate a random account from the game data
3. format the account data into printable format
4. ask user for a guess.
5. check if user is correct.
i. get follower count of each account
ii. use if statement to check if user is correct
6. give user feedback on their guess
7. score keeping
8. make the game repeatable
9. making account at position B become the next account at position A.
10. clear the screen between round
'''
from game_data import data
from art import logo, vs
import random
print(logo)
score = 0
should_game_continue = True
account_b = random.choice(data)
while should_game_continue:
    account_a = account_b
    account_b = random.choice(data)


    while account_a == account_b:
        account_b = random.choice(data)


    def format_data(account):
        account_name = account['name']
        account_describ = account['description']
        account_country = account['country']

        return f"{account_name}, {account_describ}, {account_country}"


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has a greater follower. Type 'A' or 'B': ")

    a_follower_count = account_a['follower_count']
    b_follower_count = account_a['follower_count']

    def check_answer(guess, a_follower, b_follower):
        if a_follower > b_follower:
            return guess == "a"
        else:
            return guess == "b"


    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"correct. Your score is {score}")
    else:
        should_game_continue = False
        print(f"Wrong. Your score is {score}")

