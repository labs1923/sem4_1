import numpy as np
items = int(input("Enter no of items : "))
capacity = int(input("Enter Capacity : "))
pi =[0]+ list(map(int,input("Enter Profits : ").split()))
w = [0]+list(map(int,input("Enter weights : ").split()))
item = list(i for i in range(items+1))
p = np.zeros([items+1, capacity+1],dtype=int)
for i in range(1,items+1):
    for j in range(1,capacity+1):
        l = list()
        a = p[i-1,j]
        if(j<w[i]):
            b = -1
        else:
            b = p[i-1,j-w[i]]+pi[i]
        p[i,j] += int(max(a,b))
m = p[items,capacity]
backtrack = [0]*(items+1)
for i in range(items,0,-1):
    if m in p[i] and m in p[i-1] :
        continue
    else :
        m -= pi[i]
        backtrack[i] = 1
print("maximum profit that can be obtained is ",p[items,capacity])
print("Items are : ")
print([i for i in range(len(backtrack)) if backtrack[i]==1 ])


'''
sample input
7
15
10 5 15 7 6 18 3
2 3 5 7 1 4 1
'''