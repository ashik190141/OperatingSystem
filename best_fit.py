process,memory,allocation = [],[],[]
noOfProcess=int(input())
#take input
for _ in range(noOfProcess):
    allocation.append(-1)
process=list(map(int, input().strip().split()))[:noOfProcess]
memory=list(map(int, input().strip().split()))[:noOfProcess]

for i in range(noOfProcess):
    processSize= process[i]     #20

    matching=[]
    for j in range(noOfProcess):
        if(processSize<=memory[j] and allocation[j]==-1):
            matching.append((memory[j]-processSize,j))
    
    matching.sort()
    allocation[matching[0][1]]=i+1

for k in range(noOfProcess):
    if (allocation[k] == -1):
        print(f'{k+1} no partition is not allocated for any process')
    else:
        print(f'{k+1} no Partition is allocated for {allocation[k]} no process')