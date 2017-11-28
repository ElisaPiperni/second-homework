#Counting Sort 2

from collections import Counter

n = int(input())
ar = list(map(int, input().split()))

counts = Counter(ar)
C = []
for i in range(100):
    if i in counts.keys():
        C.append(counts[i])
    else:
        C.append(0)

k = 0
for i in range(len(C)):
    while C[i] > 0:
        ar[k] = i
        k += 1
        C[i] -= 1

print(' '.join(map(str, ar)))
