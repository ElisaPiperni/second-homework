#Correctness and the Loop Invariant

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):  #I changed this from j>0 to j>=0 to consider the case when l[i] is the smallest number
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
