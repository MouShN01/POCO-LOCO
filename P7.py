import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

N = int(input())

P1 = []
P1 = input().split()

M = int(input())

Q1 = []
Q1 = input().split()

Q = [int(i) for i in Q1]

P = [int(i) for i in P1]

if len(Q) > len(P):
    for i in range(len(Q)-len(P)):
        P.append(0)
    l = len(Q)
else:
    for i in range(len(P)-len(Q)):
        Q.append(0)
    l = len(P)

f = []

for i in range(l):
    if i == None:
        i = 0
    f.append(Q[i] + P[i])
    

print(*f)