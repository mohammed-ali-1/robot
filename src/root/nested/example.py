'''
Finished on March, 12, 2017

@author: Mohammed Ali Al-Ameen
'''
from __future__ import print_function
from random import randint
from Robot_class import Robot

rows = 10
cols = 10

grid = []

for i in xrange(rows):
    grid.append([])
    for j in xrange(cols):
            grid[i].append(randint(0,2))

for i in xrange(rows):
    for j in xrange(cols):
            print (grid[i][j], end=" ")
    print(end="\n")


stuck_break = False
dirs = ['l','r', 'u', 'd']

init_x = int(raw_input("Enter the initial x of the robot: "))
init_y = int(raw_input("Enter the initial y of the robot: "))

while(not(init_x >= 0 and init_x < rows and init_y >= 0 and init_y < rows)):
    print ("\nThe values you entered are out of bounds. Choose valid values:\n")
    init_x = int(raw_input("Enter the initial x of the robot: "))
    init_y = int(raw_input("Enter the initial y of the robot: "))


while(grid[init_x][init_y] == 2):
    print ("\nCan't put the robot on an obstacle!\n")
    init_x = int(raw_input("Enter the initial x of the robot: "))
    init_y = int(raw_input("Enter the initial y of the robot: "))
    while(not(init_x >= 0 and init_x < rows and init_y >= 0 and init_y < rows)):
        print ("\nThe values you entered are out of bounds. Choose valid values:\n")
        init_x = int(raw_input("Enter the initial x of the robot: "))
        init_y = int(raw_input("Enter the initial y of the robot: "))

direction = raw_input("Enter the initial direction: u (up), d (down), l (left), r (right): ")

while(not(direction == 'u' or direction == 'd' or direction == 'l' or direction == 'r')):
    print("\nInvalid direction. Enter a valid direction like u, d, l, or r.\n");
    direction = raw_input("Enter the initial direction: u (up), d (down), l (left), r (right): ")

num_moves = int(raw_input("\nEnter the numbers of moves: "));

while(num_moves < 0):
    print("\nNumbers of moves can't be negative or zero.\n")
    num_moves = int(raw_input("\nEnter the numbers of moves: "));

rb = Robot(init_x, init_y, direction)

if(rb.x == 0 and rb.y == 0):
    if(grid[0][1] == 2 and grid[1][0] == 2):
        print("\nStuck in the top left corner and can't move anywhere!\n")
        stuck_break = True

elif(rb.x == rows - 1 and rb.y == 0):
    if(grid[rows-2][0] == 2 and grid[rows-1][1] == 2):
        print("\nStuck in the bottom left corner and can't move anywhere!\n")
        stuck_break = True

elif(rb.x == 0 and rb.y == rows - 1):
    if(grid[0][rows-2] == 2 and grid[1][rows-1] == 2):
        print("\nStuck in the top right corner and can't move anywhere!\n")
        stuck_break = True
    
elif(rb.x == rows - 1 and rb.y == rows - 1):
    if(grid[rows-1][rows-2] == 2 and grid[rows-2][rows-1] == 2):
        print("\nStuck in the bottom right corner and can't move anywhere!\n")    
        stuck_break = True
    
elif(rb.x > 0 and rb.x < rows - 1 and rb.y == 0):
    if(grid[rb.x-1][rb.y] == 2 and grid[rb.x][rb.y+1] == 2 and grid[rb.x+1][rb.y] == 2):
        print("\nStuck in the leftmost column and can't move anywhere!\n")    
        stuck_break = True

elif(rb.x == rows - 1 and rb.y > 0 and rb.y < rows - 1):
    if(grid[rb.x+1][rb.y] == 2 and grid[rb.y][rb.y-1] == 2 and grid[rb.x][rb.y+1] == 2):
        print("\nStuck in the bottom row and can't move anywhere!\n")
        stuck_break = True
    
elif(rb.x > 0 and rb.x < rows - 1 and rb.y == rows - 1):
    if(grid[rb.x-1][rb.y] == 2 and grid[rb.x+1][rb.y] == 2 and grid[rb.x][rb.y-1] == 2):
        print("\nStuck in the rightmost column and can't move anywhere!\n")
        stuck_break = True

elif(rb.x == 0 and rb.y > 0 and rb.y < rows - 1):
    if(grid[rb.x][rb.y-1] == 2 and grid[rb.x][rb.y+1] == 2 and grid[rb.x+1][rb.y] == 2):
        print("\nStuck in the top row and can't move anywhere!\n")
        stuck_break = True

elif(rb.x > 0 and rb.x < rows - 1 and rb.y > 0 and rb.y < rows - 1):
    if(grid[rb.x + 1][rb.y] == 2 and grid[rb.x-1][rb.y] == 2 and grid[rb.x][rb.y-1] == 2 and grid[rb.x][rb.y+1] == 2):
        print("\nStuck somewhere in the grid and can't move anywhere!\n")
        stuck_break = True 

while(stuck_break == False and num_moves > 0):
    if(rb.direction == 'u'):
        if(rb.move_up(grid) == True):
            num_moves -= 1
        elif(rb.move_up(grid) == False):
            while(rb.direction == 'u'):
                rb.direction = dirs[randint(0,3)]
    elif (rb.direction == 'd'):
        if (rb.move_down(rows, grid) == True):
            num_moves -= 1
        elif (rb.move_down(rows, grid) == False):                
            while (rb.direction == 'd'):
                rb.direction = dirs[randint(0,3)]
    elif(rb.direction == 'l'):
        if(rb.move_left(grid) == True):
            num_moves -= 1
        elif(rb.move_left(grid) == False):
            while(rb.direction == 'l'):
                rb.direction = dirs[randint(0,3)]    
    elif(rb.direction == 'r'):
        if(rb.move_right(rows, grid)):
            num_moves -= 1
        elif(rb.move_down(rows, grid) == False):
            while(rb.direction == 'r'):
                rb.direction = dirs[randint(0,3)]
                

print("\nThe grid afterwards:\n")

for i in xrange(rows):
    for j in xrange(cols):
            print (grid[i][j], end=" ")
    print(end="\n")

print("\nStatistics:\n")
print("The final position of the robot: (" + (str)(rb.x) + ", " + (str)(rb.y) + ")\n")
print("The number of successful moves: " + (str)(rb.success) +"\n")
print("Beepers dropped: " + (str)(rb.bee_dropped)+"\n")
print("Beepers picked up: " + (str)(rb.bee_picked)+"\n")
print("Number of obstacles faced: " + (str)(rb.obstacles)+"\n")

