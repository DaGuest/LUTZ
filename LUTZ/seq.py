import pygame
import os

class Sequencer():
    def __init__(self, patternBank):
        pygame.mixer.init(frequency=448100, szie=-16, channels=2, buffer=4096)
        pygame.mixer.set_num_channels(64)
        pygame.init()
        self.patternBank = patternBank
        self.step = 0
        self.soundFileBank = ['kick.wav', 'hihat.wav', 'kick.wav', 'hihat.wav', 'kick.wav', 'hihat.wav']
        self.soundBank = []

    def setupSoundBank(self):
        homePath = os.path.expanduser('~')
        for i in range(len(soundFileBank)):
            soundPath = os.path.join(homePath, self.soundFileBank[i])
            soundBank.append(pygame.mixer.Sound(soundBank))

    def performStep(self):
        stepSequence = self.patternBank.getAllPatternSteps()
        for index, stepValue in enumerate(stepSequence):
            if stepValue:
                freeChannel = pygame.find_channel()
                if freeChannel != None:
                    freeChannel.play(soundBank[index])
        self.patternBank.setLightsToCurrentPattern(self.step)
        self.step += 1