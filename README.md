# XORStrings
Cybersecurity Fall 2020 XOR Strings

PART 1: human readable mode

Write a program that takes three inputs.
Given three strings mode, text, and key: it will produce an output string by xor'ing corresponding values together.
input mode: human/numOut
input keyfile is extended ASCII text FILE
input textfile is extended ASCII text FILE
output is the xor'ed value of the text and the key string.

Note:
The output should be the same length as the text.
If the length of the keyfile is shorter than the textfile, loop the key string.


The output should be only the string of the encoded message with no extra output. The @ in the makefile suppresses your run commands from showing up as output.

MAKEFILE:
run:
	@python hex.py $(ARGS)

Usage:
make run ARGS="mode keyfile textfile"

File contents: EXCLUDE THE QUOTES inside your file.
key1 ="A"
key2 ="FISH"
message1="hello"
message2=")$--."
message3=" this is a test"
message4="f=;!5i:;f(s<#:'"

$ make run ARGS="human key1 message1"
python hex.py human key1 message1
)$--.

$ make run ARGS="human key1 message2"
hello

$ make run ARGS="human key2 message3"
f=;!5i:;f(s<#:'

$ make run ARGS="human key2 message4"
 this is a test

PART 2: NumberOutput mode:
When mode is set to NumberOutput, the output should be in space separated hex values:

$ make run ARGS="numOut key1 message1"
29 24 2d 2d 2e

$ make run ARGS="numOut key1 message2"
68 65 6c 6c 6f

$ make run ARGS="numOut key2 message3"
66 3d 3b 21 35 69 3a 3b 66 28 73 3c 23 3a 27

$ make run ARGS="numOut key2 message4"
20 74 68 69 73 20 69 73 20 61 20 74 65 73 74
