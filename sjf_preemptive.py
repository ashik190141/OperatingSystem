operation, arrivalTime, burstTime, execution, readyQueue = [], [], [], [], []
turnaroundTime, waitingTime, completionTime = [], [], []
noOfProcess=int(input())
totalTime,sum=0,0

for _ in range(noOfProcess):
    process, arrival, burst = map(int, input().strip().split())
    totalTime+=burst
    burstTime.append(burst)
    arrivalTime.append(arrival)
    operation.append((arrival, process, burst))
    turnaroundTime.append(-1)
    waitingTime.append(-1)
    completionTime.append(-1)

operation.sort()

while(sum!=totalTime):

    for i in range(noOfProcess):
        if(sum>=operation[i][0] and operation[i][2]!=0):
            readyQueue.append((operation[i][2],operation[i][0],operation[i][1]))    #b a p

    readyQueue.sort()

    if(readyQueue[0][0]>0):
        sum+=1
        execution.append((readyQueue[0][2],sum))

        first_parameter_arrivalTime= readyQueue[0][1]
        second_parameter_process = readyQueue[0][2]
        third_parameter_burst = readyQueue[0][0] - 1

        operation.remove((first_parameter_arrivalTime, second_parameter_process, third_parameter_burst+1))
        operation.append((first_parameter_arrivalTime,second_parameter_process, third_parameter_burst))
        operation.sort()
        readyQueue=[]

print(execution)

count=0
for i in range(len(execution)-1,-1,-1):
    if(completionTime[execution[i][0]-1] == -1):
        completionTime[execution[i][0]-1]=execution[i][1]
        count+=1
    elif count==noOfProcess:
        break
print(completionTime)

for i in range(noOfProcess):
    turnaroundTime[i]=completionTime[i]-arrivalTime[i]
print(turnaroundTime)

avg=0
for i in range(noOfProcess):
    waitingTime[i]=turnaroundTime[i]-burstTime[i]
    avg+=waitingTime[i]
print(waitingTime)
print(avg/noOfProcess)