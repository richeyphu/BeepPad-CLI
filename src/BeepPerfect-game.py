from random import randint
from winsound import Beep
from BeepPad import getPitch, getFrequency, notes, line, line2
from time import sleep
from threading import Thread
from sys import maxsize

__author__ = "AkaraSellegg"
__copyright__ = "Copyright 2019, BeepPad Project"
__license__ = "MIT"
__version__ = "0.2.0"
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
        freq = randint(getFrequency("C3"), getFrequency("B5"))  # 131-988 Hz
        note = getPitch(freq)[0: -1]
    dura = 3000

    Thread(target=playBeep, args=(freq, dura)).start()
    sleep(1.5)

    print()
    while True:
        ans = input("Enter your answer : ").upper()
        global score
        if ans == note:
            score += 1
            print("\n>>Correct!\t    >>[{}]<<".format(note))
            break
        elif ans == 'R':
            Thread(target=playBeep, args=(freq, dura)).start()
        elif ans == 'Q':
            line2()
            print(">>RAGE QUIT [{}/{}]".format(score, rounds))
            exit()
        elif ans == 'H':
            line()
            showHelp()
            line()
        else:
            print("\n>>Try again...\t>>[{}]<<".format(note))
            break


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


def getRound():
    r = input("Enter rounds : ")
    return int(r) if r.isdigit() and int(r) > 0 else maxsize


def showHelp():
    print("\t[H] Show help")
    print("\t[R] Play beep again")
    print("\t[Q] Rage quit")


if __name__ == '__main__':
    showTitle()

    while True:
        diff = getDiff()
        rounds = getRound()
        line()

        notes_set = [x for x in notes if len(x) == 1] if diff == "1" else notes
        review()
        line()
        showHelp()
        line()

        score = 0
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
        print(">>Score: {}/{} ({:.2f}%)".format(score, rounds, score / rounds * 100))
        line2()

        if input("Play again? (Y/N) : ").upper() != 'Y':
            line()
            print("\t\tThanks for playing, see you again!")
            line()
            exit()
        line()
