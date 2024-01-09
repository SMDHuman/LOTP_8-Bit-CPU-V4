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
