#Find the Median

n = int(input())
ar = list(map(int, input().split()))

ar.sort()
md = ar[(len(ar)-1)//2]     #in the input n is always odd
print(md)