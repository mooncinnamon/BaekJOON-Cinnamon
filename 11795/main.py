count = int(input())

water = 0
food = 0
medic = 0

for i in range(0, count):
    x, y, z = map(int, input().split())
    water += x
    food += y
    medic += z

    if water >= 30 and food >= 30 and medic >= 30:
        if water <= food and water <= medic:
            print(water)
            food -= water
            medic -= water
            water = 0
        elif food <= water and food <= medic:
            print(food)
            water -= food
            medic -= food
            food = 0
        elif medic <= water and medic <= food:
            print(medic)
            water -= medic
            food -= medic
            medic = 0

    else:
        print("NO")

