# birth_year = int(input("Enter the year you were born: "))
# age_in_2025 = 2025 - birth_year
# print(f"You will turn {age_in_2025} in 2025.")


# import random

# number_to_guess = random.randint(1, 100)
# guess_count = 0

# while True:
#     user_guess = int(input("Guess the number (between 1 and 100): "))
#     guess_count += 1

#     if user_guess < number_to_guess:
#         print("Too low!")
#     elif user_guess > number_to_guess:
#         print("Too high!")
#     else:
#         print(f"Correct! It took you {guess_count} guesses.")
#         break




# groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

# while True:
#     print(f"Current grocery list: {groceries}")
#     item_to_remove = input("Enter an item to remove (or type 'stop' to exit): ").lower()

#     if item_to_remove == "stop":
#         break
#     elif item_to_remove in groceries:
#         groceries.remove(item_to_remove)
#         print(f"Removed {item_to_remove}.")
#     else:
#         print(f"{item_to_remove} is not in the list.")


import random
import time

def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    spaces.append("green")  # Add the green space for zero
    return spaces

def spin_wheel(spaces):
    return random.choice(spaces)

def play_game():
    money = 1000
    spaces = generate_wheel()

    while True:
        print("You have $" + str(money) + ".")
        bet = input("How much money do you want to bet? (go all in with your life savings is the only right answer): ")
        
        # Check if the bet is more than the money the user has
        bet = int(bet)
        if bet > money:
            print("You can't bet more than you have!")
            continue  # If the bet is more than the money, it will ask again
        
        color = input("What color do you want to bet on? (red, black, or green): ").lower()

        print("The wheel is spinning. Good luck!")
        time.sleep(2)
        
        landed = spin_wheel(spaces)
        print(f"It landed on {landed}.")
        
        if landed == color:
            money += bet
            print(f"Congrats! You now have ${money}. You should go all in again!!")
        else:
            money -= bet
            print(f"Sorry! You now have ${money}. Don't give up now! 99 percent of gamblers quit before they hit BIG, sell your body parts and go again!")

        play_again = input("Keep going? You don't want to be like those other loser gamblers, right? (yes/no): ").lower()
        if play_again == "no":
            print("What a loser!")
            break

# Start the game
play_game()



# Initial menu dictionary
menu = {
    "Pizza": 1.99,
    "Soda": 0.69,
    "Double Chunk Chocolate Chip Cookie": 2.49
}

# Function to add an item to the menu
def add_item_to_menu(item, price):
    menu[item] = price

# Call the function with an example item and price
add_item_to_menu("Hot Dog", 1.29)

# Print the updated menu to check
print(menu)


{
    'Pizza': 1.99,
    'Soda': 0.69,
    'Double Chunk Chocolate Chip Cookie': 2.49,
    'Hot Dog': 1.29
}

