message = input()

count = [0] * 26
ans_v = '?'
max_v = 0

message = message.upper()

for x in message:
    count[ord(x) - 65] += 1
    if max_v < count[ord(x) - 65]:
        ans_v = x
        max_v = count[ord(x) - 65]
    elif max_v == count[ord(x) - 65]:
        ans_v = '?'

print(ans_v)
