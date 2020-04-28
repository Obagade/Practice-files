bill = float(input("Enter your bill? "))

tip = int(input("Enter tip percentage? "))

tip_amt = bill * tip/100

total = bill + tip_amt
print(f"Your tip is ${tip_amt:.2f} and total is ${total:.2f} ")


# bill = float(input("Your bill is "))

# print("Select a tip amount between 15%, 18%, and 20%")

# tip = ((float(input("Enter tip ")) / 100) * bill)

# print(f"Your tip amount is equivalent to {tip}")

# total = bill + tip
# print(f"Your total bill is {total}")