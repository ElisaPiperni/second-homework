#Diagonal Difference

# !/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

primary_s = 0
secondary_s = 0
for i in range(n):
    primary_s += a[i][i]
    secondary_s += a[i][-i - 1]

diff = abs(primary_s - secondary_s)
print(diff)

