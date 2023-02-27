operation,waitingTime,turnaroundTime,burstTime,execution,ready,arrivalTime=[],[],[],[],[],[],[]
noOfProcess=int(input())
cnt=1

for _ in range(noOfProcess):
    process, arrival, burst = map(int, input().strip().split())
    operation.append((arrival,process,burst))
    waitingTime.append(-1)
    turnaroundTime.append(-1)
    burstTime.append(burst)
    arrivalTime.append(arrival)

operation.sort()
execution.append((operation[0][1],operation[0][2]))
sum=operation[0][2]
operation.pop(0)

while(cnt!=noOfProcess):
    ready=[]

    for i in range(len(operation)):
        if(operation[i][0]<=sum):
            ready.append(operation[i])
    
    if(len(ready)!=0):
        sum+=ready[0][2]
        execution.append((ready[0][1],sum))
        operation.remove(ready[0])
        ready.pop(0)
        cnt+=1
    else:
        sum+=1

print(execution)

for i in range(noOfProcess):
    turnaroundTime[execution[i][0]-1]=execution[i][1]-arrivalTime[execution[i][0]-1]

print(turnaroundTime)

avg=0
for i in range(noOfProcess):
    waitingTime[i]=turnaroundTime[i]-burstTime[i]
    avg+=waitingTime[i]

print(waitingTime)
print(avg/noOfProcess)
'''
wt=[]
bt=[]
sum=0
avg=0
for _ in range(p):
    bt.append(int(input()))
for i in range(p):
    wt.append(sum)
    sum=sum+bt[i]
# for i in range(p):
#     # print('p{}={}')
print(wt)
for i in range(p):
    avg=avg+wt[i]
print(avg/p)
'''
