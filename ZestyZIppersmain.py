# Jaden Mack
# Zesty Zippers

import random

# Variables
totalTime = 495
optimalTime = 401
shroomNum = 0
lapCount = 0
laps = 0


# seconds

# mushroom class
class Mushroom:
    def __init__(self, value):
        self.value = value

# returning the value of the mushroom
    def shroomvalue(self):
        shroomvalue = self.value
        return shroomvalue

# instances of class Mushroom
shroomOne = Mushroom(random.randrange(1, 100))
shroomTwo = Mushroom(random.randrange(1, 100))
shroomThree = Mushroom(random.randrange(1, 100))
shroomFour = Mushroom(random.randrange(1, 100))
shroomFive = Mushroom(random.randrange(1, 100))
shroomSix = Mushroom(random.randrange(1, 100))

# variable for the value for mushroom one
shroomOneValue = shroomOne.shroomvalue()
shroomTwoValue = shroomTwo.shroomvalue()
shroomThreeValue = shroomThree.shroomvalue()
shroomFourValue = shroomFour.shroomvalue()
shroomFiveValue = shroomFive.shroomvalue()


# class for shortcut
class Shortcut:
    def __init__(self, time):
        self.time = time
        # time measured in seconds

    def shortcuttime(self):
        shorttime = self.time
        return shorttime



shortcutOne = Shortcut(5)
shortcutTwo = Shortcut(15)
shortcutThree = Shortcut(10)
shortcutFour = Shortcut(5)
shortcutFive = Shortcut(3)

totalShortcuts = 0

# variable for the time of each shortcut
shortcutOneTime = shortcutOne.shortcuttime()
shortcutTwoTime = shortcutTwo.shortcuttime()
shortcutThreeTime = shortcutThree.shortcuttime()
shortcutFourTime = shortcutFour.shortcuttime()
shortcutFiveTime = shortcutFive.shortcuttime()

# while lapCount <= 3:

if shroomOneValue <= 45:
    shroomNum += 1
    print("You have the", shroomNum, "mushroom")

    if shroomNum >= 1:
        print("This shortcut takes", shortcutOneTime, "seconds to travel.")
        print("Keep going to the next shortcut.")
        print("This shortcut takes", shortcutTwoTime, "seconds to travel")
        print("Keep going to the next shortcut.")
        print("This shortcut takes", shortcutThreeTime, "seconds to travel")
        print("Keep going to the next shortcut.")
        print("This shortcut takes", shortcutFourTime, "seconds to travel")
        print("Keep going to the next shortcut.")
        print("This shortcut takes", shortcutFiveTime, "seconds to travel")




