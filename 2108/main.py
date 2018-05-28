import sys

count = int(input())

num_list = []
temp_dict = {}

input_list = [sys.stdin.readline() for i in range(count)]
input_list = list(map(int, input_list))
for num in input_list:
    num_list.append(num)
    if num in temp_dict:
        temp_dict[num] += 1
    else:
        temp_dict[num] = 1

num_list.sort()
aver = round(sum(num_list) / len(num_list))
middle = num_list[int(len(num_list) / 2)]

print(aver)
print(middle)

value_list = temp_dict.values()
max_value = max(value_list)

many_key = []
for t in temp_dict.keys():
    if temp_dict[t] == max_value:
        many_key.append(t)

if len(many_key) == 1:
    print(many_key[0])
else:
    many_key.sort()
    print(many_key[1])

max_num = int(max(temp_dict.keys()))
min_num = int(min(temp_dict.keys()))
print(max_num - min_num)
