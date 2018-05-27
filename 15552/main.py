import sys

count = int(input())

for i in range(0, count):
    a = [int(x) for x in sys.stdin.readline()[:-1].split()]
    print(a[0] + a[1])

'''
count = int(input())

for i in range(0, count):
    a, b = input().split()
    print(int(a) + int(b))
'''