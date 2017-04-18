import os

class User(object):

    def __init__(self, firstname, middlename, lastname, group):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.username = firstname[0] + middlename[0] + lastname
        self.group = group


def main():
    filename = input("Please enter a file name containing a list of users to add: ")
    if(filename == None):
        print("Error: no filename entered.")
    else:
        f = open(filename)
        for line in f:
            line.strip()
            line = line.split()
            if(len(line) == 0):
                continue;
            if(line[3].isdigit() == True):
                newuser = User(line[0], line[1], line[2])
            print(line)
            os.system("/usr/sbin/useradd " + newuser.username + " -g " + newuser.group)


main()