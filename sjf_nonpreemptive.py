pt=[]
wt=[]
apt=[]
n = int(input())
for _ in range(n):
    x, y = map(int, input().strip().split())
    pt.append((x,y))
    apt.append((x,y))
for i in range(n):
    wt.append(-1)
rpt=[]
pt.sort()
sum=pt[0][1]
wt[0]=pt[0][0]
pt.pop(0)
n=n-1
while(n!=0):
    rpt=[]
    for i in range(len(pt)):
        if(pt[i][0]<=sum):
            rpt.append((pt[i][1],pt[i][0]))
    rpt.sort()
    p=rpt[0][1]
    q=rpt[0][0]
    for i in range(len(apt)):
        if rpt[0][0]==apt[i][1]:
            pos=i
            break
    wt[pos]=sum
    sum = sum+rpt[0][0]
    pt.remove((p,q))
    n=n-1
print(wt)
avg=0
for i in range(len(apt)):
    avg=avg+abs(wt[i]-apt[i][0])
print(avg/len(apt))