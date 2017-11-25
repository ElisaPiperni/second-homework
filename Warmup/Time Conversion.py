#Time Conversion

# !/bin/python3

import sys


def timeConversion(s):
    if s[-2:] == "PM":
        if s[:2] == "12":
            return s[:-2]
        else:
            hh = int(s[:2]) + 12
            return str(hh) + s[2:-2]

    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00" + s[2:-2]
        else:
            return s[:-2]


s = input().strip()
result = timeConversion(s)
print(result)