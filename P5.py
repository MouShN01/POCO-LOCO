import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

N = int(input())

a = list()
a = input().split()

P = input()

for i in range(N):
    i = int(i)
    if P in a:
        a.remove(P)
    i+1



print(*a)
