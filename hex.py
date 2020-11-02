# Christine Yan
# Period 5
# Cybersecurity Fall 2020

# XOR String Assignment

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
    
def iterate(key, inp):
    str = ""
    count = 0
    while (count < len(inp)):
        str = str + key[count % len(key)]
        count += 1
    return str

def human(key, inp):
    output = ""
    for i in range(len(inp)):
        output = output + chr(ord(key[i]) ^ ord(inp[i]))
    return output
    
def numOut(key, inp):
    output = ""
    for i in range(len(inp)):
        output = output + hex(ord(key[i]) ^ ord(inp[i]))[2:] + " "
    return output

if (len(key) < len(inp)):
    key = iterate(key, inp)
if (mode == "human"):
    print(human(key, inp))
else:
    print(numOut(key, inp))
