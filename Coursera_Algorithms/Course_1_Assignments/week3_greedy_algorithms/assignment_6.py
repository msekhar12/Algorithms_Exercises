#python 3

def read_input():
    n = int(input())
    numbers = input().split()
    return numbers
    

def greater_than_or_equal(a,b):
    if int(a+b) > int(b+a):
       return True
    else:
       return False    
      
      
numbers = read_input()

#some test cases
#9 4 6 1 9
#1 1 10 1 1 10 10 1 1 10 10 10 1 1 1 10 1 1 1 1 10 10 1

#1 1 10 1 1 10 10 1 1 10 10 10 1 1 1 10 1 1 1 1 10 10

#2 8 2 3 6 4 1 1 10 6 3 3 6 1 3 8 4 6 1 10 8 4 10 4 1 3 2 3 2 6 1 5 2 9 8 5 10 8 7 9 6 4 2 6 3 8 8 9 8 2 9 10 3 10 7 5 7 1 7 5 1 4 7 6 1 10 5 4 8 4 2 7 8 1 1 7 4 1 1 9 8 6 5 9 9 3 7 6 3 10 8 10 7 2 5 1 1 9 9 5

#The above input shoud give us the following:
#9999999998888888888887777777776666666666555555554444444443333333333222222222111111111111111101010101010101010



max_number = ""
while len(numbers) > 0:
    max_indx = 0
    i = 1
    while i <= len(numbers) - 1:
        if greater_than_or_equal(numbers[i], numbers[max_indx]):
             max_indx = i
        i += 1         
    
    element = numbers.pop(max_indx)
    max_number = max_number+element
    
print(max_number)    