from random import randint
from winsound import Beep
from BeepPad import getPitch, getFrequency, notes, line, line2
from time import sleep
from threading import Thread

__author__ = "AkaraSellegg"
__copyright__ = "Copyright 2019, BeepPad Project"
__license__ = "MIT"
__version__ = "0.1.5"
__maintainer__ = "AkaraSellegg"
__status__ = "Prototype"


# BeepPad - pitch guessing game
def showTitle():
    line2()
    print("\t\t\tBeepPad - Beep Perfect Game")
    line2()


def gameStart():
    print("\rPlease listen...")
    if diff != '3':
        ran = (randint(0, 11) if diff == '2' else randint(0, 6))
        note = notes_set[ran]
        freq = getFrequency(note + "4")
    else:
        freq = randint(getFrequency("D1"), getFrequency("B7"))  # 37-3951 Hz
        note = getPitch(freq)[0: -1]
    dura = 3000

    Thread(target=playBeep, args=(freq, dura)).start()
    sleep(1.5)

    print()
    ans = input("Enter your answer : ")
    print()
    global score
    if ans.upper() == note:
        score += 1
        print(">>Correct!\t    >>[{}]<<".format(note))
    else:
        print(">>Try again...\t>>[{}]<<".format(note))


def playBeep(f, d):
    Beep(f, d)


def review():
    for i in notes_set:
        note = i
        print(" [{}]".format(note), end="")
        Beep(getFrequency(note + "4"), 400)
    print()


def getDiff():
    print("Please select difficulty:")
    print("\t[1] Easy")
    print("\t[2] Hard")
    print("\t[3] Nightmare")
    ipt = input("Enter difficulty : ")
    return '1' if ipt not in ('1', '2', '3') else ipt


if __name__ == '__main__':
    showTitle()

    while True:
        diff = getDiff()

        notes_set = [x for x in notes if len(x) == 1] if diff == "1" else notes

        line()
        review()
        line()

        score = 0
        rounds = 5
        for i in range(1, rounds + 1):
            print(">>ROUND #{}".format(i))
            print()
            for count in reversed(range(1, 4)):
                print("\rGet ready... [{}]".format(count), end="")
                sleep(1)
            # print("\rGet ready... [GO!]", end="")

            gameStart()
            line() if i < rounds else line2()

        if score == rounds:
            print("\tCongratulations! You are BEEP PERFECT !!!")
        print(">>Score: {}/{}".format(score, rounds))
        line2()

        if input("Play again? (Y/N) : ").upper() != 'Y':
            print("\t\tThanks for playing, see you again!")
            line()
            exit()
        line()
