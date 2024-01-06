import pyautogui
import os

class LogisimInterface:
	inputLocs = []
	outputLocs = []

	inputValues = []
	outputValues = []

	inputImgs = ["images/button0.png", "images/button1.png", "images/buttonX.png"]
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
			pyautogui.moveTo(pos.left + pos.width/2, pos.top + pos.height/2)
			pyautogui.click()

		inputXLocs = self._locsToList(pyautogui.locateAllOnScreen(self.inputImgs[-1], confidence = 0.98))
		for pos in inputXLocs:
			pyautogui.moveTo(pos.left + pos.width/2, pos.top + pos.height/2)
			pyautogui.click()


		self.inputLocs = self._locsToList(pyautogui.locateAllOnScreen(self.inputImgs[0], confidence = 0.98))
		self.inputValues = [0] * len(self.inputLocs)

	def setInput(self, index, value):
		if(self.inputValues[index] != value):
			pos = self.inputLocs[index]
			pyautogui.moveTo(pos.left + pos.width/2, pos.top + pos.height/2)
			pyautogui.click()
			self.inputValues[index] = value

	def getValue(self, index):
		...  

	def setAllInputs(self, values):
		if(len(self.inputValues) < len(values)):
			print("Given values much more than number of inputs")
			exit()
		
		values += [0] * (len(self.inputValues) - len(values))
		for i, v in enumerate(values):
			self.setInput(i, v)

	def getAllOutputs(self):
		...

if(__name__ == "__main__"):
	import keyboard
	logi = LogisimInterface()

	while(not keyboard.is_pressed("enter")):pass
	while(keyboard.is_pressed("enter")):pass

	logi.scanCircuit()