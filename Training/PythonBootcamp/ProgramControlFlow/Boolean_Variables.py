# Truthiness of statements

results = ''
if bool(results):
    print('results is not empty')
else:
    print('result is empty')

var1 = 'ss'
if var1:
    print('var1 truthy value is True')
else:
    print('var1 truthy value is False')

# var1 = []  replace 'ss' with an empty string, this will print False
# if var1:
#    print('var1 truthy value is True')
# else:
#     print('var1 truthy value is False')

# nested if/elif/else statements

answer = input('Do you want to continue? Enter yes or no:')
if answer == 'yes':
    print('We\'ll move on.')
elif answer == 'no':
    print('We\'ll stop.')
else:
    print('Invalid answer')

# the nested statement can be dragged in to the if statements

x = 10
if x <= 10:
    print('x is less or equal to 10')
elif x == 10:
    print('x equal 10')
else:
    print('x is greater')
