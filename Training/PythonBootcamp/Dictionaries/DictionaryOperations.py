# Exercise 23

# given ,,,
money = {
    'bank': 8564.61,
    'paypal': 1998.21,
    'cash': 480,
    'payoneer': 250.5
}

# using a for loop
total_amount = 0
for value in money.values():
    total_amount += value

print(total_amount)
