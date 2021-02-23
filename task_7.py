#!/usr/bin/env python3

num = int(input("Please provide any number: "))

matrix = [[None] * num for i in range(num)] # generates a square matrix n x n
count = 1 # this value increases by 1 each step and populates the matrix

p = 0
m = 0
for i in range(2): # 2 is for testing
    for i in range(m,num-1-p):
        matrix[m][i] = count
        count += 1

    for j in range(m,num-1-p):
        matrix[j][num-1-m] = count
        count += 1

    for k in range(m,num-1-p):
        matrix[num-1-m][num-1-k] = count
        count += 1

    for i in range(m,num-1-p):
        matrix[num-1-i][m] = count
        count += 1
    p += 2
    m += 1

for i in matrix:
    print(i)

