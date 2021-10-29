# Terese Mihalcin
# Class shortcut (time)
# shortcut.1.time = 30

# lap counter
import random

# variables i will need
totalTimeNoShortcuts = 68
optimalTimeShortcuts = 52
mushroomNum = 0
lapCounter = 0
lap = 0


# seconds

# mushroom class
class Mushroom:
    def __init__(self, value):
        self.value = value

# returning the value of the mushroom
    def mushvalue(self):
        shroomvalue = self.value
        return shroomvalue

# instances of class Mushroom
mushroomOne = Mushroom(random.randrange(1, 100))
mushroomTwo = Mushroom(random.randrange(1, 100))
mushroomThree = Mushroom(random.randrange(1, 100))
mushroomFour = Mushroom(random.randrange(1, 100))
mushroomFive = Mushroom(random.randrange(1, 100))
mushroomSix = Mushroom(random.randrange(1, 100))

# class for shortcut
class Shortcut:
    def __init__(self, time):
        self.time = time
        # time measured in seconds

    def shortcuttime(self):
        sctime = self.time
        return sctime



shortcutOne = Shortcut(1)
shortcutTwo = Shortcut(5)
shortcutThree = Shortcut(7)

# variable for the value for mushroom one
mushroomOneValue = mushroomOne.mushvalue()
mushroomTwoValue = mushroomTwo.mushvalue()
mushroomThreeValue = mushroomThree.mushvalue()
mushroomFourValue = mushroomFour.mushvalue()
mushroomFiveValue = mushroomFive.mushvalue()
mushroomSixValue = mushroomSix.mushvalue()

totalShortcutsTaken = 0

# variable for the time of each shortcut
shortcutOneTime = shortcutOne.shortcuttime()
shortcutTwoTime = shortcutTwo.shortcuttime()
shortcutThreeTime = shortcutThree.shortcuttime()
# while lapCounter <= 3:

if mushroomOneValue <= 45:
    mushroomNum += 1
    print("You have", mushroomNum, "mushroom")

    if mushroomNum >= 1:
        print("this shortcut takes", shortcutOneTime, "second to travel")
        print("we will keep going until we reach the next shortcut")
        print("this shortcut takes", shortcutTwoTime, "seconds to travel, so we will take it")



        # check the time of your shortcut



        # take the shortcut
        # unless shortcutOne
