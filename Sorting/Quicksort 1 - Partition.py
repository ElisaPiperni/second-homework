#Quicksort 1 - Partition

n = int(input())
ar = list(map(int,input().split()))
p = ar[0]
left = []
right = []
equal = []

for i in range(n):
    if ar[i] < p:
        left.append(ar[i])
    elif ar[i] == p:
        equal.append(ar[i])
    else:
        right.append(ar[i])

print(' '.join(map(str,left+equal+right)))