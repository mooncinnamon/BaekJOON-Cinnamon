count = int(input())

for i in range(0, count):
    height, width, number = map(int, input().split())
    xx = number % height
    yy = number / height

    if xx == 0:
        xx = height
        yy -= 1

    print(int(xx * 100 + yy + 1))
