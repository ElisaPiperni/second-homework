#Sherlock and the Valid String

# !/bin/python3

import sys

from collections import Counter


def isValid(s):
    c = Counter(s)
    v = list(c.values())
    s = set(v)
    ans = 'NO'

    if len(s) == 1:  # if all the characters have the same frequency the string is valid
        ans = 'YES'

    elif len(s) == 2:  # if the length is 2 there could be just one character with a different frequency
                        # if that is the case I can try to make the string valid by deleting one of its occurrences
        ma_i = v.index(max(s))
        mi_i = v.index(min(s))

        # in two cases I will be able to make the string valid:

        # if the character frequency is greater by 1 in respect to all the others
        v[ma_i] -= 1
        s = set(v)
        if len(s) == 1:
            ans = 'YES'

        # if the character frequency is just 1 and thus I will remove that character by deleting one occurrence
        else:
            v[ma_i] += 1  # to undo the previous action
            v[mi_i] -= 1
            if v[mi_i] == 0:
                v.remove(v[mi_i])
                s = set(v)
                if len(s) == 1:
                    ans = 'YES'

    return (ans)


s = input().strip()
result = isValid(s)
print(result)