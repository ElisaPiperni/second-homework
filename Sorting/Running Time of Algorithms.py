#Running Time of Algorithms

s = int(input())
ar = list(map(int, input().split()))
count = 0

for i in range(1, len(ar)):
    for j in range(0, i):
        if ar[i] < ar[j]:
            value = ar.pop(i)
            ar.insert(j, value)
            count += i-j
print (count)