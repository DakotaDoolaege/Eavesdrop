import random 
from itertools import islice

def Sliced(): 
    count = len(open("pulp_fiction.txt").readlines(  ))
    partition= random.randint(0,(count-100))
    #print(count)
    #print(partition)
    script= open('pulp_fiction.txt').readlines()[:(partition+100)][partition:]
    
    dialogue=""
    for s in script: 
        print(s , end= "")
        dialogue=dialogue+s 

    #print(dialogue)
    return dialogue



Sliced() 


