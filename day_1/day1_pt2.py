""" advent of code - day 2
    author: @alisonlhart
"""

"""

Goal: Compare increases between 3 number sums and the next 3 number sums

Idea:
- Read the file into a list (turn string into int)
- While(index!=last2oflist):
- iterate through list, get index+(index+1)+(index+2)
- compare to previous number, if current > previous then add to increase_var 
- set previous to current
- repeat until last 2 of the list

"""
current_total=0
previous_total=0
increased_total=0
value_list=[]
list_size=0


def comparison(current, previous) -> int:
    return 1 if current > previous else 0



with open("../inputs/input.txt") as file:
    for value in file:
        value=value.strip()
        value=int(value)
        value_list.append(value)

     
file.close()
list_size=len(value_list)


for index, element in enumerate(value_list):
    if (list_size-2==index):
        break
    current_total=value_list[index]+value_list[index+1]+value_list[index+2]

    if(previous_total==0):
        print("(N/A)\n")
    elif(previous_total!=0 and comparison(current_total,previous_total)):
        print(str(current_total)+" (INCREASED)\n")
        increased_total+=1
    else:
        print(print(str(current_total)+" (DECREASED)\n"))

    previous_total=current_total


print("Total: "+str(increased_total))
