import threading
import Adafruit_Trellis
import RPi.GPIO as GPIO
import copy
import time

class IOController(threading.Thread):
    def __init__(self):
        self.matrix0 = Adafruit_Trellis.Adafruit_Trellis()
        self.trellis = Adafruit_Trellis.Adafruit_TrellisSet(self.matrix0)
        self.trellisListeners = []
        self.IOListeners = []
        self.numPatterns = 6
        self.switchMode = []
        self.numKeys = 16
        self.pins = [17, 27, 22, 23, 24, 10]
        self.setupTrellis()
        self.setupIO()

    def run(self):
        trellisThread = threading.Thread(target=runTrellis, daemon=True)
        IOThread = threading.Thread(target=runIO, daemon=True)
        trellisThread.start()
        IOThread.start()

    def lightsTestLoop(self):
        for i in range(self.numKeys):
	        self.trellis.setLED(i)
	        self.trellis.writeDisplay()
	        time.sleep(0.05)
        for i in range(numKeys):
	        self.trellis.clrLED(i)
	        self.trellis.writeDisplay()
	        time.sleep(0.05)

    def setupTrellis(self):
        self.Trellis.begin((0x70, 1))

    def registerTrellisListener(self, listener):
        self.trellisListeners.append(listener)

    def notifyTrellisListeners(self, message):
        for listener in self.trellisListeners:
            listener.receiveTrellisMessage(message)

    def runTrellis(self):
        while True:
            if self.trellis.readSwitches():
                for index in range(self.numKeys):
                    if self.trellis.justPressed(index):
                        self.notifyTrellisListeners(index)
            time.sleep(0.05)

    def setupIO(self):
        self.switchMode = [0] * self.numPatterns
        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def registerIOListener(self, listener):
        self.IOListeners.append(listener)

    def notifyIOListeners(self, message):
        for listener in self.IOListeners:
            listener.receiveIOMessage(message)

    def runIO(self):
        while True:
            oldSwitchMode = copy.deepcopy(self.switchMode)
            for index, pin in enumerate(self.pins):
                self.switchMode[index] = GPIO.input(pin)
            if self.switchMode != oldSwitchMode:
                self.notifyIOListeners(self.translateSwitchModeToIndexNum())

            time.sleep(0.1)
                    
    def translateSwitchModeToIndexNum(self):
        for index in range(len(self.pins)):
            if self.switchMode[index] == 0:
                return index

    def setPatternLights(self, pattern, currentStep=-1):
        trellis.clear()
        for index, lightMode in enumerate(pattern):
            if index == currentStep:
                if self.trellis.isLED(index):
                    self.trellis.clrLED(index)
                else:
                    self.trellis.setLED(index)
            elif lightMode:
                self.trellis.setLED(index)
        self.trellis.writeDisplay()

