from IntroToPython.Feline import Feline

class Tiger(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.leg = "four"
        self.call = "roar"
        self.paw = "four"
        self.eye = "green"
        self.teeth = "sharp"
        self.bite = "people"


feline = Feline()
print(feline.leg)

tiger = Tiger()
print(tiger.leg)
print(tiger.eye)
print(tiger.call)
print(tiger.paw)
print(tiger.teeth)
print(tiger.bite())

