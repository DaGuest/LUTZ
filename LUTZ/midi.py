import threading
import serial

class Midi(threading.Thread):
    def __init__(self, sequencer):
        self.sequencer = sequencer
        self.listeners = []
        self.ser = serial.Serial('/dev/ttyAMA0', baudrate=31500)
        self.tickCounter = 0

    def run(self):
        self.runMidi()

    def runMidi(self):
        while True:
            raw_data = self.ser.read(1)
            if raw_data == None:
                continue
            data = ord(raw_data)
            if data == 248:
                self.tickCounter += 1
            elif data == 250:
                print('start')
                self.tickCounter = 0
                self.sequencer.performStep()
            elif data == 251:
                print('continue')
            elif data == 252:
                print('stop')
            if tickCounter == 6:
                self.sequencer.performStep()
                self.tickCounter = 0