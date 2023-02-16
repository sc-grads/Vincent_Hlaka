# Ex 37


message = 'Wow! Python is great'
vowels = 'aeio'

no_vowels = [x for x in message if x not in vowels and x != ' ']

print(no_vowels)  # => ['W', 'w', '!', 'P', 'y', 't', 'h', 'n', 's', 'g', 'r', 't']