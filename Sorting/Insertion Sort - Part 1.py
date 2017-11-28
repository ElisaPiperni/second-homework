#Insertion Sort - Part 1

n = int(input())
arr = list(map(int, input().split()))
value = arr[n-1]

i = n-2
while (i >= 0) and (arr[i] > value):
    arr[i+1] = arr[i]
    i -= 1
    s = ' '.join(str(i) for i in arr)
    print(s)
arr[i+1] = value
s = ' '.join(str(i) for i in arr)
print(s)