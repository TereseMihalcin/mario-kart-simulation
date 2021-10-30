# Terese Mihalcin
# Track: Ancient Algorithms

import random

# variables i will need
totalTimeNoShortcuts = 68
optimalTimeShortcuts = 52
mushroomNum = 0
lapCounter = 0
lap = 0


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


# ideally I would create an object to iterate over using a for loop and loop through this
# code three times to represent the three laps

# the code here represents one lap
# for x in lap:
while lapCounter != 1:
        if mushroomOneValue <= 45:
            mushroomNum += 1
            print("You have", mushroomNum, "mushroom")

            if mushroomNum >= 1:
                print("this shortcut takes", shortcutOneTime, "second to travel")
                print("we will keep going until we reach the next shortcut")
                print("this shortcut takes", shortcutTwoTime, "seconds to travel, so we will take it")
                mushroomNum -= 1
                print("you now have", mushroomNum, "mushrooms")
                if mushroomFourValue <= 45:
                    mushroomNum += 1
                    print("you hit a mushroom!")
                    print("this next shortcut takes", shortcutThreeTime, "seconds, so we will take it")
                    mushroomNum -= 1
                    if mushroomSixValue <= 45:
                        mushroomNum += 1
                        print("you are now at the finish line and have", mushroomNum, "Mushroom(s)")
                        lapCounter += 1
                    else:
                        print("you are now at the finish line and have", mushroomNum, "Mushroom(s)")
                        lapCounter += 1
                else:
                    print("you cannot take the third shortcut")
                    print("keep going until you hit the finish line")
                    print("you are now at the finish line and have", mushroomNum, "Mushroom(s)")
                    lapCounter +=1
        else:
            print("you do not have a mushroom")
            print("you cannot take first and second shortcut")
            if mushroomTwoValue <= 45:
                mushroomNum += 1
                print("you hit a mushroom!")

                if mushroomThreeValue <= 45:
                    mushroomNum += 1
                    print("you hit a mushroom")
                    print("you have enough mushrooms to take the third shortcut so we will take it")
                    print("you are now at the finish line and have", mushroomNum, "Mushroom(s)")
                    lapCounter += 1
            else:
                if mushroomThreeValue <= 45:
                    mushroomNum += 1
                    print("you hit a mushroom")
                    print("you have enough mushrooms to take the third shortcut so we will take it")
                    # at the third shortcut
                    print("you are now at the finish line and have", mushroomNum, "Mushroom(s)")
                    lapCounter += 1
                else:
                    print("you seem to be pretty bad at getting mushrooms")
                    print("you could not take any shortcuts this lap")
                    print("you are now at the finish line and have", mushroomNum, "Mushroom(s)")
                    lapCounter += 1




