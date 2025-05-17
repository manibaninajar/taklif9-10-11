print("Welcome to the bakery!")

name = input("What is your name? ")
card_number = input("Enter your card number: ")

password1 = input("Enter your card password: ")
password2 = input("Enter your password again: ")

if password1 == password2:
    print("Password confirmed!")

    again = "yes"

    while again == "yes":
        bread = input("What kind of bread do you want? (e.g., sangak, barbari): ")
        count = input("How many " + bread + "s do you want? ")

        print("Here you go! " + count + " " + bread + "(s) ready!")

        again = input("Do you want more bread? (yes or no): ")

    print("Thanks for coming, goodbye!")

else:
    print("Passwords do not match! Please try again.")
