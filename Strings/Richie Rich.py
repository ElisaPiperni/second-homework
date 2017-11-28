#Richie Rich

# !/bin/python3

import sys


def richieRich(s, n, k):
    l = list(s)
    if n % 2 == 0:
        left = l[:n // 2]
        right = l[n // 2:]
    else:
        left = l[:n // 2]
        right = l[n // 2 + 1:]
        central = l[n // 2]
    right = right[::-1]

    diff = 0
    for i in range(len(left)):
        if left[i] != right[i]:
            diff += 1           # this is the number of changes needed to make the string palindrome
                                # this number must always be greater or equal than k (the maximum number of digits that can be altered)

    for i in range(len(left)):

        if left[i] == right[i] and left[i] != '9':
            if k - 2 >= diff:       # I can "afford" making two changes even if the two digits are already equal
                left[i] = 9
                right[i] = 9
                k -= 2

        if left[i] != right[i]:
            if k >= diff:

                if left[i] == '9' or right[i] == '9':       # if one of the two different digits is 9, I change the other in 9 too
                    right[i] = 9
                    left[i] = 9
                    k -= 1
                    diff -= 1

                else:
                    if k - 2 >= diff - 1:       # if i can "afford" making two changes but removing just one difference
                        left[i] = 9
                        right[i] = 9
                        k -= 2
                        diff -= 1
                    else:
                        m = max([left[i], right[i]])        # I use the greater number to make the two digits equal
                        left[i] = m
                        right[i] = m
                        k -= 1
                        diff -= 1

            else:
                return -1

    left = ''.join(map(str, left))
    right = ''.join(map(str, right[::-1]))

    if n % 2 == 0:
        return left + right
    elif n % 2 != 0 and k > diff:   # if there are still changes available the central digit becomes 9
        return left + '9' + right
    else:
        return left + str(central) + right


n, k = map(int, input().split())
s = input().strip()
result = richieRich(s, n, k)
print(result)