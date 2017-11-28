#Counting Sort 1

from collections import Counter
n = int(input())
ar = list(map(int, input().split()))

c = Counter(ar)
l = []

for i in range(100):
    if i in c.keys():
        l.append(c[i])
    else:
        l.append(0)
print (' '.join(map(str,l)))