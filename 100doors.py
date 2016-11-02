doors = [False]*100    #create 100 doors, where 'False' means a closed door 

for x in range(100):    #number of passes by the hallway

    for y in range(x, 100, x+1):    #with each pass, the number of steps between the door and increased by one 

        doors[y] = not doors[y]     #change the status of the door to the opposite

print('The following doors are open: ', end='')    #end='' to continue in the same line

for i, value in enumerate(doors, start=1): #return index and value of doors, start counting from 1

        if value is True:     #checking value of the doors
            if i == len(doors):
                print(i)
            else:
                print(i, end=', ')    #prints the results after comma
exit()
