from winsound import Beep
from math import log2, pow
from time import sleep
from threading import Thread

__author__ = "AkaraSellegg"
__copyright__ = "Copyright 2019, BeepPad Project"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "AkaraSellegg"
__status__ = "Prototype"

A4 = 440
C0 = A4 * pow(2, -4.75)
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def pitch(freq):  # Music, Hertz, Barks
    h = round(12 * log2(freq / C0))
    octave = h // 12
    n = h % 12
    return notes[n] + str(octave)


def getFrequency(note):
    # notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    octave = int(note[2]) if len(note) == 3 else int(note[1])

    keyNumber = notes.index(note[0:-1]) + 3

    # if (keyNumber < 3):
    #     keyNumber = keyNumber + 12 + ((octave - 1) * 12) + 1
    # else:
    keyNumber = keyNumber + ((octave - 1) * 12) + 1

    return round(A4 * 2 ** ((keyNumber - 49) / 12))


def getBeep(key, d=1000, oct=4):
    keys = ['a', 'w', 's', 'e', 'd', 'f', 't', 'g', 'y', 'h', 'u', 'j', 'k', 'o', 'l', 'p', ';', "'"]
    for i in key:
        try:
            keyNum = keys.index(i)
            if keyNum <= 11:
                Beep(getFrequency(notes[keyNum] + str(oct)), d)
            else:
                keyNum -= 12
                Beep(getFrequency(notes[keyNum] + str(oct + 1)), d)
        except ValueError:
            sleep(d / 1000)
            # print("Bad Key, please try again...")


def showTitle():
    print("=" * 50)
    print("\t\t   BeepPad CLI - Python Edition")
    print("=" * 50)


def showKeyboard():
    keyboard = """\
  _____________________________________________
  |  ███ ███  |  ███ ███ ███  |  ███ ███  |   |
  |  ███ ███  |  ███ ███ ███  |  ███ ███  |   |
  |  █w█ █e█  |  █t█ █y█ █u█  |  █o█ █p█  |   |
  |  ███ ███  |  ███ ███ ███  |  ███ ███  |   |
  |   |   |   |   |   |   |   |   |   |   |   |
  | a | s | d | f | g | h | j | k | l | ; | ' |
  |___|___|___|___|___|___|___|___|___|___|___|"""
    print(keyboard)


if __name__ == '__main__':
    showTitle()

    duration = int(input("Input duration (ms) : "))  # ms
    start_oct = int(input("Input start octave  : "))

    print("-" * 50)
    showKeyboard()
    print("-" * 50)

    while True:
        key = input("Enter Key : ")
        if key == "":
            break
        # getBeep(key, duration, start_oct)
        thr = Thread(target=getBeep, args=(key, duration, start_oct))
        thr.start()
