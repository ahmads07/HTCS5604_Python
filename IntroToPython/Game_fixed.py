from random import randint

# 1. Get a random integer
#myNumber = randint(1, 99)
myNumber = 50

# 2. ask player input a number
# Because we have
i = 0
while i <= 9:  # Set 10 times for guessing because the first has been input from 0

    # ask player to input a number
    print("you have " + str(10 - i) + " chances")
    num = input("Please guess a number:")

    # verify the input number
    try:
        int(num)
        if  int(num) <1 or int(num) >99:
            print("Please input a number between 1 to 99")
        else: # number is invalid
            if int(num) > myNumber:
                print("Your number is higher")
            elif int(num) < myNumber:
                print("Your number is lower")
            else:
                print ("You win")
                break

    except:
        print("Please input a valid number")
    i = i + 1

if i == 10:
    print("You lose")
    print("the numbe ris " +str(myNumber))

# # 3. if the number equal to generate number
# if num == myNumber:
#     print("You win")
#
# # 4. give another chance to player, if their guess is wrong
# num = input("Please input your number: ")
#
# # 5. if the number equal to generate number
# if num == myNumber:
#     print("You win")
#
# # 6. if over 10 times guessing
# i = 0
# while i < 10 and !step3:
#     i = i + 1
#     # repeat step 2
#
# # for step 2, need verification