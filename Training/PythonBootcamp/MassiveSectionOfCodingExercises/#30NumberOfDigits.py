# Exercise 30
# Calculate the number of digits in the total number of IPv6 addresses. Each IPv6 uses 128 bits and the total number of IPv6 is 2 raised to the power of 128.
#Save the number of digits in the total number of IPv6 in a variable called no_of_digits.
# Total number of IPv6 (each ipv6 consists of 128 bits)
no_of_ipv6 = 2 ** 128

no_of_digits = len(str(no_of_ipv6))

print(no_of_digits)  # => 39