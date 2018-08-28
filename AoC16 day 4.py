import csv
from collections import parse

dirty_input = csv.reader(open("C:\Users\Diane\Desktop\Advent of code 2016\day 4 input.csv", "rb"), delimiter=",", quotechar='|')

rooms = []
for row in dirty_input:
    rooms.append(row)
print rooms

for enc in rooms:
    checksum = search('[{:s}]', enc)
    print checksum