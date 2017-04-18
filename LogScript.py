import sys

def find_nth(line, char, n):
    start = line.find(char)
    while start >= 0 and n > 1:
        start = line.find(char, start+len(char))
        n -= 1
    return start

def getDate(line):
    start = line.find("]")
    line = line[:start]
    line = line.strip("[")
    line = line.split()
    if "Mon" in line:
        day = "Monday"
    elif "Tue" in line:
        day = "Tuesday"
    elif "Wed" in line:
        day = "Wednsday"
    elif "Thur" in line:
        day = "Thursday"
    elif "Fri" in line:
        day = "Friday"
    if "Jan" in line:
        month = "January"
    elif "Feb" in line:
        month = "February"
    elif "Mar" in line:
        month = "March"
    elif "Apr" in line:
        month = "April"
    elif "Jun" in line:
        month = "June"
    elif "Jul" in line:
        month = "July"
    elif "Aug" in line:
        month = "August"
    elif "Sep" in line:
        month = "September"
    elif "Oct" in line:
        month = "October"
    elif "Nov" in line:
        month = "November"
    elif "Dec" in line:
        month = "December"
    return day + " " + month + " " + line[2] + " " + line[4] + ":"

def main():
    errors = 0
    filename = input("Please enter an error_log file: ")
    if(filename == ""):
        print("Error: no filename entered.")
        sys.exit(0)
    else:
        f = open(filename)
        print("ERROR LOG FOR LOCAL APACHE SERVER")
        print("=================================")
        for line in f:
                if "error" in line:
                    start = find_nth(line, "]", 4)
                    print(getDate(line))
                    errors + 1
                    print("Error " + line[start+2:])
                    print("\n")
main()