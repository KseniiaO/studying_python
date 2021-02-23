#!/usr/bin/env python3

import os

pid = os.getpid()
user = os.getlogin()
os_info = os.uname()

# prints PID, user who is running the process, OS name and release

print("This script has the following PID: %s" % pid) 
print("It was ran by {} to work happily".format(user)) 
print(f"on {os_info[0]}-{os_info[2]}")

