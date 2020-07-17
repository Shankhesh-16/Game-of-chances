import random
money = 100

def up_or_down():
    global money
    choice = input('Choose from "7up" or "7down": ')
    bet1 = input('You have ' + str(money) + ' in your pocket place a bet: ')
    bet = float(bet1)

    print("Welcome to 7 up, 7 down")
    dice = random.randint(1, 12)

    if bet <= money or bet != 0:
        if choice.lower() == "7up":
            if dice > 6:
                print("Outcome is " + str(dice) + ".")
                money += 1.5 * bet
                print("Your balance is " + str(money))

            elif dice < 7:
                print("Outcome is " + str(dice) + ".")
                money -= bet
                print("Your balance is " + str(money))

        elif choice.lower() == "7down":
            if dice > 6:
                print("Outcome is " + str(dice) + ".")
                money -= bet
                print("Your balance is " + str(money))

            elif dice < 7:
                print("Outcome is " + str(dice) + ".")
                money += 1.5 * bet
                print("Your balance is " + str(money))

        else:
            print("Please select from '7up' or '7down'.")

    else:
        print('Please place a bet which is lower or equal to your balance, which is: ' + str(money))

up_or_down()