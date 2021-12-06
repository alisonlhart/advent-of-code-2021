"""
advent of code: day 3
author: @alisonlhart
"""
list_text=[]
gamma=""
epsilon=""
size=1
x=0
y=0

with open("/home/ali/python_learning/advent_of_code/inputs/input_day3.txt") as file: 
    for line in file:
        line=line.strip()
        size=len(line)
        list_text.append(line)



while(x<size):
    zero_count=0
    one_count=0
    for string_x in list_text:
        if string_x[y]=="0":
            zero_count+=1
        else:
            one_count+=1
    if zero_count>one_count:
        gamma+="0"
        epsilon+="1"
        print("ZERO")
    else:
        gamma+="1"
        epsilon+="0"
    x+=1
    y+=1

gamma=int(gamma,2)
epsilon=int(epsilon,2)
        
print("GAMMA: "+str(gamma)+"\nEPSILON: "+str(epsilon))

print("Multiplied total: "+str(gamma*epsilon))