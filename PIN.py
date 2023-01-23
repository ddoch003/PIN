import winsound
import datetime
import time

pin = "1234"
user_entry = ""
counter = 0
limit = 3
balance=20000
running=True
card_blocked=False

def main_menu():
    print()
    print("***** MAIN MENU *****")
    print()
    print("1. Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Cancel")
    print()
    global select_option
    select_option = int(input("Please select one of the options: "))
    while select_option!=1 and select_option!=2 and select_option!=3 and select_option!=4:
        print("Invalid operator!")
        select_option = int(input("Please select one of the options: "))
    else:
        if select_option==1:
            current_amount()
        elif select_option==2:
            withdraw()
        elif select_option==3:
            deposit()
        else:
            global running
            running=False

def proceed_decision_function():
    proceed_decision = input("Do you want to continue with another operation (y/n): ").lower()
    while proceed_decision != "y" and proceed_decision != "n":
        print("Please enter a valid operator!")
        proceed_decision = input("Do you want to continue with another operation (y/n): ").lower()
    else:
        if proceed_decision == "y":
            main_menu()
        else:
            global running
            running = False

def current_amount():
    print("Please wait...")
    time.sleep(3)
    print("Your current balance is: " + str(balance))
    proceed_decision_function()

def withdraw():
    global balance
    withdraw_amount = int(input("Please enter the amount you want to withdraw: "))
    while withdraw_amount > 500 or withdraw_amount>balance:
        print("Please wait...")
        time.sleep(2)
        print("Exceeded withdraw limit")
        withdraw_amount = int(input("Please enter the amount you want to withdraw: "))
    else:
        while withdraw_amount%10!=0:
            print("Please wait...")
            time.sleep(2)
            print("Please enter amount divisible by 10")
            withdraw_amount = int(input("Please enter the amount you want to withdraw: "))
        else:
            balance = balance - withdraw_amount
            print("Please wait...")
            time.sleep(3)
            print("You have successfully withdrawn " + str(withdraw_amount))
            print("Your current balance is: " + str(balance))
            proceed_decision_function()

def deposit():
    deposit_amount = int(input("Please enter the amount you want to deposit: "))
    global balance
    balance = balance + deposit_amount
    print("Please wait...")
    time.sleep(3)
    print("You have successfully deposited " + str(deposit_amount))
    print("Your current balance is: " + str(balance))
    proceed_decision_function()

def card_blocked_function():
    winsound.Beep(900, 500)
    print("Card blocked! Please contact 0800 000 111")
    global card_blocked
    card_blocked=True

def incorrect_pin():
    winsound.Beep(432, 500)
    global counter
    print("Incorrect PIN! " + str(limit - (counter + 1)) + " tries left.\n")
    counter = counter + 1

def correct_pin():
    winsound.Beep(600, 500)
    print("Correct PIN! Please wait...\n")
    time.sleep(4)


winsound.Beep(600, 500)
x=datetime.datetime.now()
print(x.strftime("%A"),x.date(),x.strftime("%X"))
print()
print("Welcome to Python Bank!\n")

while running:
    if counter < limit:
        user_entry = input("Please enter your PIN: ")
        if user_entry != pin:
            if not user_entry.isdigit() and not user_entry == "quit":
                print("Please enter numbers only.\n")
            elif user_entry == "quit":
                running = False
            else:
                incorrect_pin()
        else:
            correct_pin()
            main_menu()
    else:
        card_blocked_function()
        break
else:
    if card_blocked==False:
        print("Thank you for choosing Python Bank. Goodbye!")