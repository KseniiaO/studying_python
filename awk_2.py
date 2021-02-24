#!/usr/bin/env python3

# the following script provides statistics for IP address

import re

datestamp = {}
logs = input("Please provide full path to the apache log file: ")
ip = input("Please enter IP address: ")

with open(logs, 'r') as file:
    for line in file:
        upd_line = re.split(' |/|:', line)
        if upd_line[0] == ip:
            key = upd_line[4] + " " + upd_line[5]
            if key in datestamp:
                datestamp[key] += 1
            else:
                datestamp[key] = 1
file.close()

if len(datestamp) > 0:
    for i, j in datestamp.items():
        print(f"{i} - number of requests: {j} ")
else:
    print(f"Sorry, I couldn't find IP address {ip} in the logs")
