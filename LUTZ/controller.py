import iocontroller
import patbank
import seq
import midi
import time

def main():
    iocontrol = iocontroller.iocontroller()
    iocontrol.daemon = True
    iocontrol.lightsTestLoop()
    iocontrol.start()
    patternBank = patbank.PatternBank(iocontrol)
    sequencer = seq.Sequencer(patternBank)
    mid = midi.Midi(sequencer)
    mid.daemon = True
    mid.start()
    while True:
        time.sleep(1)

main()