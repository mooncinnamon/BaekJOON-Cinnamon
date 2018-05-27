test_case = int(input())


def sum_people(floor_room, room_num):
    sum = floor_room[0]
    for number in range(0, room_num):
        sum += floor_room[number+1]
    return sum


for x in range(test_case):
    floor = int(input())
    room = int(input())

    bottom_floor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    for i in range(0, floor):
        temp_room = []
        for t in range(0, room):
            temp_room.append(sum_people(bottom_floor, t))
        bottom_floor = temp_room
    print(bottom_floor[-1])
