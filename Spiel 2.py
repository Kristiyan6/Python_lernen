import random

options = ["stein", "papier", "schere"]

user_choice = input("Wähle stein, schere, oder papier:\n ").lower()

computer_choice = random.choice(options)

print("Du hast gewählt: ", user_choice)

print("Der Computer hat gewählt: ", computer_choice)

if user_choice == computer_choice:

    print("Es ist ein Unentschieden!")

elif user_choice == "stein" and computer_choice == "schere":

    print("Du hast gewonnen!")

elif user_choice == "papier" and computer_choice == "stein":

    print("Du hast gewonnen!")

elif user_choice == "schere" and computer_choice == "papier":

    print("Du hast gewonnen!")

else:

    print("Der Computer hat gewonnen!")
