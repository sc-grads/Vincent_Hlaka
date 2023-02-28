# Challenge 14

# Write a Python script that validates an email address by writing "Valid email!" or "Invalid email!".

# If the email is not valid the script should display why it's not valid.

# Consider a valid email address if: it has at least 6 characters but no more than 16.
# it contains both . and @
# it does not contain any of the following characters:'[]{}()$*'

not_permitted = '[]{}()$*'
must_contain = '.@'
while True:
    email = input("Enter your email:")
    if len(email) < 6 or len(email) > 16:
        print('Invalid email length!')
    elif not set(email).isdisjoint(set(not_permitted)):  # two sets are disjoint if they have no elements in common
        print('Invalid symbols in email!')
    elif set(must_contain) & set(email) != set(must_contain):
        print('Invalid email. Must contain . and @')
    else:
      print('Valid email!')
      break