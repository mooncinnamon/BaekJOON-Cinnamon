i = int(input())

for x in range(0, i):
    a, b = map(int, input().split())
    count = 0
    n = 1
    length = b - a
    while (True):
        pow = n * n
        min = pow - n + 1
        max = pow + n
        if min <= length and length <= max:
            if length <= pow:
                count = n * 2 - 1
                break
            else:
                count = n * 2
                break
        n += 1

    print(count)
