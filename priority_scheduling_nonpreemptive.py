pt,wt,apt,at,bt,st=[],[],[],[],[],[]
turnAroundTime,completionTime,waitingTime = [],[],[]
totalTime,j=0,1
n = int(input())
for _ in range(n):
    w,x,y,z = map(int, input().strip().split())
    pt.append((y,w,x,z)) #Arrival processes priority BurstTime
    apt.append((y,w,x,z))
    bt.append((y, w, x, z))
    st.append((x, w, y, z))
    totalTime+=z
    wt.append(-1)
pt.sort()
wt[(pt[0][1])-1] = pt[0][3]
sum=pt[0][3]
print(f'process {pt[0][1]} Priority {pt[0][2]} Arrival Time {pt[0][0]} Burst Time {pt[0][3]} Waiting Time {sum}')
pt.pop(0)
n-=1
st.sort()
while(sum!=totalTime):
    at=[]
    for i in range(n):
        if(pt[i][0]<=sum):
            at.append((pt[i][2],pt[i][0],pt[i][1],pt[i][3])) #priority Arrival Processes BurstTIme
        else:
            break
    at.sort()
    sum+=at[0][3]
    wt[(at[0][2])-1] = sum
    check = (at[0][1], at[0][2], at[0][0], at[0][3])
    pt.remove(check)
    n-=1
print(wt)
avg=0
for i in range(len(apt)):
    wt[i]=wt[i]-apt[i][0]
    avg=avg+wt[i]
print(wt)
pos = -1
cur = -1
for i in range(len(st)):
    cur = st[i]
    for j in range(len(st)):
        if (cur == bt[j]):
            pos = j
            print(f'process {bt[pos][1]} Priority {bt[pos][2]} Arrival Time {bt[pos][0]} Burst Time {bt[pos][3]} Waiting Time {wt[pos]}')
print(avg/int(len(apt)))