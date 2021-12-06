"""
--- day 2: dive! ---
author: @alisonlhart
"""



"""
COMMANDS

forward
up
down

"""

direction_position = []
depth = 0
horizontal_pos = 0
aim = 0

def position_changer(current_pos,change) -> int:
    return current_pos + change

with open("../inputs/input_day2.txt") as file:
    for line in file:
        direction_position = line.split(' ')
        if('for' in direction_position[0]):
            horizontal_pos=position_changer(horizontal_pos, int(direction_position[1]))
        elif('up' in direction_position[0]):
            depth=position_changer(depth, int(direction_position[1])*-1)
        elif('down' in direction_position[0]):
            depth=position_changer(depth, int(direction_position[1]))

print("Multiplied: "+str(horizontal_pos*depth))
