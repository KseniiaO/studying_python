#!/usr/bin/env python3

num = int(input("Please provide any number: "))

matrix = [[None] * num for i in range(num)] # generates a square matrix n x n
count = 1 # this value increases by 1 each step and populates the matrix

for i in range(num-1):
    matrix[0][i] = count
    count += 1

for j in range(num-1):
    matrix[j][num-1] = count
    count += 1

for k in range(num-1):
    matrix[num-1][num-1-k] = count
    count += 1

for i in range(num-1):
    matrix[num-1-i][0] = count
    count += 1

for i in matrix:
    print(i)
