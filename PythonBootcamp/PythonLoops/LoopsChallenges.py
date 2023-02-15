# Loops challenges


# Challenge 1
# Python script that asks the user for a number and then prints out a list of all the divisors of each number
# less than the asked number.


x = int(input("Enter a number: "))
all_divisors = list()
for i in range(2, x//2+1):
    if x % i == 0:
        all_divisors.append(i)

print(all_divisors)

# Challenge 2
# Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.
# Input: 16, 2
# Output: 4 ** 2 = 16

x = int(input("Enter a number x: "))
y = int(input(f"Enter a number y to test if x which is {x} is a power of y: "))

found = False

for k in range(2, x//2):
    if y ** k == x:
        print(f"{y} ** {k} = {x}")
        found = True
        break
else:
    print(f'{x} is not the power of {y}')

# Challenge 5

print("Enter some floats to calculate their sum, product and average. Input 0 to exit.")

count = 0
sum = 0.0
product = 1

while True:
	number = float(input(''))
	if number == 0:
		break

	sum += number
	product *= number
