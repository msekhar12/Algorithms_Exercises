# python 3

import sys
print(sys.version)
print(sys.executable)
# Russian peasants algorithm to multiply 2 large numbers in O(logn) complexity


def multiply(a, b):
    '''
    INPUT:
     Integers a and b (both positive)
    OUTPUT:
     Product of a and b

     Logic:
      1. Declare total=0
      2. If b is 0 then return 0
      3. While a != 0:
         3a. If a is odd:
                 total = total + b
         3b.
             3b1. Divide a by 2 (round down)
             3b2. Multiply b by 2
    '''

    if b == 0:
        return 0

    total = 0
    while a != 0:
        if a % 2 == 1:
            total += b
        a = a >> 1
        b = b << 1
    return total


print(multiply(2, 3))
print(multiply(12, 13))
print(multiply(1222222222222, 3333333333333333333))
print(multiply(12222**1000, 3333**1000))
