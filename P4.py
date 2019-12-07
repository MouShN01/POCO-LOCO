import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

N = int(input())

a = list()
a = input().split()

for i in range(N):
    i = int(i)
    i+1

P = int(input())
Q, K = map(int, input().split())

del a[P-1:P]
a.insert(Q-1, K)

print(*a)
