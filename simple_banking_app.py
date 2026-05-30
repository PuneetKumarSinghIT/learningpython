"""
This module is created for banking application in python as simple functions.
It will help user to check balance, deposit and withdraw money from their account.
"""

balance = 0

def check_balance(balance):
    """This function will check the balance of the user."""
    return balance

def deposit(amount):
    """This function will deposit the amount to the user's account."""
    global balance
    if amount > 0:
        balance += amount

def withdraw(amount):
    """This function will withdraw the amount from the user's account."""
    global balance
    if amount <= balance:
        balance -= amount

print("Welcome to the Simple Banking App!")
while True:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        print(f"Your balance is ${check_balance(balance)}")
        
    elif choice == "2":
        amount = float(input("Enter the amount to deposit: "))
        deposit(amount)
        print(f"You have deposited ${amount}")
        
    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: "))
        withdraw(amount)
        print(f"You have withdrawn ${amount}")
        
    elif choice == "4":
        print("Thank you for using the Simple Banking App!")
        break
        
    else:
        print("Invalid choice! Please try again.")