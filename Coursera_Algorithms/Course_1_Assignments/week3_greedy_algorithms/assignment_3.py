#python 3

#Advertisement revenue maxima

#Complexity is O(N log(N)) since we need to sort the data

def read_input():
    n = int(input())
    a = input().split()
    a = [int(i) for i in a]
    p = input().split()
    p = [int(i) for i in p]
    
    #Sort the data is desc order
    a = sorted(a, key = lambda x: -x)
    p = sorted(p, key = lambda x: -x)
    
    return a, p

a, p = read_input()

total = 0

for i, j in zip(a,p):
    total += i*j
print(total)    