# LOTP_8-Bit-CPU-V4
This 8-bit CPU project's main goal is to make a usable breadboard computer. Its instruction set spouse to be richer than SAP-1 and as simple it is. I want to write a compiler for it later to relatively complex programs.


## CPU Architecture
```
                       bus
      +------------+ 8 ||| 8 +----------------+
      |instruction |<=>|||<=>|   A register   |
      |register    |   |||   +----------------+       
      +------------+   ||| 4 +-----------+  ||
              ||8      |||==>|calculation|  ||
              \/       |||   | register  |  ||8
       <-+---------+   |||   +-----------+  ||
       <-|microcode|   |||         ||4      ||
       <-|Memory   |   |||         \/       \/
       <-+---------+   ||| 8 +----------------+
              /\       |||<==|       ALU      |
              ||4      |||   +----------------+
+-----+  +---------+ 8 |||        /\     
|clock|--|12address|<=>|||        ||8    
+-----+  | counter |   ||| 8 +----------+ 
         +---------+   |||==>|B register|
          +--------+ 8 |||   +----------+
          |address |<==||| 8 +--------+ 8+-------+
          |register|   |||<=>| stack  |<=| stack |
          +--------+   |||   | Memory |  |counter|
              ||8      |||   +--------+  +-------+
              \/       ||| 8 +---------------+       
          +--------+ 8 |||<==|input register |<== = =
          |program |==>|||   +---------------+<-- - -   
          | Memory |   ||| 8 +---------------+      
          +--------+   |||==>|output register|== = >   
                       |||   +---------------+-- - >   
```

## Instruction Set
```
0: NOP				- Noting
1: LDA [DATA]			- Load next value of program Memory to A register
2: LAP [ADDRESS]		- Take next value as pointer and load data from program Memory to A register
3: STA [ADDRESS]		- Take next value as pointer and Store data from A register to program Memory
4: LDB [DATA]			- Load next value of program Memory to B register
5: CAL [CALCULATION]	        - Make a calculation between A and B register 
6: ATA 	                        - Store ALU's calculation to A Register
7: JMP [ADDRESS]		- Jump immediate
8: JOF [ADDRESS]		- Jump if overflow
9: JEZ [ADDRESS]		- Jump if equal zero 
A: PSH				- Push data from A register to FILO stack
B: POP				- Pop data from FILO stack and write A register
C: INP				- Read data from input and write A register
D: OUT				- Read data from A register and write output
E: 
F: HLT				- Stops clock ticking
```
