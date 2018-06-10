import sys
import random
import time

def maximumProductNormal(a,n):
    t0 = time.time()
    product = 0

    for ii in range(n):
        for jj in range(ii + 1, n):
            product = max(product, a[ii] * a[jj])

    t1 = time.time()
    timeNormal = t1 - t0
    return product, timeNormal



def maximumProductFast(a):
    t0 = time.time()
    b = max(a)
    index1 = a.index(b)
    a[index1] = 0
    c = max(a)
    product = b * c
    t1 = time.time()
    timeFast = t1 - t0

    return product, timeFast

def stressTEST(N,M):
    while True:
        n = random.randint(2,N)
        a = [0]*n
        for i in range(n):
            a[i] = random.randint(0,M)

        print('a = ', a)
        resultNormal = maximumProductNormal(a,n)
        resultFast = maximumProductFast(a)

        if resultNormal[0] == resultFast[0]: # the first element is the actual result, the second element is the time taken for the solution
            print('OK')
            print('Normal Time = ',resultNormal[1],' seconds')
            print('Fast Time = ',resultFast[1],' seconds')
            print('Faster solution approx.',int(resultNormal[1]/resultFast[1]),' times faster than normal solution')
        else:
            print('Wrong answer:',resultNormal[0],resultFast[0])
            break

stressTEST(50000,100000000000000)
