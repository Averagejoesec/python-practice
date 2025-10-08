# Takes a payment amount and purchase price as input
print("Smart Change Maker")
purchase_price = float(input("Enter purchase price: "))
payment_amout = float(input("Enter payment amount: "))

# Calculates the change owed
change_owed = payment_amout - purchase_price
print(f"Change owed: ${change_owed}")

# Determines the minimum number of coins/bills needed
fifty_bills = 0
twenty_bills = 0
ten_bills = 0
five_bills = 0
one_bills = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

while change_owed != 0.000:
    change_owed = round(change_owed, 2)
    if change_owed > 50:
        fifty_bills += 1
        change_owed = change_owed - 50
    elif change_owed > 20:
        twenty_bills += 1
        change_owed = change_owed - 20
    elif change_owed > 10:
        ten_bills += 1
        change_owed = change_owed - 10
    elif change_owed > 5:
        five_bills += 1
        change_owed = change_owed - 5
    elif change_owed > 1:
        one_bills += 1
        change_owed = change_owed - 1
    elif change_owed > .25:
        quarters += 1
        change_owed = change_owed - .25
    elif change_owed > .10:
        dimes += 1
        change_owed = change_owed - .10
    elif change_owed > .05:
        nickels += 1
        change_owed = change_owed - .05
    elif change_owed >= .01 :
        pennies += 1
        change_owed = change_owed - .01
    else:
        break


print(fifty_bills, ten_bills, five_bills, one_bills, quarters, dimes, nickels, pennies)

# Shows the breakdown of each denomination

# Handles different currency denominations (quarters, dimes, nickels, pennies)

# Works with both coins and bills ($100, $50, $20, $10, $5, $1)