n = int(input())
m = int(input())
m1 = [[int(input()) for j in range(m) ] for i in range(n)]

for i in range(m):
    for j in range(n):
        print(m1[i][j], end=" ")
    print("")
m2 = [[int(input()) for j in range(m) ] for i in range(n)]

for i in range(m):
    for j in range(n):
        print(m2[i][j], end=" ")
    print("")

for i in range(m):
    for j in range(n):
        print(m1[i][j]+m2[i][j], end=" ")
    print("")
