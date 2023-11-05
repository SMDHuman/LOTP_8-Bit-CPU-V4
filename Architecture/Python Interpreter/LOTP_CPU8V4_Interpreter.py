def bitwiseNot(x):
	binary = list(bin(x)[2:])
	binary = ["0"]*(8-len(binary)) + binary
	binary = ["1" if i == "0" else "0" for i in binary]
	return(int("".join(binary), 2))

def rotate_list(lst, n):
    for i in range(n):
        lst.insert(0, lst.pop())
    return lst

def represents_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

EEPROM = [None]*256
with open("code.txt") as f:
	for line in f.readlines():
		line = line.split(" ")
		i = int(line[0])
		EEPROM[i] = " ".join(line[1:]).replace("\n", "")
		if(represents_int(EEPROM[i])):
			EEPROM[i] = max(0, min(255, int(EEPROM[i])))

stackEEPROM = [0]*256
stackCounter = 0
counterReg = 0
addressReg = 0
AReg = 0
BReg = 0
inputReg = 0
outputReg = 0
instructionReg = 0
OverflowFlag = 0
while(True):
	addressReg = counterReg
	counterReg += 1
	instructionReg = EEPROM[addressReg]
	match instructionReg:
		case "LDA":
			addressReg = counterReg
			counterReg += 1
			AReg = EEPROM[addressReg]
		case "LAP":
			addressReg = counterReg
			counterReg += 1
			addressReg = EEPROM[addressReg]
			AReg = EEPROM[addressReg]
		case "STA":
			addressReg = counterReg
			counterReg += 1
			addressReg = EEPROM[addressReg]
			EEPROM[addressReg] = AReg
		case "LDB":
			addressReg = counterReg
			counterReg += 1
			BReg = EEPROM[addressReg]
		case "ADD":
			AReg += BReg
			if(AReg	< 0): AReg = 255
			if(AReg	> 255): AReg = 0
		case "INC":
			AReg += 1
			if(AReg	< 0): AReg = 255
			if(AReg	> 255): AReg = 0
		case "SFH":
			binary = list(bin(AReg)[2:])
			binary = ["0"]*(8-len(binary)) + binary
			AReg = int("".join(rotate_list(binary, len(binary)-1)), 2)
		case "A2A":
			AReg = AReg
		case "AND":
			AReg = AReg & BReg
		case "ORG":
			AReg = AReg | BReg
		case "XOR":
			AReg = AReg ^ BReg
		case "B2A":
			AReg = BReg
		case "SUB":
			AReg -= BReg
			if(AReg	< 0): AReg = 255
			if(AReg	> 255): AReg = 0
		case "DEC":
			AReg -= 1
			if(AReg	< 0): AReg = 255
			if(AReg	> 255): AReg = 0
		case "SFL":
			binary = list(bin(AReg)[2:])
			binary = ["0"]*(8-len(binary)) + binary
			AReg = int("".join(rotate_list(binary, 1)), 2)
		case "ANT":
			AReg = bitwiseNot(AReg)
		case "NAN":
			AReg = bitwiseNot(AReg & BReg)
		case "NOR":
			AReg = bitwiseNot(AReg | BReg)
		case "XNR":
			AReg = bitwiseNot(AReg ^ BReg)
		case "BNT":
			AReg = bitwiseNot(BReg)
		case "JMP":
			addressReg = counterReg
			counterReg = EEPROM[addressReg]
		case "OUT":
			outputReg = AReg	
			print(AReg)
		case "HLT":
			break
