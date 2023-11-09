RAC = 0b0001 # Read Address Counter
RPM = 0b0010 # Read Program Memory
RIR = 0b0011 # Read Instruction Register
RAR = 0b0100 # Read A Register
RIP = 0b0101 # Read Input Register
RSM = 0b0110 # Read Stack Memory
RAL = 0b0111 # Read ALU

WAC = 0b00010000 # Write Address Counter
WAD = 0b00100000 # Write Adress Register
WPM = 0b00110000 # Write Program Memory
WIR = 0b01000000 # Write Instruction Register
WAR = 0b01010000 # Write A Register
WBR = 0b01100000 # Write B Register
WCL = 0b01110000 # Write Calculation Register
WOP = 0b10000000 # Write Output Register
WSM = 0b10010000 # Write Stack Memory

CHL = 0b000100000000 # Clock Halt
ACU = 0b001000000000 # Address Counter Up
SCU = 0b010000000000 # Stack Counter Up
SCD = 0b100000000000 # Stack Counter Down
RMC = 0b0001000000000000 # Reset Microcode Counter