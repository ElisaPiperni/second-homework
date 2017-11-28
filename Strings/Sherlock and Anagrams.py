#Sherlock and Anagrams


# !/bin/python3

import sys

from collections import Counter


def sherlockAndAnagrams(s):
    pairs = 0
    n = len(s)
    l = list(s)

    for k in range(1, n):       # all the possible sizes of the substrings
        stop = n - k + 1

        for i in range(stop):   # compare each substring with all of its following substrings with the same size, two by two
            c1 = Counter(l[i:i + k])

            for j in range(i + 1, stop):
                c2 = Counter(l[j:j + k])

                if c1 == c2:
                    pairs += 1

    return (pairs)


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)