print("Hi!! Welcome to GOOD CAFE")
Name = input("What is your name?\n").upper()

def amt(price):
    print("Your total is " + str(price) + ". Thank you!")

def menu():
    print("Hello " + Name + ", What would you like to order? \nCoffee, Tea, Samosa")
    Order = input().lower()
    Qunt = int(input("How many?\n"))

    if Order == "coffee":
        price = 20 * Qunt
        amt(price)
    elif Order == "tea":
        extra_milk = input("Do you like it with extra milk?\n").lower()

        if extra_milk == "yes":
            price = 14 * Qunt
            amt(price)
        else:
            price = 5 * Qunt
            amt(price)
    elif Order == "samosa":
        price = 15 * Qunt
        amt(price)
    else:
        print("Invalid order")

if Name in ["HEN", "DUCK", "Dove"]:
    Bird = input('''Are you a bird?\n(Yes or No)\n''').lower()

    if Bird == "no":
        menu()
    else:
        print("Sorry " + Name)
else:
    menu()
