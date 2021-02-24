#!/usr/bin/env python3

num = int(input("Please provide any number: "))
n = num - 1 # to avoid mess in the ranges

matrix = [[None] * num for i in range(num)] # generates a square matrix n x n
count = 1 # this value increases by 1 with each step and populates the matrix

d = 0 # with each new 'circle' size of the unmodified column or row is decreasing by 2
# we need this variable to decrease ranges and move to the next column or row

# to calculate the number of 'circles' we need to divide provided integer by 2
# if the integer is odd the result has to be rounded down to the nearest integer 

for t in range(num // 2): 

    for i in range(d,n-d): # updates first row
        matrix[d][i] = count
        count += 1

    for j in range(d,n-d): # updates right column
        matrix[j][n-d] = count
        count += 1

    for k in range(d,n-d): # updates last row
        matrix[n-d][n-k] = count
        count += 1

    for i in range(d,n-d): # updates left column
        matrix[n-i][d] = count
        count += 1
    d += 1

# if the provided number is odd we need to calculate central element of the matrix
if num % 2 != 0:
    matrix[num // 2][num // 2] = num ** 2

for i in matrix:
    print(i)
