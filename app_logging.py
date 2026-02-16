#SECTION C
import logging

logging.basicConfig(filemode ="Error.log", level = logging.ERROR)

def read_logfile(filename):
    records = []

    try:
        with open (filename, "r") as file:
            for line in file:
                line = line.strip()
            if line:
                records.append(line)
        return records
    except FileNotFoundError as e:
        print("file not ound: %s", filename)
        raise e

def parsed_records(lines):
    parsed = []
    for line in lines:
        parts = line.split(",")
        if len(parts)>=2:
            parsed.append({
                "user": parts[0],
                "status":parts[1]
            })
    return parsed

def main():
    filename = input("Enter a file name : ")

    try:
        lines = read_logfile(filename)
        data = parsed_records(lines)

        print("Parsed Data : ", data)
    except Exception as e:
        print("Error occured", e)

if __name__ == "__main__":
    main()
