# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import random


# %%
money = 100  


# %%
def odd_or_even(guess, bet):
    dice = random.randint(1,12)
    global money

    outcome = ""

    if dice % 2 == 0:
        outcome = "even"

    else:
        outcome = "odd"
    
    if outcome == "even":
        if guess.lower() == "even":
            money += bet * 1.5
            print("Congrats, you won!")
            print("Your balance is " + str(money))

        elif guess.lower() == "odd":
            money -= bet
            print("Better luck next time!")
            print("Your balance is " + str(money))

        else:
            print("Please select from 'odd' or \"even\".")
            print("Your balance is " + str(money))

    elif outcome == "odd":
        if guess.lower() == "odd":
            money += bet * 1.5
            print("Congrats, you won!")
            print("Your balance is " + str(money))

        elif guess.lower() == "even":
            money -= bet
            print("Better luck next time!")
            print("Your balance is " + str(money))

        else:
            print("Please select from \"odd\" or \"even\".")
            print("Your balance is " + str(money))



# %%
odd_or_even("odd",10)


# %%


