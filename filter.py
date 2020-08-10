import re
import sys
import time

def filter(string):
    x = str(string)
    x = x.split(' ')
    print(x[9])
    time.sleep(60)

string = sys.stdin.read()

filter(string)
