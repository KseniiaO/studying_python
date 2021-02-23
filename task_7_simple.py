#!/usr/bin/env python3

num = int(input("Please provide any number: "))

matrix = [[None] * num for i in range(num)] # generates a square matrix n x n
count = 1 # this value increases by 1 each step and populates the matrix

for i in range(num):
    for j in range (num):
        matrix[i][j] = count
        count += 1

for i in matrix:
    print(i)
