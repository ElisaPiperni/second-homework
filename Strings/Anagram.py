#Anagram

# !/bin/python3

import sys

def anagram(s):
    length = len(s)
    count = 0
    if length % 2 != 0:
        return -1
    else:
        s1 = list(s[:length // 2])
        s2 = list(s[length // 2:])

        for i in range(len(s1)):
            if s1[i] in s2:
                s2.remove(s1[i])
            else:
                count += 1
        return count


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
