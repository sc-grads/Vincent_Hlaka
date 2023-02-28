# Importing the module
import csv

## Opening people.csv in append-mode
with open('people.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)  # getting a csv.writer object
    csvdata = (5, 'Anne', 'Amsterdam')
    writer.writerow(csvdata)
# appending a line to the end file. csvdata is a tuple