#!/usr/bin/env python3

def dictionary(str):
    my_dict = {}

    for x in str:
        if x.isspace() == False: # skips whitespaces
            if x in my_dict:
                my_dict[x] += 1 # if the key exists the value is increased    
            else:
                my_dict.update({x: 1}) # if it's a new key add this key to the dict with value 1
    return my_dict

text = input("Please enter any text: ")

print(dictionary(text))
