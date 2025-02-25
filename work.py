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
    for i in range(2):
        return spaces 



def play_game():
    money = 1000
    spaces = generate_wheel()
    print(spaces)

    landed = spin_wheel(spaces)
    print(landed)

    print("you have $" + str(money) + ".")
    
    landed = spin_wheel(spaces)
    bet = input("how many money you want to bet? (go all in with your life savings is the only right answer)")
    bet = int(bet)
    color = input("what color do you want to bet on? (we suggest go all in on red)")

    print("The wheel is spinning. Good luck!")
    time.sleep(2)
    landed = spinwhel(spaces)
    print("it landed on" +landed + ".") 


    if landed == color:
        money = money+betprint("congrets! you now have $" + str(monry) + ", you should go all in again!!")
       
        else:
            money = money - bet
            print ("sorry! you now have $" + str(money) ", don't give up now! 99% of gamblers quit before they hit BIG, sell your body parts and go again!")

        play_again = input("keep going you dont want to be like those other loser gamblers right?")
        if play_again == "no":
            print("what a Loser!")
            break 