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
JUMPOF"name"
JUMPEZ "name"
PUSH
POP
INPUT
OUTPUT
HALT
"""

with open("exampleCode.txt", "r") as f:
	lines = f.readlines()
	for i, line in enumerate(lines):
		line = line.replace("\n", "")
		line = line.split(" ")
		line = [n for n in line if n != ""]
		lines[i] = line
	while([] in lines): lines.remove([])
print(lines)

calculations = ["ADD", "SUB", "INC", "DEC", "ROTLOW", "ROTHIGH", "B2A", "NEG",
               "AND", "OR", "XOR", "NOT"]

programMEM = [0]*256
address = 0
pointers = {}
for i, line in enumerate(lines):
	command = None
	arg = None
	if(":" in line[0]):
		if(len(line) > 1): 
			command = line[1]
			arg = line[2] if len(line) > 2 else None

		if(line[0][:-1] in pointers): 
			print("ERROR:\n Same two pointers at different addresses\n", i, "-", " ".join(line))
			exit()
		else: 
			pointers[line[0][:-1]] = address
	else:
		command = line[0]
		arg = line[1] if len(line) > 1 else None
	
	if(command == None): continue
	command = command.upper()
	if(command == "LDA"):
		programMEM[address] = "LDA"
		programMEM[address+1] = arg
		address += 2
	elif(command == "LAP"):
		programMEM[address] = "LAP"
		programMEM[address+1] = arg
		address += 2
	elif(command == "STA"):
		programMEM[address] = "STA"
		programMEM[address+1] = arg
		address += 2
	elif(command == "LDB"):
		programMEM[address] = "LDB"
		programMEM[address+1] = arg
		address += 2
	elif(command in calculations):
		programMEM[address] = f"CAL,{calculations.index(command)}"
		programMEM[address+1] = "ATA"
		address += 2
	elif(command == "SETCAL"):
		programMEM[address] = f"CAL,{calculations.index(arg)}"
		address += 1
	elif(command == "JUMP"):
		programMEM[address] = "JMP"
		programMEM[address+1] = arg
		address += 2
	elif(command == "JUMPOF"):
		programMEM[address] = "JOF"
		programMEM[address+1] = arg
		address += 2
	elif(command == "JUMPEZ"):
		programMEM[address] = "JEZ"
		programMEM[address+1] = arg
		address += 2
	elif(command == "POP"):
		programMEM[address] = f"POP"
		address += 1
	elif(command == "PUSH"):
		programMEM[address] = f"PSH"
		address += 1
	elif(command == "INPUT"):
		programMEM[address] = f"INP"
		address += 1
	elif(command == "OUTPUT"):
		programMEM[address] = f"OUT"
		address += 1
	elif(command == "HALT"):
		programMEM[address] = f"HLT"
		address += 1
	elif(command == "NOP"):
		address += 1
	elif(command.isdigit()):
		programMEM[address] = int(command)
		address += 1

	if(address > 255):
		print("ERROR:\n runout of memory")
		exit()




for i, data in enumerate(programMEM):
	stripedData = str(data).replace("+", "").replace("-", "")
	if(stripedData in pointers.keys()):
		programMEM[i] = pointers[stripedData] + data.count("+") - data.count("-")


print(pointers)
[print(i, ":", n) for i, n in enumerate(programMEM)]