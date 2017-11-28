#Insertion Sort - Part 2

s = int(input())
ar = list(map(int, input().split()))

for i in range(1, len(ar)):
    for j in range(0, i):
        if ar[i] < ar[j]:
            value = ar.pop(i)
            ar.insert(j, value)
    print (' '.join(map(str, ar)))