#!/usr/bin/env python3

def top(mylist):
    
    num_list = []
    str_list = []

 # populates newly created lists: 1 - with integers, 2 - with everything else but integers
    for x in mylist:    
        if x.isdigit():
            num_list.append(int(x))
        else:
            str_list.append(x)

# notifies the user there are some non-integers in the list
    if len(str_list) > 0:
        print("I couldn't parse these elements:", str_list, "so I threw them away")

# sorts the list in descending order, if there are no integers provides a list of fruits
    if len(num_list) > 0:
        final_list = sorted(num_list, reverse = True)
        print("Top largest integers I found in the list:", final_list[0:3])
    else:
        print("As there were no integers at all take a list of fruits:",['apple', 'banana'])


mylist = input("Please provide comma-separated integers: ").split(",")
top(mylist)
