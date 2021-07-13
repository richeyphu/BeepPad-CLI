from random import randint
from winsound import Beep
from BeepPad import getPitch, getFrequency, notes, line, line2
from time import sleep

__author__ = "AkaraSellegg"
__copyright__ = "Copyright 2019, BeepPad Project"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "AkaraSellegg"
__status__ = "Prototype"


# BeepPad - pitch guessing game
def showTitle():
    line2()
    print("\t\t\tBeepPad - Beep Perfect Game")
    line2()


def gameStart():
    print("Please listen...")
    ran = randint(0, 11) if diff == "H" else randint(0, 6)
    note = notes_set[ran]
    freq = getFrequency(note + "4")
    dura = 3000

    Beep(freq, dura)

    print()
    ans = input("Enter your answer : ")
    print()
    global score
    if ans.upper() == note:
        score += 1
        print("Correct!\t>>[{}]<<".format(note))
    else:
        print("Try again...\t>>[{}]<<".format(note))


def review():
    for i in notes_set:
        note = i
        print(" [{}]".format(note), end="")
        Beep(getFrequency(note + "4"), 400)
    print()


def getDiff():
    print("Please select difficulty:")
    print("\t[E] Easy")
    print("\t[H] Hard")
    return input("Enter difficulty : ").upper()


if __name__ == '__main__':
    showTitle()

    diff = getDiff()

    notes_set = [x for x in notes if len(x) == 1] if diff == "E" else notes

    line()
    review()
    line()

    score = 0
    rounds = 5
    for i in range(1, rounds + 1):
        print("ROUND #{}".format(i))
        print()
        print("Get ready...", end="")
        for count in reversed(range(1, 4)):
            print(" {}".format(count), end="")
            sleep(1)
        print()

        gameStart()
        line() if i < rounds else line2()

    if score == rounds:
        print("\tCongratulations! You are BEEP PERFECT !!!")
    print("Score: {}/{}".format(score, rounds))
    line2()
