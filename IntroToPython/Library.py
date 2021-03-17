from random import randint

def generateANumber():
    return randint (1, 99)

def stillHaveChance(tryTimes, TotalTimes):
    if tryTimes <= TotalTimes:
        return True
    return False

def tryTimesLeft(tryTimes, totalTimes):
    return totalTimes - tryTimes

def isValidInput(num ):
    try:
        int(num)
        if  int(num) <1 or int(num) >99:
            return False
        return True
    except:
        return False

def win(num, myNumber):
    if num != myNumber:
        return False
    return True

def feedback(num, myNumber):
    if num < myNumber:
        return "go higher"
    elif num > myNumber:
        return "go lower"
    else:
        return "you win"
