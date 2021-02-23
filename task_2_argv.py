#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("Please provide some arguments next time.")
    exit()

for i in sys.argv[1:]: # takes command line arguments and prints only even numbers
    if i == "254":     # if number 254 is met the loop breaks
        break
    elif i.isdigit() and int(i) % 2 == 0:
        print(i)
