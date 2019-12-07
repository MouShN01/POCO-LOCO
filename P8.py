#import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

N = int(input())

a = list()
a = input().split()

M = int(input())

b = list()
b = input().split()

c = sorted(a + b)
c = [int(i) for i in c]

print(*c)
