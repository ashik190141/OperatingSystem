str = input()
no_of_frame = int(input())
arr = [' '] * no_of_frame
stringIntoFrame = 0
h=0
m=0
si=0
inputIndex=0 

for i in range(len(str)):
    f=0
    p=0
    for j in range(len(arr)):
        if (stringIntoFrame != (no_of_frame) or arr[j] == -1):
            arr[inputIndex]=str[i]
            inputIndex = (inputIndex + 1) % no_of_frame
            stringIntoFrame +=1 
            m += 1
            p=1
            break
    
    if(p==0):
        for j in range(len(arr)):
            if (arr[j] == str[i]):
                f = 1

        if (f == 0):
            arr[si] = str[i]
            si = (si+1) % no_of_frame
            m+=1
        else:
            h+=1

    print('String is ',str[i])
    for k in range(len(arr)):
        print(arr[k], end=' ')
    print()

hit_ratio = (h/len(str)) * 100
miss_ratio = (m/len(str)) * 100

print('Hit Count = ', h)
print('Miss Count = ',m)
print("Hit Ratio = ", hit_ratio)
print("Miss Ratio = ", miss_ratio)