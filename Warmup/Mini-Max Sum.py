#Mini-Max Sum

#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

s = sum(arr)
mi = min(arr)
ma = max(arr)

print (s-ma, s-mi)
