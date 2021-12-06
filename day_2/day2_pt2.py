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


with open("../inputs/input_day2.txt") as file:
    for line in file:
        direction_position = line.split(' ')
        direction_position[1] = direction_position[1].strip()

        if('for' in direction_position[0]):
            if aim != 0:
                depth += int(direction_position[1])*aim
                horizontal_pos += int(direction_position[1])
            else:
                horizontal_pos += int(direction_position[1])

        elif('up' in direction_position[0]):
            aim -= int(direction_position[1])

        elif('down' in direction_position[0]):
            aim += int(direction_position[1])

file.close()

print("Multiplied: " + str(horizontal_pos*depth))
