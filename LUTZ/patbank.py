class PatternBank:
    def __init__(self, iocontroller):
        self.patterns = {}
        self.numPatterns = 6
        self.patternLength = 16
        self.iocontroller = iocontroller
        self.iocontroller.registerTrellisListener(self)
        self.iocontroller.registerIOListener(self)
        self.currentPattern = 0

    def setupBank(self):
        for i in range(self.numPatterns):
            self.patterns[i] = [0] * self.patternLength 
        
    def receiveIOMessage(self, message):
        self.currentPattern = message
        self.iocontroller.setPatternLights(self.currentPattern, self.currentStep)

    def receiveTrellisMessage(self, buttonIndex):
        self.patterns[self.currentPattern][buttonIndex] = 1 - self.patterns[self.currentPattern][buttonIndex]

    def setLightsToCurrentPattern(self, step=0):
        self.iocontroller.setPatternLights(self.currentPattern, step)

    def getAllPatternSteps(self, step):
        stepSequence = []
        for i in range(self.numPatterns):
            stepSequence.append(self.patterns[i][step])
        return stepSequence

