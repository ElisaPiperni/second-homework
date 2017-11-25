#Simple Array Sum

#!/bin/python3

import sys

def simpleArraySum(n, ar):
    s = sum(ar)
    return s


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
