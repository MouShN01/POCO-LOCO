#import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        print("ok")
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def clear(self):
        print("ok")
        self.items.clear()

    def show(self):
        return self.items

s = Stack()

l = True


while l == True:
    N = input("")
    i = N[-1]

    if N == "push " + i:
        i = int(i)
        s.push(i)

    if N == "show":
        print(s.show())

    if N == "pop":
        print(s.pop())

    if N == "back":
        print(s.peek())

    if N == "size":
        print(s.size())

    if N == "clear":
        s.clear()

    if N == "exit":
        print("bye")
        break