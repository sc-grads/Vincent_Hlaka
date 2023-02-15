#  Lambda parameter_list: expression

def add(a, b, c):
    result = a + b + c
    return result

result = (lambda a,b, c: a +b +c )(3, 4, 5)
print(result)

square = lambda x=10: x ** 2
print(square(4))
print(square())

skeem = [('Tim', 30), ('Jos', 25), ('Jeff', 22)]
skeem.sort(key=lambda x: len(x[0]))
print(skeem)