from random import random

M = 10
N = 15
list1 = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 11))
        print("%3d" % b[j], end='')
    list1.append(b)
    print('   |', sum(b))

for i in range(M):
    print(" --", end='')
print()

for i in range(M):
    s = 0
    for j in range(N):
        s += list1[j][i]
    print("%3d" % s, end='')
print()