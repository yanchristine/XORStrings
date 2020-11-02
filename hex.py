# Christine Yan
# Period 5
# Cybersecurity Fall 2020

import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]

key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)
            
def human(key, inp):
    output = ""
    for i in range(len(inp)):
        output = output
    return output
    
def numOut(key, inp):
    output = ""
    for i in range(len(inp)):
        output = output
    return output

if (mode == "human"):
    print(human(key,inp))
else:
    print(numOut(key,inp))
