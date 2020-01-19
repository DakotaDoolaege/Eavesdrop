import random 
from itertools import islice

script_file = "res/pulp_fiction.txt"
size_of_slice = 4
max_dialogue_len = 250

def Sliced(): 
    count = len(open(script_file).readlines())
    partition = random.randint(0,(count-size_of_slice))
    script = open(script_file).readlines()[:(partition+size_of_slice)][partition:]
    

    dialogue=""

    for s in script: 
        dialogue=dialogue+s

    if len(dialogue) > max_dialogue_len:
        return dialogue[0:max_dialogue_len]    
    else:
        return dialogue



Sliced() 


