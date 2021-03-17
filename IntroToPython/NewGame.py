from Library import generateANumber, win, stillHaveChance, tryTimesLeft, isValidInput, feedback

myNumber = generateANumber()
tryTimes = 1
totalTimes = 10
num = 0

while stillHaveChance(tryTimes, totalTimes) and (not win(num, myNumber)):
    print("You have " + str(tryTimesLeft(tryTimes, totalTimes)) + " chances left")
    num = input("Please guess a number")
    if isValidInput(num):
        num = int(num)
        print(feedback(num, myNumber))
    else:
        print("You should input a number between 0 to 100")
    tryTimes = tryTimes + 1

if not stillHaveChance(tryTimes, totalTimes):
    print("YOU LOOOOOOOOSE!")
