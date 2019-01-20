# python 3
# Max product of 2 numbers from an array of integers

# Input will be 2 lines.
# The first line will contain the number of elements in the array, and the second line will be space separated numbers:


def find_max_product(n, l):
    if n <= 1:
        return None
    comps = 0

    if l[0] > l[1]:
        max_1 = l[0]
        max_2 = l[1]
        comps += 1
    else:
        max_2 = l[0]
        max_1 = l[1]
        comps += 1

    for i in range(2, n):
        if l[i] > max_1:
            max_2 = max_1
            max_1 = l[i]
            comps += 1
        elif l[i] > max_2 and l[i] <= max_1:
            max_2 = l[i]
            comps += 1

    return max_1, max_2, max_1*max_2, comps


n = int(input())
l = [int(x) for x in input().split()]

print(find_max_product(n, l))
