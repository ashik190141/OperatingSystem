print(f'Enter the number of files: ',end='')
n = int(input())
fileInfo = []

for i in range(n):
    print(f'Enter name of file {i+1}: ',end='')
    fileName = input()
    print(f'Enter the starting block of file {i+1}: ',end='')
    startingBlock = int(input())
    print(f'Enter the length of the block {i+1}: ',end='')
    lengthOfBlock = int(input())
    fileInfo.append((fileName,startingBlock,lengthOfBlock))

print('Enter the search file name: ',end='')
searchFile = input()
for i in range(n):
    if(searchFile == fileInfo[i][0]):
        si = fileInfo[i][1]
        length = fileInfo[i][2]
        break

for i in range(si,si+length):
    print(i,end=' ')
print()