#SECTION - B
import sys
filename = input("Enter a log file name: ")
records = []
log_summary = {}
try:
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue
        parts = line.split(",")
        if len(parts) >= 2:
            users = parts[0]
            status = parts[1]
            record = {
                "users": users,
                "status": status
            }
            records.append(record)
            if users in log_summary:
                log_summary[users] += 1
            else:
                log_summary[users] = 1
        
        print("records: ", len(records))
        print("summary: ", log_summary)
        x = 5
        y = 3
        print("Bitwise OR:- ", x|y)
        print("Bitwise AND:- ", x&y)
except FileNotFoundError:
    print("File not Found Sorry!!!")

