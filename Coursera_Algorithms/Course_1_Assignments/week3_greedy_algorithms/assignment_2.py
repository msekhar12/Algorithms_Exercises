#python 3
#Fractional knapsack

#The complexity of this algorithm is 0(N log(N)) since we are sorting the data
#N = Number of all items available to fill the bag

#Read input:
def read_input():
    n, W = input().split()
    n = int(n)
    W = float(W)

    value = []
    weight = []

    value_per_weight = []
    
    for i in range(n):
        v, w = input().split()
        v = float(v)
        w = float(w)
        weight.append(w)
        value_per_weight.append([v/w,w, i])
    
    return n, W, value_per_weight
    
def fill_knapsack(n, W, value_per_weight):    
    weights = [0] * n
    total_value = 0
    value_per_weight = sorted(value_per_weight, key=lambda x: -x[0])

    for v,w,i in value_per_weight:
        if W == 0:
           return total_value, weights
        a = min(w, W)
        weights[i] = a    
        total_value += a*v
        W = W - a
        
    #If we have only one item, then the above for will get exited just after decrementing W by a
    #So we need to return total_value and weights
    return total_value, weights

n, W, value_per_weight = read_input()
total_value, weights = fill_knapsack(n, W, value_per_weight)
print(total_value)    
