print("Welcome to the bakery!")

name = input("What is your name? ")

# گرفتن شماره کارت و بررسی ۱۶ رقمی بودن
card_number = input("Enter your card number: ")
if len(card_number) != 16 or not card_number.isdigit():
    print("Card number must be exactly 16 digits!")
    exit()

# گرفتن رمز دوبار و بررسی ۴ رقمی بودن
password1 = input("Enter your card password: ")
password2 = input("Enter your password again: ")

if len(password1) != 4 or not password1.isdigit():
    print("Password must be exactly 4 digits!")
    exit()

if password1 != password2:
    print("Passwords do not match! Please try again.")
    exit()

print("Password confirmed!")

again = "yes"

while again == "yes":
    bread = input("What kind of bread do you want? (e.g., sangak, barbari): ")
    count = input("How many " + bread + "s do you want? ")

    print("Here you go! " + count + " " + bread + "(s) ready!")

    again = input("Do you want more bread? (yes or no): ")

print("Thanks for coming, goodbye!")
