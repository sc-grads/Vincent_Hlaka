# Ex 32

# Your task is to extract the price in a variable called price and calculate the VAT knowing that the VAT percentage is 19%.
# Use only 2 decimal points for the VAT value.

# The VAT value will be stored in a variable called vat and will be a float.
# Given
phone = {'Brand': 'Samsung', 'Price': 650.2, 'Seller': 'Nile'}
# code
price = phone['Price']
vat = format(price * 0.19, '.2f')   # format() returns a string
vat = float(vat)                    # casting to float

print(vat)  # => 123.54
