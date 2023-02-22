pt,wt,apt,at,bt=[],[],[],[],[]
turnAroundTime,completionTime,waitingTime = [],[],[]
n = int(input())
total_time=0
for _ in range(n):
    x, y,z = map(int, input().strip().split())
    total_time+=y
    pt.append((x, y,z))
    apt.append((x, y,z))
    turnAroundTime.append(-1)
    completionTime.append(-1)
    waitingTime.append(-1)
for i in range(total_time):
    wt.append(-1)
pt.sort()
j=pt[0][0]
while(j!=total_time):
    bt=[]
    for i in range(n):
        if(pt[i][0]<=j and pt[i][1]!=0):
            bt.append((pt[i][1], pt[i][0], pt[i][2]))
    bt.sort()
    wt[j]=bt[0][2]
    j+=1
    match=((bt[0][1],bt[0][0],bt[0][2]))
    for i in range(n):
        if(pt[i]==match):
            t0=pt[i][0]
            t1=pt[i][1]-1
            t2=pt[i][2]
            pt[i]=(t0,t1,t2)
            break
print(wt)
for i in range(n):
    pick=i+1
    b=0
    for j in range(total_time,-1,-1):
        if(wt[j-1]==pick and b==0):
            completionTime[i]=j
            b=1
        elif(b==1):
            break
print(completionTime)
for i in range(n):
    turnAroundTime[i]=completionTime[i]-pt[i][0]
print(turnAroundTime)
sum=0
for i in range(n):
    waitingTime[i]=turnAroundTime[i]-apt[i][1]
    sum=sum+waitingTime[i]
averageWaitingTime=sum/n
print(averageWaitingTime)