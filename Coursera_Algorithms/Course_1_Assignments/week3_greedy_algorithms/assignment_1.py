#python 3

#Given that we have 1, 5, 10 denominations, we need to get the change with minimum number of coins.
#For example, if we have 28 as input, then we can use two 10 coins, one 5 coins and one 3 coins.
#Therefore we need 6 coins total, and this is the minimum possible coins. Any other combination like 
#three 5 coins, one 10 coin and three 1 coins will give us 7 coins total.

#Our greedy choice should be use as many high denominations as possible 
#Let us check if this is a safe move:

#Assume that for 28, the optimal choice is three 5 coins, one 10 coin and three 1 coins. 
#But the three 5 coins can be replaced with one 5 coin and one 10 coin. So the required number of 
#coins decrease from 7 to 6.

#Algorithm:
#Use the highest denomination, and get as many coins as possible to make up the given money
#Check if there is any leftover money. If yes, use the next highest denomination, and repeat again.

#The complexity of this algorithm is O(N), where N = number of different denominations

n = int(input())

denominations = [10, 5, 1]
total_coins = 0

for i in denominations:
    total_coins += n//i
    n = n%i
print(total_coins)	
    