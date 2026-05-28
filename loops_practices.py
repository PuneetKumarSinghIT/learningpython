"""
This module will demonstrate the nested loops concept and will help in implementing the loops for testing.
It is a practice module.
"""

# Nested loops example
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"Outer loop iteration {i}, Inner loop iteration {j}")

# Looping through a list of lists (2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Newline after each row

# 2D coordinates example
for x in range(3):
    for y in range(3):
        print(f"Coordinate: ({x}, {y})")

# 2D cocordintes in tabular format.
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})", end=" ")
    print()  # Newline after each row

# Practicing with starts pattern printing.
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()  # Newline after each row

# Roll a dice example using nested loops

import random

print("Welcome to dice rolling simulator!")
while True:
    choice = input("Press enter to roll the dice or press 'q' to quit: ")
    choice = (
        choice.strip()
    )  # Convert input to lowercase for case-insensitive comparison
    if choice == "q":
        print("Thanks for playing!")
        break
    elif choice == "":
        number = random.randint(1, 6)
        print("You rolled a", number)
    else:
        print("Invalid input. Please press enter to roll the dice or 'q' to quit.")

# List and loops usage
countries = [
    "USA",
    "Canada",
    "Mexico",
    "Brazil",
    "Argentina",
    "UK",
    "France",
    "Germany",
    "Italy",
    "Spain",
    "Portugal",
    "India",
    "China",
    "Japan",
    "Australia",
    "New Zealand",
    "South Africa",
    "Egypt",
    "Nigeria",
    "Kenya",
    "Indonesia",
    "Iran",
    "Iraq",
    "Thailand",
    "Malaysia",
    "Singapore",
    "Philippines",
    "Vietnam",
    "South Korea",
    "North Korea",
    "Russia",
    "Ukraine",
    "Belarus",
    "Poland",
    "Czech Republic",
    "Slovakia",
    "Bulgaria",
    "Romania",
    "Moldova",
    "Hungary",
    "Austria",
    "Switzerland",
    "Sweden",
    "Norway",
    "Denmark",
    "Finland",
    "Iceland",
    "Greece",
    "Turkey",
]
for country in countries:
    print("Country:", country)

# count all the countries in the list which are startign with i or I
# Also print all the countries which are starting with i or I as list.
count = 0
i_countries = []
for country in countries:
    if country.lower().startswith("i"):
        count += 1
        i_countries.append(country)
print("Number of countries starting with 'i' or 'I':", count)
print("Countries starting with 'i' or 'I':", i_countries)

# Loop and dictionary example
user = {
    "user_name": "john_doe",
    "password": "password123",
    "email": "iVw0b@example.com",
    "address": "123 Main St, Anytown, USA",
    "country": "USA",
}

# Delete the sensitive information from the dictionary present in a list sensitive_info = ["password", "address"]
# Don't ever try to delete any entry from the dictionary or list which you are looping for finding your desired value,
# as it will cause the error "RuntimeError: dictionary
# changed size during iteration" or "RuntimeError: list changed size during iteration"

sensitive_info = ["password", "address", "phone_number"]
# Added phone_number to demonstrate the case
# where the key might not exist in the dictionary
for key in sensitive_info:
    if key in user:
        print(f"Removing sensitive information: {key}, value: {user.get(key)}")
        user.pop(
            key, None
        )  # Remove the key from the dictionary if it exists, otherwise do nothing
    else:
        print(f"Key '{key}' not found in the user dictionary. Skipping removal.")
print(user)

"""
Create a simple number guessing game.
The user gets 10 choices to guess a number.
If the user guesses the number before 10 chances, stop asking the number from the user,
say Congrats and end the game.
If user never guesses the number, ask them 10 times and then end the game.
"""

import random

number_to_guess = random.randint(1, 50)
print("Welcome to the number guessing game!")
for attempt in range(1, 11):
    guess = int(input(f"Attempt {attempt}: Guess the number between 1 and 50: "))
    if guess == number_to_guess:
        print("Congrats! You've guessed the number correctly!")
        break
    elif guess < number_to_guess:
        print("Wrong guess. Try higher.")
    else:
        print("Wrong guess. Try lower.")
else:
    print(
        f"""Sorry, you've used all 10 attempts. 
      The number was {number_to_guess}. Better luck next time!"""
    )

print("Thanks for playing the number guessing game!")


# As you can see above that
# for condition:
#     statements
# else:
#     statements
# this is the special for loop with else block, the else block will be executed only
# if the loop is not terminated by a break statement.
