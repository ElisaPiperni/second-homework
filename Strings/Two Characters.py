#Two Characters

# !/bin/python3

import sys

from itertools import combinations

s_len = int(input().strip())
s = input().strip()

characters = set(s)
comb = list(combinations(characters, 2))

all_t = []
for c in comb:
    new = ''
    for i in s:
        if i in c:
            new += i
    all_t.append(new)  # list of all the possible two distinct characters strings

alter_t = []
for t in all_t:
    count = 0
    for i in range(len(t) - 1):
        if t[i] != t[i + 1]:
            count += 1
    if count == len(t) - 1:  # if the count is equal to the lenght of the strings all the characters must be alternating
        alter_t.append(t)

if len(alter_t) == 0:
    print('0')
else:
    print(len((max(alter_t, key=len))))  # print the longest of the alternating stings
