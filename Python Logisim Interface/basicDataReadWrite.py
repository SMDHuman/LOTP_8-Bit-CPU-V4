import pyLogisimInterface as pli
import keyboard
import time

def binary_to_gray_op(n):
   n = int(n, 2)
   n ^= (n >> 1)

   return bin(n)[2:]

logi = pli.LogisimInterface()

logi.scanCircuit()

bits = 8
for i in range(2**bits):
	x = bin(i)[2:]
	x = binary_to_gray_op(x)
	x = [int(n) for n in x]
	x = [0]*(bits-len(x)) + x

	logi.setAllInputs(x[::-1])
	print(x[::-1], logi.getAllOutputs())
