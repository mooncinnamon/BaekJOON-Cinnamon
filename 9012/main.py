count = int(input())

parenthesis = [input() for i in range(count)]
temp_stack = 0
for x in parenthesis:
    parent_len = int(len(x))
    if parent_len % 2 == 1:
        print('NO')
        continue
    for parent in x:
        if parent == '(':
            temp_stack += 1
        elif parent == ')':
            temp_stack -= 1
        if temp_stack < 0:
            break

    if temp_stack == 0:
        print('YES')
    elif temp_stack != 0:
        print('NO')
    temp_stack = 0


