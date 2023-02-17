import csv

people = [
    ['Dan', 34, 'Bucuresti'],
    ['Andrei',21, 'London'],
    ['Maria', 45, 'Paris']
]

# writing into a csv file
with open('people2.csv', 'w') as f:
    writer = csv.writer(f, delimiter=':')
    for item in people:
        writer.writerow(item)


# reading a csv file
with open('people2.csv') as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        print(row)