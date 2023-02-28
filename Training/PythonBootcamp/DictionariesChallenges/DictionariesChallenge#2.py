# Challenge 2

# Consider a list of words (strings).
# Write a Python script that generates a dictionary where the key is the word in the list
# and the value is its length.
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

# Expected Result: {'Python': 6, 'Java': 4, 'C++': 3, 'Golang': 6, 'Solidity': 8, 'Bash': 4}

words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
words_and_length = dict()

for w in words:
    words_and_length[w] = len(w)

print(words_and_length)