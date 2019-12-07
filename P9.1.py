#import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = list()

l = True

while l == True:
    N = input("")
    i = N[len(N)-2:len(N)]

    if i == "" + i:
        i = N[-1]

    if N == "push " + i:
        i = int(i)
        if i > 100:
            break
        s.append(i)
        print("ok")

    if N == "pop":
        print(s[-1])
        s.pop()

    if N == "back":
        print(s[-1])

    if N == "size":
        print(len(s))

    if N == "clear":
        s.clear()
        print('ok')

    if N == "exit":
        print("bye")
        l = False