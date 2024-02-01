"""
---COMMANDS---
"name":  			- this will create a variable that will stores raw address of its current location on ram after compilation
NOP					- does nothing
LDA "name/number" 	- load given value on its next address to A Register   
LAP "name" 			- load value with given address from ram to A Register
STA "name" 			- Store value with given address from ram from A Register
LDB "name/number"	- load given value on its next address to B Register   
...
SETCAL "CAL"
JUMP "name"
JUMPOF "name"
JUMPEZ "name"
PUSH
POP
INPUT
OUTPUT
HALT
"""

with open("exampleCodeL1.txt", "r") as f:
	lines = f.readlines()
	for i, line in enumerate(lines):
		line = line.replace("\n", "")
		line = line.split(" ")
		line = [n for n in line if n != ""]
		lines[i] = line
	while([] in lines): lines.remove([])
print(lines)
