p=int(input())

ta=[]
for _ in range(p):
    at=int(input())
    bt=int(input())
    ta.append((at,bt))
ta.sort()
sum=ta[0][0]
wt=[]
for i in range(p):
    if(sum>=ta[i][0]):
        wt.append(sum)
        sum=sum+ta[i][1] #4
        print(ta[i][1])
    else:
        wt.append(ta[i][0])
        sum = sum+(ta[i][0]-sum)+ta[i][1]
        print(ta[i][1])
avg=0
for i in range(p):
    avg=avg+wt[i]-ta[i][0]
print(wt)
print(avg/p)
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
