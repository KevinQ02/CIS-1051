
import random

def game2():
    deck = ["B"] * 7 + ["R"] * 2    
    random.shuffle(deck)
    grid = [ deck[0:3],deck[3:6],deck[6:]]
   # for row in range (3):
       # nums = [ ]
        #for col in range(3):
          #  nums.append(deck[row*3 + col])
        #grid.append(nums)
    for row in grid:
        print(row)
    choice = grid[0]
    return"R" not in choice


TRIALS =10000
wins =0

for _ in range(TRIALS):
    if game2() == True:
        wins +=1
print(wins/TRIALS)


















