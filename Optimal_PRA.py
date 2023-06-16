str = input()
no_of_frame = int(input())
arr = [' '] * no_of_frame
stringIntoFrame = 0
h = 0
m = 0
si = 0
inputIndex = 0

for i in range(len(str)):
    f = 0
    p = 0
    ch = str[i]
    foundString = []
    for j in range(len(arr)):
        if (stringIntoFrame != (no_of_frame) or arr[j] == -1):
            arr[inputIndex] = str[i]
            inputIndex = (inputIndex + 1) % no_of_frame
            stringIntoFrame += 1
            m += 1
            p = 1
            break

    if (p == 0):
        for j in range(len(arr)):
            if (arr[j] == str[i]):
                f = 1

        if (f == 0):
            for k in range(len(arr)):
                fnd = str.find(arr[k], i+1, len(str))
                if(fnd != -1):
                    index = str.index(arr[k],i+1,len(str))
                    if(index):
                        foundString.append((index,k,i))
                else:
                    foundString.append((i+1,0,i))
                    break

            foundString.sort(reverse=True)

            frameNo = foundString[0][1]
            stringSequence = foundString[0][2]

            arr[frameNo]= str[stringSequence]
            m+=1

        else:
            h += 1

    print('String is ', str[i])
    for k in range(len(arr)):
        print(arr[k], end=' ')
    print()

hit_ratio = (h/len(str)) * 100
miss_ratio = (m/len(str)) * 100

print('Hit Count = ', h)
print('Miss Count = ', m)
print("Hit Ratio = ", round(hit_ratio,2))
print("Miss Ratio = ", round(miss_ratio,2))
