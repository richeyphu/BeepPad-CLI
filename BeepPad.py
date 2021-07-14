from winsound import Beep
from math import log2, pow
from time import sleep
from threading import Thread

__author__ = "AkaraSellegg"
__copyright__ = "Copyright 2019, BeepPad Project"
__license__ = "MIT"
__version__ = "0.3.3"
__maintainer__ = "AkaraSellegg"
__status__ = "Prototype"

A4 = 440
C0 = A4 * pow(2, -4.75)
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def getPitch(freq):  # Music, Hertz, Barks
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


def getBeep(key, d=1000, oct=4, mode=1):
    keys = ['a', 'w', 's', 'e', 'd', 'f', 't', 'g', 'y', 'h', 'u', 'j', 'k', 'o', 'l', 'p', ';', "'"]
    print("Now playing\t:", end="")
    if mode == "1":
        for i in key:
            try:
                keyNum = keys.index(i)
                if keyNum <= 11:
                    note = notes[keyNum] + str(oct)
                else:
                    keyNum -= 12
                    note = notes[keyNum] + str(oct + 1)
                print(" [{}]".format(note), end="")
                Beep(getFrequency(note), d)
            except ValueError:
                print(" [  ]", end="")
                sleep(d / 1000)
                # print("Bad Key, please try again...")
    else:
        for i in key.split(' '):
            try:
                i = i.upper() if i[-1].isdigit() else i.upper() + str(oct)

                freq = getFrequency(i)
                print(" [{}]".format(i), end="")
                Beep(freq, d)
            except (ValueError, IndexError):
                print(" [  ]", end="")
                sleep(d / 1000)
    print()


def showTitle():
    line2()
    print("\t\t   BeepPad CLI - Python Edition")
    line2()


def showKeyboard():
    keyboard = """\
  _____________________________________________
  |  ███ ███  |  ███ ███ ███  |  ███ ███  |   |
  |  ███ ███  |  ███ ███ ███  |  ███ ███  |   |
  |  ███ ███  |  ███ ███ ███  |  ███ ███  |   |
  |  █w█ █e█  |  █t█ █y█ █u█  |  █o█ █p█  |   |
  |   |   |   |   |   |   |   |   |   |   |   |
  | a | s | d | f | g | h | j | k | l | ; | ' |
  |___|___|___|___|___|___|___|___|___|___|___|"""
    print(keyboard)


def getConfig():
    print("Please select mode:")
    print(" [1] BeepPad (Default)")
    print(" [2] Chromatic Notation [{Note}{Octave}]")
    line()
    mo = input("Input mode : ")
    line()

    while True:
        try:
            du = int(input("Input duration (ms)      : "))  # ms
            if du > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Bad Value")

    while True:
        try:
            so = int(input("Input start octave (1-9) : "))
            if 1 <= so <= 9:
                break
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Bad Value")

    return mo if mo == "1" or mo == "2" else "1", du, so


def showHelp():
    print(" [help] Show all commands")
    print(" [kb]   Show Keyboard")
    print(" [r]    Restart")
    print(" [exit] Exit")


def line():
    print("-" * 50)


def line2():
    print("=" * 50)


if __name__ == '__main__':
    showTitle()

    while True:
        mode, duration, start_oct = getConfig()

        line()
        showKeyboard()
        line()
        showHelp()
        line()

        while True:
            key = input("Enter Key\t: ").lower()
            if key == "":
                continue
            elif key == "exit" or key == "end":
                line2()
                exit()
            elif key == "r":
                line2()
                break
            elif key == "kb":
                line()
                showKeyboard()
                line()
            elif key == "help":
                line()
                showHelp()
                line()
            else:
                if mode == "1":
                    getBeep(key, duration, start_oct, mode=mode)
                    # thr = Thread(target=getBeep, args=(key, duration, start_oct))
                    # thr.start()
                else:
                    getBeep(key, duration, start_oct, mode=mode)
