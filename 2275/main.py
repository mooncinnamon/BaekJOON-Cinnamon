test_case = int(input())



for x in range(test_case):
    floor = int(input())
    room = int(input())

    bottom_floor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    for i in range(1,floor):
        temp_room = []
        for t in range(0,room):
            for y in range(0, t):
                temp_room.append(bottom_floor[y])
        bottom_floor = temp_room
    print(bottom_floor)