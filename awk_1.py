#!/usr/bin/env python3

user_agents = {} # key - user agent, value - number of uses

logs = input("Please provide full path to the log file: ")

with open(logs, "r") as file:
    for line in file: # reads each line of the provided file 
        try:
            key = line.split('"')[5] # columns are separated with ", we need values in column 6(index 5)
            if key in user_agents:
                user_agents[key] += 1 # increases value for existing key
            else:
                user_agents[key] = 1 # adds new key with value 1
        except IndexError: # if a line is too short,the script skips it
            pass
        
file.close()

# sort by value to find the most popular user agent
sorted_list = sorted(user_agents.items(), key=lambda y: y[1], reverse = True)

print("The most popular user agents are: ")
for i in sorted_list[:10]:
    print(i[0], i[1])
