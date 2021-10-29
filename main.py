# Terese Mihalcin
# loop through each lap
# while lap < 3

# if random Num > 45 mushroom = false
# else mushroom = true

# while mushroom.count = >=1
# take the shortcut

# Class shortcut (time)
# shortcut.1.time = 30

# lap counter
import random

# variables
totalTimeNoShortcuts = 68
optimalTimeShortcuts = 52
mushroomNum = 0
lapCounter = 0
lap = 0


# seconds


class Mushroom:
    def __init__(self, value):
        self.value = value
        # mushroom_num = mushroom_num + 1  mushroom counter ++

    def getmushval(self):
        print(self.value)


mushroomOne = Mushroom(random.randrange(1, 100))
mushroomTwo = Mushroom(random.randrange(1, 100))
mushroomThree = Mushroom(random.randrange(1, 100))
mushroomFour = Mushroom(random.randrange(1, 100))
mushroomFive = Mushroom(random.randrange(1, 100))
mushroomSix = Mushroom(random.randrange(1, 100))
mushroomOne.getmushval()

class Shortcut:
    def __init__(self, time):
        self.time = time
        # time measured in seconds


shortcutOne = Shortcut(1)
shortcutTwo = Shortcut(5)
shortcutThree = Shortcut(7)

while lapCounter >= 3:

    if mushroomOne <= 45:

        mushroomNum += 1

        # take the shortcut
        # unless shortcutOne
