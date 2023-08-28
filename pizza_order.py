size = input("what size of pizza do you want? S, M, L: ")

bill = 0

if size == "S":
    bill += 10
elif size == "M":
    bill +=15
else:
    bill +=20

add_peperoni = input("Do you want to add peperoni? Y, N: ")

if add_peperoni == "Y":
    bill += 3
    print(f"Your final bill is $ {bill}.")
else:
    print(f"Your final bill is $ {bill}.")

