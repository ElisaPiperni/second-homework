#Birthday Cake Candles

#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    tall = max(ar)
    return ar.count(tall)


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)