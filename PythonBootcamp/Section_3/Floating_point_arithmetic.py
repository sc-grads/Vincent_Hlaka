# Floating point arithmetic

print(0.125 == 1/10 + 2/100 + 5/1000)

print(format(1/3, '.20f'))
print(format(1/10, '.20f'))
print(format(0.1, '.20f'))
print(format(0.125, '.50f'))

a = 0.1 * 3
b = 0.3
print(a == b)


print(format(a, '.25f'))

from math import isclose
# isclose()
x = 0.00000001
y = 0.00000002
print(x == y)

print(isclose(x, y, abs_tol=0.01))

a = 999999999.01
b = 999999999.02
print(isclose(a, b, rel_tol=0.01))

a = 3.4
b = 2.3
print(a + b)
print(format(a, '.25f'))
print(format(b, '.25f'))

# Quiz
print(0.3 == 0.1 * 3)
print(0.3 * 3 != 0.9)
import math
a = 0.3
b = 0.1
print(math.isclose(a, b * 3 ))
