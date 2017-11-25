#Compare the Triplets

# !/bin/python3

import sys


def comparisonPoints(a, b):
    Alice = 0
    Bob = 0

    if a[0] > b[0]:
        Alice += 1
    elif a[0] < b[0]:
        Bob += 1

    if a[1] > b[1]:
        Alice += 1
    elif a[1] < b[1]:
        Bob += 1

    if a[2] > b[2]:
        Alice += 1
    elif a[2] < b[2]:
        Bob += 1

    return Alice, Bob


a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = comparisonPoints(a, b)
print(' '.join(map(str, result)))
