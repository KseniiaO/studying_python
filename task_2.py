#!/usr/bin/env python3

print("Please provide comma-separated numbers (you may \
also enter words but we're gonna throw them away)")

numbers = input(">>> ")

new_list = numbers.split(",") # creates a list of arguments provided by user

for i in new_list: # goes through each value in the list
    if i == "254":     # if value 254 is met the loop breaks
        break
    elif i.isdigit() and int(i) % 2 == 0: # prints only even numbers
        print(i)
