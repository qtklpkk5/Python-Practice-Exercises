birth_year = int(input("Enter the year you were born: "))
age_in_2025 = 2025 - birth_year
print(f"You will turn {age_in_2025} in 2025.")


import random

number_to_guess = random.randint(1, 100)
guess_count = 0

while True:
    user_guess = int(input("Guess the number (between 1 and 100): "))
    guess_count += 1

    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Correct! It took you {guess_count} guesses.")
        break




groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:
    print(f"Current grocery list: {groceries}")
    item_to_remove = input("Enter an item to remove (or type 'stop' to exit): ").lower()

    if item_to_remove == "stop":
        break
    elif item_to_remove in groceries:
        groceries.remove(item_to_remove)
        print(f"Removed {item_to_remove}.")
    else:
        print(f"{item_to_remove} is not in the list.")
