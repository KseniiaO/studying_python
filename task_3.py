#!/usr/bin/env python3

import sys

if len(sys.argv) < 2: # exit the program if there are no arguments
    print("Please provide some arguments next time.")
    exit()

# creates a loop that breaks when input and one of the arguments match
while True:
    words = input("Enter my favorite word or phrase: ")
    for h in sys.argv[1:]:
        if h == words:
            print("Correct! Thank you, bye")
            exit()               
    print("No, it's not what I want!")
              
