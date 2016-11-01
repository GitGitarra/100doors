doors = [0]*100

for x in range(1, 100):

    for y in range(x, 100, x+1):

        doors[y] = not doors[y]

print('The following doors are open:', end=' ')

for i, value in enumerate(doors, start=1):

        if value == 1:
            if i == len(doors):
                print(i)
        else:
            if i < 100:
                print(i, end=', ')
            else:
                print(i, end='.')
exit()
