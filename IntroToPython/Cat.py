from IntroToPython.Feline import Feline


class Cat(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.call = "meow"


feline = Feline()
print(feline.leg)

cat = Cat()
print(cat.leg)
print(cat.eye)
print(cat.paw)
print(cat.teeth)
print(cat.bite())
