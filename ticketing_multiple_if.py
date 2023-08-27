print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?: "))
    if age < 12:
        photo = input("Do you want photo? ")
        if photo == "yes":
            print("Please Pay $8")
        else:
            print("Please pay $5.")

    elif age <= 18:
        photo = input("Do you want photo? ")
        if photo == "yes":
            print("Please Pay $10")
        else:
            print("Please pay $7.")
    else:
        photo = input("Do you want photo? ")
        if photo == "yes":
            print("Please Pay $15")
        else:
            print("Please pay $12.")

else:
    print("Sorry, you have to grow taller before tou can ride.")