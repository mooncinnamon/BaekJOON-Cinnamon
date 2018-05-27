i = int(input())

textbook = {}

for x in range (0, i):
    text = input()
    if len(text) in textbook:
        textbook.get(len(text)).append(text)
    else:
        textbook[len(text)] = [text]

keyfile = list(textbook.keys())
keyfile.sort()
for x in keyfile:
    sortlist = list(set(list(textbook.get(x))))
    sortlist.sort()
    for y in sortlist:
        print(y)