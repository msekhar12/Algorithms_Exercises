#python 3

def read_input():   
    m = int(input())
    l = []
    for i in range(m):
        a,b = input().split()
        a = int(a)
        b = int(b)
        l.append([a,b])
    return l    

def check_if_overlap(a1, b1, a2, b2):
    if a2 >= a1 and a2 <= b1:
        return [max(a1, a2), min(b1, b2)]
    if a2 > b1:
        return [None, None]
   
   
   



#l = [[1, 3], [1.5, 2.5], [2, 5], [3, 4], [4.55, 4.56], [3, 6], [10,11]]
#l = [[1,3],[2,5],[3,6]]
#l = [[4,7],[1,3],[2,5],[5,6]]

l = read_input()

#Sort the data
l = sorted(l, key=lambda x: (x[0], -x[1]))


n = len(l) 

i = 1

#[[1, 3], [1.5, 2.5], [2, 5], [3, 6], [3, 4], [4.5, 4.56]]
#[[1, 3], [1.5, 2.5], [2, 5], [2.55, 4.56], [3, 6], [3, 4]]
#[[1, 3], [1.5, 2.5], [2, 5], [3, 6], [3, 4], [4.55, 4.56]]
a1,b1 = l[0]
#print(l)

points = []
while i <= n-1:
    #print(l[i][0],l[i][1], l[i+1][0],l[i+1][1])
    #print(a1, b1, l[i][0], l[i][1])
    c1, c2 = check_if_overlap(a1, b1, l[i][0], l[i][1])
    #print(c1,c2)
    if c1 == None:
        #print(a1, b1)
        points.append(b1)
        #total_points += 1
        a1, b1 = l[i]
        #print("New assignment:", l[i])
    else:
        a1, b1 = c1, c2    
    i = i+1

#For the last segment c1, c2 will be none, if there is no overlap with the 
#segment before the last segment. In that cae we will return the last segment's 
#ending coordinate c2 as output    
if c1 != None:
   #print(c1, c2)
   points.append(c2)
   #total_points += 1
else:
   #print(a1, b1)
   points.append(b1)
   #total_points += 1

print(len(points))
print(" ".join([str(i) for i in points]))

#print(l)