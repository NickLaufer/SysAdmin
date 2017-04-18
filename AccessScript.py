
def getDate(line):
    start = line.find("[")
    end = line.find("]")
    line = line[start:end]
    line = line.strip("[")
    line = line.split("/")
    line[2] = line[2].split(":")
    return line[0] + " " + line[1] + " " + line[2][0]


def main():
    linelist = []
    filename = input("Please enter an access log file: ")
    if(filename == ""):
        print("Error: no filename entered.")
    else:
        access = 0
        f = open(filename)
        for line in f:
            linelist.append(line)
            if "GET" in line:
                if "index.html" in line:
                    access = access + 1
        print("WEBLOG REPORT FOR LOCAL APACHE SERVER")
        print("=====================================")
        print("Report covers from " + getDate(linelist[0]) + " to " + getDate(linelist[len(linelist)-1]))
        print("There were " + str(access) + " hits.")


main()