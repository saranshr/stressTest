# Python3

# Get user input
n = int(input())
inputList = input().split()
a = [0]*len(inputList)

for x in range(0,len(inputList)):
    a[x] = int(inputList[x])

b = max(a)
index1 = a.index(b)

a[index1] = 0


c = max(a)

product = b*c

print(product)