print(f'Enter the number of files: ', end='')
n = int(input())
memory_size = [None] * 100
index_of_memories = []

for i in range(n):
    address_of_blocks = []
    print(f'Enter name of the file {i+1}: ', end='')
    fileName = input()

    print(f'Enter the number of blocks in file {i+1}: ', end='')
    no_of_block = int(input())

    print(f'Index of file {fileName}:',end=' ')
    indexNo = int(input())

    index_of_memories.append((fileName,indexNo))

    for j in range(no_of_block):
        print(f'{j+1} no block address is:', end=' ')
        blocks = int(input())
        address_of_blocks.append(blocks)
        memory_size[blocks] = fileName

    memory_size[indexNo]=address_of_blocks

print('Enter the search file name: ', end='')
searchFile = input()


for i in range(len(index_of_memories)):
    if(searchFile == index_of_memories[i][0]):
        ind = index_of_memories[i][1]
        break

# print(memory_size[ind][0])

for i in range(len(memory_size[ind])):
    print(memory_size[ind][i],end=' ')
print()
