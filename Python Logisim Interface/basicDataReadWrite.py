import pyLogisimInterface as pli
import keyboard
import time

def binary_to_gray_op(n):
   n = int(n, 2)
   n ^= (n >> 1)

   return bin(n)[2:]

logi = pli.LogisimInterface()

while(not keyboard.is_pressed("enter")):pass
while(keyboard.is_pressed("enter")):pass

logi.scanCircuit()
print(logi.inputValues)

while(not keyboard.is_pressed("enter")):pass
while(keyboard.is_pressed("enter")):pass

for i in range(256):
	x = bin(i)[2:]
	x = binary_to_gray_op(x)
	x = [int(n) for n in x]
	x = [0]*(8-len(x)) + x

	logi.setInput(8, 0)
	logi.setAllInputs(x[::-1])
	logi.setInput(8, 1)
