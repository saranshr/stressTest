# Python3

# Get user input
n = int(input())
inputList = input().split()
a = [0]*len(inputList)

for x in range(0,len(inputList)):
    a[x] = int(inputList[x])
product = 0

for i in range(n):
    for j in range(i+1,n):
        product = max(product, a[i]*a[j])

print(product)