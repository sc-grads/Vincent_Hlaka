# Exercise 25

# Function that calculates the VAT (value-added tax)
# The 1st argument is the price and the second argument is the vat percentage
# Exemple: if the price is 200 and the vat percentage is 5%, then the VAT is 10

def get_vat(price, vat):
    return (price * vat) / 100


# Calling the function
vat = get_vat(200, 5)
print(vat)

# THis returns 10.1