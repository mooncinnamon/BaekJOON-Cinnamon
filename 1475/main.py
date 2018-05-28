number = input()

numberCount = [1, 1, 1, 1, 1, 1, 2, 1, 1]
counter = 1

for num in number:
    if int(num) == 9:
        num = 6
    if numberCount[int(num)] > 0:
        numberCount[int(num)] -= 1
    else:
        counter += 1
        for i in range(0, 9):
            numberCount[i] += 1
            if i == 6:
                numberCount[i] += 1
        numberCount[int(num)] -= 1

print(counter)
