import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

N = int(input())

a = list()
a = input().split()

for el in a:
    el = int(el)

P = int(input())

a.insert(0, a[P-1])
del a[P:P+1]


print(*a)
