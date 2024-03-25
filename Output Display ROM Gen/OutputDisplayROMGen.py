segmentDigits = {0   :"11111100",
				 1   :"01100000",
				 2   :"11011010",
				 3   :"11110010",
				 4   :"01100110",
				 5   :"10110110",
				 6   :"10111110",
				 7   :"11100000",
				 8   :"11111110",
				 9   :"11110110",
				 "a" :"11101110",
				 "b" :"00111110",
				 "c" :"10011100",
				 "d" :"01111010",
				 "e" :"10011110",
				 "f" :"10001110", 
				 "-" :"00000010",
				 "00":"00101000",
				 "01":"01101000",
				 "10":"00101100",
				 "11":"01101100",
				 " " :"00000000"}
def get7Digit(n):
	if(type(n) == str and n in "abcdefg"):
		return(segmentDigits[n])
	elif(str(n) in "0123456789" and 0 <= int(n) <= 9 and len(n) == 1):
		n = int(n)
		return(segmentDigits[n])
	else:
		return(segmentDigits[n])


def segment2ROMbyteOrder(byte):
	newByteOrder = [0]*8

	newByteOrder[6] = byte[0] # A
	newByteOrder[7] = byte[1] # B
	newByteOrder[3] = byte[2] # C
	newByteOrder[1] = byte[3] # D
	newByteOrder[2] = byte[4] # E
	newByteOrder[5] = byte[5] # F
	newByteOrder[4] = byte[6] # G
	newByteOrder[0] = byte[7] # .

	newByteOrder = "".join(newByteOrder[::-1])
	return(newByteOrder)


def mode1(number, digit): # unsigned integer
	number = str(number)
	number = " " * (4 - len(number)) + number
	number = number[digit]
	byte = get7Digit(number)
	return(byte)

def mode2(number, digit): # signed integer
	number = number if number < 128 else 127-number
	number = str(number)
	number = " " * (4 - len(number)) + number
	number = number[digit]
	byte = get7Digit(number)
	return(byte)

def mode3(number, digit): # hex
	number = hex(number)[2:]
	number = ("  0" if len(number) == 1 else "  ") + number
	number = number[digit]
	byte = get7Digit(number)
	return(byte)

def mode4(number, digit): # binary
	number = bin(number)[2:]
	number = "0" * (8 - len(number)) + number
	number = number[digit*2:digit*2+2]
	byte = get7Digit(number)
	return(byte)

modes = [mode1, mode2, mode3, mode4]

ROM = ["00"]*2**12
for mode in range(4):
	for digit in range(4):
		for number in range(256):
			byte = modes[mode](number, digit)
			byte = segment2ROMbyteOrder(byte)
			byte = hex(int(byte, 2))[2:]
			byte = byte if len(byte) == 2 else "0" + byte

			address = 0 << 12 | mode << 10 | (3-digit) << 8 | number
			ROM[address] = byte


file = open("OutputDisplayROM", "w")
file.write("v2.0 raw")

for i, data in enumerate(ROM):
	file.write(" " if i % 16 else "\n")
	file.write(data)

file.close()