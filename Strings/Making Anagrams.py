#Making Anagrams

# !/bin/python3

import sys

from collections import Counter


def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    diff = (c1 - c2) + (c2 - c1)
    return sum(diff.values())


s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)