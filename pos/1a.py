import sys
p = list(map(int,input("Enter the process names :").split()))
at = list(map(int,input("Enter the arrival time : ").split()))
bt = list(map(int,input("Enter the burst time :").split()))
ct = [0]*len(p)
tat = [0]*len(p)
wt = [0]*len(p)
at_d = at.copy()
v = 0
gant_chart = [0]*len(p)
print(at.index(min(at)))
for i in range(len(p)):
    x = at.index(min(at))
    ct[x] = v + bt[x]
    gant_chart[i] = p[x]
    tat[x] = ct[x] - at[x] 
    wt[x] = tat[x] - bt[x]
    v = ct[x]
    at[x] = sys.maxsize

print("Gantt chart:")
for i in gant_chart:
    print(i,end="|")
print()
    
print("Process   ArrivalTime   BurstTime   CompleteTime   TurnAroundTime  WaitingTime")
for i in range(0,len(p)):
    print("  ",p[i],"   \t",at_d[i],"   \t",bt[i],"\t\t",ct[i],"\t\t",tat[i],"\t\t",wt[i],"\t\t")
print("Average WaitingTime=",sum(wt)/len(wt))
print("Average TurnAroundTime=",sum(tat)/len(tat))
