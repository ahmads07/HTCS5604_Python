print("Hello World!")

Name = input("What is your name?")
try:
    int(Name)
    print("Your name should not be a number")
except:
    print("your name is " + Name)

Age = input("What is your age?")
try:
    int(Age)
    if  int(Age) <0 or int(Age) >110:
        print("Your age is not real")
    else:
        print("Your age is " + Age)
except:
    print("Age must be an integer")








