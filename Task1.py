from random import random


def countsum(numericList):
    theSum = 0
    for i in numericList:
        theSum = theSum + i
    return theSum


M = int(input("Enter number of columns: "))
N = int(input("Enter number of rows: "))
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 11))
        print("%3d" % b[j], end='\t')
    a.append(b)
    print('   ', countsum(b))

print()

for i in range(M):
    s = 0
    for j in range(N):
        s += a[j][i]
    print("%3d" % s, end='\t')
print()
