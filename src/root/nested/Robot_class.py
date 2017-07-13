'''
Finished on March, 12, 2017

@author: Mohammed Ali Al-Ameen
'''
from __builtin__ import str
class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.bag = 200
        self.bee_dropped = 0
        self.bee_picked = 0
        self.success = 0
        self.obstacles = 0
    
    def drop_beeper(self,grid):
        self.bee_dropped += 1
        self.bag -= 1
        grid[self.x][self.y] = 1
    
    def pick_beeper(self,grid):
        self.bee_picked += 1
        self.bag += 1
        grid[self.x][self.y] = 0
        
    def move_up(self,grid):
        
        if(self.x - 1 >= 0):
            if(grid[self.x-1][self.y] == 0):
                self.x -= 1
                self.drop_beeper(grid)
                self.success += 1
                print("\nMoved up and dropped a beeper. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
                return True
            
            elif(grid[self.x-1][self.y] == 1):
                self.x -= 1
                self.pick_beeper(grid)
                self.success += 1
                print("\nMoved up and picked a beeper. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
                return True
            
            elif(grid[self.x-1][self.y] == 2):
                print("\nCan't move up. Facing an obstacle. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
                self.obstacles += 1
                return False
            
        elif(self.x - 1 < 0):
            print("\nCan't move up! Out of bounds. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
            return False
    
    def move_down(self,bound,grid):
        if(self.x + 1 >= bound):
            print("\nCan't move down! Out of bounds. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
            return False
        
        else:
            if(grid[self.x + 1][self.y] == 0):
                self.x += 1
                self.drop_beeper(grid)
                self.success += 1
                print("\nMoved down and dropped a beeper. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
                return True
            
            elif(grid[self.x+1][self.y] == 1):
                self.x += 1
                self.pick_beeper(grid)
                self.success += 1
                print("\nMoved down and picked a beeper. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
                return True
            
            elif(grid[self.x+1][self.y] == 2):
                print("\nCan't move down. Facing an obstacle. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
                self.obstacles += 1
                return False
    
    def move_right(self,bound,grid):
        if(self.y+1 >= bound):
            print("\nCan't move right! Out of bounds. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
            return False
        else:
            if(grid[self.x][self.y+1] == 0):
                self.y += 1
                self.drop_beeper(grid)
                self.success += 1
                print("\nMoved right and dropped a beeper. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")    
                return True
            
            elif(grid[self.x][self.y+1] == 1):
                self.y += 1
                self.pick_beeper(grid)
                self.success += 1
                print("\nMoved right and picked a beeper. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
                return True
            
            elif(grid[self.x][self.y+1] == 2):
                print("\nCan't move right. Facing an obstacle. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
                self.obstacles += 1
                return False
    
    def move_left(self,grid):
        if(self.y-1 >= 0):
            if(grid[self.x][self.y-1] == 0):
                self.y -= 1
                self.drop_beeper(grid)
                self.success += 1
                print("\nMoved left and dropped a beeper. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
                return True
            
            elif(grid[self.x][self.y-1] == 1):
                self.y -= 1
                self.pick_beeper(grid)
                self.success += 1
                print("\nMoved left and picked a beeper. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
                return True
            
            elif(grid[self.x][self.y-1] == 2):
                print("\nCan't move left. Facing an obstacle. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
                self.obstacles += 1
                return False
            
        elif(self.y-1 < 0):
            print("\nCan't move left! Out of bounds. I am at: " + (str)(self.x) + " " + (str)(self.y) + " now\n")
            return False