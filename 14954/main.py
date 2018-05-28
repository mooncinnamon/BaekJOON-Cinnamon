value = input()


def func(var):
    orig = 0
    count = var
    while count == 1 or orig == int(count):
        length = len(str(count))
        val = 0
        for i in range(0, length):
            val += int(str(count)[i])
        count = val
        if orig == 0:
            orig = var

    if count == 1:
        print("HAPPY")
    else:
        print("UNHAPPY")


func(value)
