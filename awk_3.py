#!/usr/bin/env python3

total_data = {}
logs = input("Please provide full path to the apaches log file: ")

with open(logs, "r") as file:
    for line in file:
        try: 
            ip = line.split(' ')[0]
            data_bytes = line.split(' ')[9]
            if ip in total_data:
                total_data[ip] += int(data_bytes)
            else:
                total_data[ip] = int(data_bytes)
        except (IndexError, ValueError) as e:
            pass
file.close()

for i, j in total_data.items():
    print(f'{j} bytes for {i}')            
