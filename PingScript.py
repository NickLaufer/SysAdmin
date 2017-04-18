import os
import subprocess

def ping():
    ping1 = subprocess.Popen('ping 129.21.3.17')
    ping2 = subprocess.Popen('ping www.google.com')
    if(ping1.poll() == 1):
            print("Connection to RIT DNS failed, check connections.")
    else:
            print("Connection to RIT DNS successful.")
    if(ping2.poll() == 1):
            print("Connection to Google failed. Check connections.")
    else:
            print("Connection to Google successful.")


if __name__ == '__main__':
    ping();