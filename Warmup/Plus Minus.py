#Plus Minus

# !/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

c_pos = 0
c_neg = 0
c_zero = 0
for i in range(n):
    if arr[i] > 0:
        c_pos += 1
    elif arr[i] == 0:
        c_zero += 1
    else:
        c_neg += 1

print(*("%0.06f" % (c_pos / n), "%0.06f" % (c_neg / n), "%0.06f" % (c_zero / n)), sep='\n')
