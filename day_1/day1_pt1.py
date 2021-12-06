""" advent of code - day 1 
    author: @alisonlhart
"""

"""

Goal: Count number of increases from list element to element 
Challenge: Don't do it in a forloop (maybe a while...)
Idea:
- Read the file into a list (turn string into int)
- set comparison var and increase var to 0
- iterate through list, skip at index 0, compare to item, 
- if item is greater than comparison var, add 1 to increase var
- set comparison var value to current item
- repeat until 0

"""

comparison_var=0
increase_var=0

def comparison(list_element, compare_var) -> int:
    return 1 if list_element > compare_var else 0



with open("../inputs/input_day1.txt") as file:
    for value in file:
        value=value.strip()
        value=int(value)
        if (comparison_var!=0 and comparison(value,comparison_var)):
            print(str(value)+" (INCREASED)\n")
            increase_var+=1
        else:
            print(str(value)+" (DECREASED)\n")
        comparison_var=value

    print("Total: "+str(increase_var))
