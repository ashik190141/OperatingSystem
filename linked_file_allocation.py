print(f'Enter the number of files: ', end='')
n = int(input())
fileInfo = []

for i in range(n):
    data_of_blocks = []
    print(f'Enter the file {i+1}: ', end='')
    fileName = input()
    print(f'Enter the number of blocks in file {i+1}: ', end='')
    no_of_block = int(input())
    for j in range(no_of_block):
        print(f'{j+1} no block is',end=' ')
        blocks = int(input())
        data_of_blocks.append(blocks)
    fileInfo.append((fileName,data_of_blocks))

# print(fileInfo)

print('Enter the search file name: ', end='')
searchFile = input()

for i in range(len(fileInfo)):
    if (searchFile == fileInfo[i][0]):
        blocks_of_file = fileInfo[i][1]
        break

for i in range(len(blocks_of_file)):
    print(blocks_of_file[i],end=' ')
print()