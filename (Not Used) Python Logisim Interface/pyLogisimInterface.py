import pyautogui
import mouse
import os
import time

class LogisimInterface:
	inputLocs = []
	outputLocs = []

	inputValues = []
	outputValues = []

	inputImgs = ["images/button0.png", "images/button1.png", "images/buttonX.png"]
	outputImgs = ["images/led0.png", "images/led1.png", "images/ledX.png"]
	handToolImg = "hand.png"

	inputClickCount = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]

	def _locsToList(self, locs):
		try:
			return(list(locs))
		except:
			return([])

	def updateAllIOs(self):
		...

	def scanCircuit(self):
		input1Locs = self._locsToList(pyautogui.locateAllOnScreen(self.inputImgs[1], confidence = 0.98))
		for pos in input1Locs:
			mouse.move(pos.left + pos.width/2, pos.top + pos.height/2)
			mouse.click()

		inputXLocs = self._locsToList(pyautogui.locateAllOnScreen(self.inputImgs[-1], confidence = 0.98))
		for pos in inputXLocs:
			mouse.move(pos.left + pos.width/2, pos.top + pos.height/2)
			mouse.click()


		self.inputLocs = self._locsToList(pyautogui.locateAllOnScreen(self.inputImgs[0], confidence = 0.98))
		self.inputValues = [0] * len(self.inputLocs)


		self.outputLocs += self._locsToList(pyautogui.locateAllOnScreen(self.outputImgs[0], confidence = 0.98))
		self.outputLocs += self._locsToList(pyautogui.locateAllOnScreen(self.outputImgs[1], confidence = 0.98))
		self.outputLocs += self._locsToList(pyautogui.locateAllOnScreen(self.outputImgs[-1], confidence = 0.98))
		
		self.outputLocs = sorted(self.outputLocs , key=lambda k: [k[1], k[0]])
		
		for i, pos in enumerate(self.outputLocs):
			x = int(pos.left + pos.width//2)+3
			y = int(pos.top + pos.height//2)

			self.outputLocs[i] = (x, y)

			self.outputValues.append(0)
			self.getValue(i)

	def setInput(self, index, value):
		if(self.inputValues[index] != value):
			pos = self.inputLocs[index]
			mouse.move(pos.left + pos.width/2, pos.top + pos.height/2)
			mouse.click()
			self.inputValues[index] = value

	def getValue(self, index):
		im = pyautogui.screenshot()
		green = im.getpixel(self.outputLocs[index])[1]

		self.outputValues[index] = {100:0, 210:1, 40:-1}[green]

		return(self.outputValues[index])

	def setAllInputs(self, values):
		if(len(self.inputValues) < len(values)):
			print("Given values much more than number of inputs")
			exit()
		
		values += [0] * (len(self.inputValues) - len(values))
		for i, v in enumerate(values):
			self.setInput(i, v)

	def getAllOutputs(self):
		values = [0]*len(self.outputValues)
		for i in range(len(self.outputValues)):
			values[i] = self.getValue(i)
		return(values)

if(__name__ == "__main__"):
	import keyboard
	logi = LogisimInterface()

	logi.scanCircuit()

	print(logi.outputValues)
	