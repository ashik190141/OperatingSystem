operation,burstTime,execution,processQueue,processIndex,arrivalTime=[],[],[],[],[],[]
turnaroundTime,waitingTime=[],[]
noOfProcess=int(input())

for _ in range(noOfProcess):
    process, arrival, burst = map(int, input().strip().split())
    burstTime.append(burst)
    arrivalTime.append(arrival)
    operation.append((arrival,process,burst))
    processIndex.append(-1)
    turnaroundTime.append(-1)
    waitingTime.append(-1)

operation.sort()
execution.append((operation[0][1],operation[0][2]))
sum = operation[0][2]
processIndex[operation[0][1]-1]=1
operation.pop(0)

for i in range(noOfProcess-1):

    for j in range(noOfProcess-1):
        if(operation[j][0]<=sum and processIndex[operation[j][1]-1]==-1):
            processQueue.append((operation[j][2],operation[j][0],operation[j][1]))  #burst arrival process
    
    processQueue.sort()
    sum += processQueue[0][0]
    execution.append((processQueue[0][2],sum))
    processIndex[processQueue[0][2]-1]=1
    processQueue=[]

print(execution)

for i in range(noOfProcess):
    k = execution[i][0]-1
    turnaroundTime[execution[i][0]-1] = execution[i][1] - arrivalTime[execution[i][0]-1]

print(turnaroundTime)

avg = 0
for i in range(noOfProcess):
    waitingTime[i] = turnaroundTime[i]-burstTime[i]
    avg += waitingTime[i]

print(waitingTime)
print(avg/noOfProcess)