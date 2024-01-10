from machine import Pin
from time import sleep
from random import randint

def int2binlist(data, lenght):
    data = max(min(2**lenght-1, data), 0)
    
    b = bin(data)[2:]
    b = "0"*(lenght - len(b)) + b
    return([int(i) for i in list(b)][::-1])

def goto(adrs):
    adrs = max(min(2**15-1, adrs), 0)
    adrs = int2binlist(adrs, 15)
    for i in range(15):
        addressPins[i].value(adrs[i])
    sleep(0.001)
    
def disable():
    WE.on()
    OE.on()
    CE.on()
    sleep(0.01)
    
def enable():
    WE.on()
    OE.on()
    CE.off()
    sleep(0.01)

def pushData(data):
    WE.on()
    OE.on()
    sleep(0.001)
    
    data = int2binlist(data, 8)
    for i in range(8):
        dataPins[i].init(dataPins[i].OUT)
        dataPins[i].value(data[i])
    sleep(0.001)
    
    WE.off()
    sleep(0.005)
    WE.on()
    sleep(0.001)
    
def pullData():
    WE.on()
    OE.off()
    sleep(0.001)
    
    data = 0
    for i in range(8):
        dataPins[i].init(dataPins[i].IN, dataPins[i].PULL_DOWN)
        data += dataPins[i].value() * 2**i
        
    sleep(0.001)
    OE.on()
    
    return(data)

A14      = Pin(28, Pin.OUT, value = 0)
A12, WE  = Pin(27, Pin.OUT, value = 0),  Pin(0, Pin.OUT, value = 1)
A7,  A13 = Pin(26, Pin.OUT, value = 0),  Pin(1, Pin.OUT, value = 0)
A6,  A8  = Pin(22, Pin.OUT, value = 0),  Pin(2, Pin.OUT, value = 0)
A5,  A9  = Pin(21, Pin.OUT, value = 0),  Pin(3, Pin.OUT, value = 0)
A4,  A11 = Pin(20, Pin.OUT, value = 0),  Pin(4, Pin.OUT, value = 0)
A3,  OE  = Pin(19, Pin.OUT, value = 0),  Pin(5, Pin.OUT, value = 1)
A2,  A10 = Pin(18, Pin.OUT, value = 0),  Pin(6, Pin.OUT, value = 0)
A1,  CE  = Pin(16, Pin.OUT, value = 0),  Pin(7, Pin.OUT, value = 1)
A0,  IO7 = Pin(17, Pin.OUT, value = 0),  Pin(8, Pin.IN, value = 0)
IO0, IO6 = Pin(11, Pin.IN, value = 0), Pin(9, Pin.IN, value = 0)
IO1, IO5 = Pin(12, Pin.IN, value = 0), Pin(10, Pin.IN, value = 0)
IO2, IO4 = Pin(13, Pin.IN, value = 0), Pin(14, Pin.IN, value = 0)
IO3      =                              Pin(15, Pin.IN, value = 0)

addressPins = [A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14]
dataPins = [IO0, IO1, IO2, IO3, IO4, IO5, IO6, IO7]

disable()
enable()

address = 0


file = open("4-Bit ALU Content", "r")
for line in file.readlines()[1:]:
    line = line.replace("\n", "")
    line = line.split(" ")
    
    for data in line:
        if("*" in data):
            count, data = data.split("*")
            count, data = int(count), int(data, 16)
            
            for i in range(count):
                goto(address)
                pushData(data)
                address += 1
        else:
            data = int(data, 16)
            
            goto(address)
            pushData(data)
            address += 1
    print(f"{address}/{2**15}")


disable()