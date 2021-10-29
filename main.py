# loop through each lap
# while lap < 3
# mushroomOne

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
# i dont know how to store the mushroom value and use it later in the big while loop

    def mushvalue(self):
        shroomvalue = self.value
        return shroomvalue


mushroomOne = Mushroom(random.randrange(1, 100))
mushroomTwo = Mushroom(random.randrange(1, 100))
mushroomThree = Mushroom(random.randrange(1, 100))
mushroomFour = Mushroom(random.randrange(1, 100))
mushroomFive = Mushroom(random.randrange(1, 100))
mushroomSix = Mushroom(random.randrange(1, 100))


class Shortcut:
    def __init__(self, time):
        self.time = time
        # time measured in seconds


shortcutOne = Shortcut(1)
shortcutTwo = Shortcut(5)
shortcutThree = Shortcut(7)

# while lapCounter <= 3:
mushroomOneValue = mushroomOne.mushvalue()

mushroomOne.mushvalue()

# while lapCounter >= 3:

if mushroomOneValue <= 45:
    print(mushroomOneValue)
    mushroomNum += 1
    print(mushroomNum)

        # take the shortcut
        # unless shortcutOne
