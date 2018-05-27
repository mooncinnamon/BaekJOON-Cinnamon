loop = int(input())

def gcd(a,b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

def lcm(a, b):
    gcd_v = gcd(a,b)
    return a * b / gcd_v

for run in range(0, loop):
    M, N, x, y = map(int, input().split())
    value = lcm(M, N)

    while x != y and x <= value:
        if x < y:
            x += M
        else:
            y += N

    if x != y:
        print(-1)
    else:
        print(x)
