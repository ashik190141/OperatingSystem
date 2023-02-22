pt, wt, apt, at, bt = [], [], [], [], []
turnAroundTime, completionTime, waitingTime = [], [], []
totalTime, j = 0, 1
n = int(input())
for i in range(n):
    x,z= map(int, input().strip().split())
    w=i+1
    pt.append((x, w, z))  # priority processes BurstTime
    apt.append((x,w, z))
    bt.append((x, w, z))
    totalTime += z
    wt.append(-1)
pt.sort()
apt.sort()
wt[(pt[0][1])-1] = pt[0][2]
sum=pt[0][2]
pt.pop(0)
n-=1
while (sum != totalTime):
    at = []
    for i in range(n):
        if (pt[i][0] <= sum):
            at.append((pt[i][0], pt[i][1], pt[i][2]))# priority  Processes BurstTIme
        else:
            break
    at.sort()
    sum += at[0][2]
    wt[(at[0][1])-1] = sum
    check = (at[0][0], at[0][1], at[0][2])
    pt.remove(check)
    n -= 1
print(wt)
pos=-1
cur=-1
for i in range(len(apt)):
    cur=apt[i]
    for j in range(len(apt)):
        if(cur==bt[j]):
            pos=j
            print(f'process {pos+1} Priority {bt[pos][0]} Burst Time {bt[pos][2]} Waiting Time {wt[pos]}')
avg=0
for i in range(len(apt)):
    avg = avg+wt[i]
print(avg/int(len(apt)))