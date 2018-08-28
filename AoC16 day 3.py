import csv

dirty_input = csv.reader(open("C:\Users\Diane\Desktop\Advent of code 2016\day 3 input.csv", "rb"), delimiter=",", quotechar='|')

A = []
B = []
C = []


ind = 0
for row in dirty_input:
        if ind == 0:
            A.append(row[0])
            A.append(row[1])
            A.append(row[2])
        if ind == 1:
            B.append(row[0])
            B.append(row[1])
            B.append(row[2])
        if ind == 2:
            C.append(row[0])
            C.append(row[1])
            C.append(row[2])
        if ind == 0:
            ind = 1
        elif ind == 1:
            ind =2
        elif ind ==2:
            ind = 0

print A
#for row in dirty_input:
 #       A.append(row[0])
  #      B.append(row[1])
   #     C.append(row[2])

counter = 0



for i in range(0,1635):
    print A[i], B[i], C[i]
    side1 = int(A[i]) + int(B[i])
    side2 = int(A[i]) + int(C[i])
    side3 = int(B[i]) + int(C[i])
    CC = int(C[i])
    AA = int(A[i])
    BB = int(B[i])
    if (side1 > CC) and (side2 > BB) and (side3 > AA):
        counter = counter+1
        print counter
print counter