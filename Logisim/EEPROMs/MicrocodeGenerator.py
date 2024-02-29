R_ADCOUNT = 0b0001 # Read Address Counter
R_PMEM = 0b0010 # Read Program Memory
R_IREG = 0b0011 # Read Instruction Register
R_AREG = 0b0100 # Read A Register
R_INREG = 0b0101 # Read Input Register
R_SMEM = 0b0110 # Read Stack Memory
R_ALU = 0b0111 # Read ALU

W_ADCOUNT = 0b00010000 # Write Address Counter
W_ADREG = 0b00100000 # Write Adress Register
W_PMEM = 0b00110000 # Write Program Memory
W_IREG = 0b01000000 # Write Instruction Register
W_AREG = 0b01010000 # Write A Register
W_BREG = 0b01100000 # Write B Register
W_CALREG = 0b01110000 # Write Calculation Register
W_OUTREG = 0b10000000 # Write Output Register
W_SMEM = 0b10010000 # Write Stack Memory

CLKHALT = 0b0000000100000000 # Clock Halt
ADCOUNTUP = 0b0000001000000000 # Address Counter Up
STCKCOUNTUP = 0b0000010000000000 # Stack Counter Up
STCKCOUNTDOWN = 0b0000100000000000 # Stack Counter Down
RTSMICROCOUNT = 0b0001000000000000 # Reset Microcode Counter

# ---- ==== ---- === ---- ==== ---- === ---- ==== ---- ===

NON = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, RTSMICROCOUNT]
LDA = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_ADCOUNT|W_ADREG, R_PMEM|W_AREG|ADCOUNTUP , RTSMICROCOUNT]
LAP = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_ADCOUNT|W_ADREG, R_PMEM|W_ADREG|ADCOUNTUP, R_PMEM|W_AREG, RTSMICROCOUNT]
STA = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_ADCOUNT|W_ADREG, R_PMEM|W_ADREG|ADCOUNTUP, W_PMEM|R_AREG, RTSMICROCOUNT]
LDB = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_ADCOUNT|W_ADREG, R_PMEM|W_BREG|ADCOUNTUP , RTSMICROCOUNT]
CAL = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_IREG|W_CALREG  , RTSMICROCOUNT]
ATA = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_ALU|W_AREG     , RTSMICROCOUNT]
JMP = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_ADCOUNT|W_ADREG, R_PMEM|W_ADCOUNT , RTSMICROCOUNT]
JOF = [[R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, RTSMICROCOUNT|ADCOUNTUP], [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_ADCOUNT|W_ADREG, R_PMEM|W_ADCOUNT , RTSMICROCOUNT],
	   [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, RTSMICROCOUNT|ADCOUNTUP], [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_ADCOUNT|W_ADREG, R_PMEM|W_ADCOUNT , RTSMICROCOUNT]]
JEZ = [[R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, RTSMICROCOUNT|ADCOUNTUP], [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, RTSMICROCOUNT|ADCOUNTUP],
	   [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_ADCOUNT|W_ADREG, R_PMEM|W_ADCOUNT , RTSMICROCOUNT], [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_ADCOUNT|W_ADREG, R_PMEM|W_ADCOUNT , RTSMICROCOUNT]]
PSH = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_AREG|W_SMEM, STCKCOUNTUP, RTSMICROCOUNT]
POP = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, STCKCOUNTDOWN, W_AREG|R_SMEM, RTSMICROCOUNT]
INP = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, W_AREG|R_INREG, RTSMICROCOUNT]
OUT = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, R_AREG|W_OUTREG, RTSMICROCOUNT]
HLT = [R_ADCOUNT|W_ADREG, R_PMEM|W_IREG|ADCOUNTUP, CLKHALT | RTSMICROCOUNT]

BOOTLOADER = [[R_ADCOUNT|W_ADREG, ADCOUNTUP, 0               , R_AREG|W_OUTREG, R_INREG|W_PMEM, R_ADCOUNT|W_AREG, RTSMICROCOUNT    , 0        , 0              , 0             , 0               ,  R_ADCOUNT|W_BREG], # Zero 0, Overflow 0
			  [R_ADCOUNT|W_ADREG, ADCOUNTUP, R_ADCOUNT|W_BREG, 0              , 0             , 0               , 0                , 0        , 0              , 0             , 0               ,  R_ADCOUNT|W_BREG,  R_ADCOUNT|W_OUTREG,  R_ADCOUNT|W_ADREG, CLKHALT | RTSMICROCOUNT], # Zero 1, Overflow 0
              [0], # Zero 0, Overflow 1
              [R_ADCOUNT|W_ADREG, ADCOUNTUP, 0               , 0              , 0             , 0               , R_ADCOUNT|W_ADREG, ADCOUNTUP, R_AREG|W_OUTREG, R_INREG|W_PMEM, R_ADCOUNT|W_AREG]] # Zero 1, Overflow 1


instructions = [NON, LDA, LAP, STA, LDB, CAL, ATA, JMP, JOF, JEZ, PSH, POP, INP, OUT, NON, HLT]
microcodeEEPROM = [0]*2**11
for i, inst in enumerate(instructions):
	if(type(inst[0]) != list):
		inst = [inst]*4

	for j, cond in enumerate(inst):
		for n, code in enumerate(cond):
			address = (j<<8)| (i<<4) | n
			print(bin(address))
			microcodeEEPROM[address] = code

for i in range(16):
	for j, cond in enumerate(BOOTLOADER):
		for n, code in enumerate(cond):
			print(code)
			address = (1<<10) | (j<<8)| (i<<4) | n
			microcodeEEPROM[address] = code

print(microcodeEEPROM)

microcodeEEPROM_A = [0]*2**11
microcodeEEPROM_B = [0]*2**11
for address, code in enumerate(microcodeEEPROM):
	microcodeEEPROM_A[address] = code & 0x00FF
	microcodeEEPROM_B[address] = (code & 0xFF00)>>8

with open("MicrocodeEEPROM_A", "w") as f:
	f.write("v2.0 raw\n")
	for data in microcodeEEPROM_A:
		f.write(str(hex(data)[2:])+" ")

with open("MicrocodeEEPROM_B", "w") as f:
	f.write("v2.0 raw\n")
	for data in microcodeEEPROM_B:
		f.write(str(hex(data)[2:])+" ")