#Closest Numbers

n = int(input())
ar = list(map(int, input().split()))
ar.sort()

min_diff = max(ar)
pairs = []

for i in range(n - 1):
    diff = abs(ar[i + 1] - ar[i])
    if diff < min_diff:
        min_diff = diff
        pairs = [ar[i], ar[i + 1]]
    elif diff == min_diff:
        pairs.append(ar[i])
        pairs.append(ar[i + 1])

print(*pairs)
