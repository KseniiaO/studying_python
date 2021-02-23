#!/usr/bin/env python3

numbers = input("Please provide some comma-separated numbers: ")         

new_list = numbers.split(",") # creates a list from the input
new_tuple = tuple(new_list) # creates a tuple from the list

print(new_list)
print(new_tuple)
