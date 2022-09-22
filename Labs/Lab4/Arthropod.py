# Carson Matz, cmatz@usc.edu
# ITP 216, Fall 2022
# Section: 32081
# Lab 2
# Description:
# Create classes and inheritance.

import random


class Arthropod(object):
    """ class for arthropod """
    #initializes count to 0
    arthropod_count = 0

    # initializes attributes of each arthropod instance and updates count
    def __init__(self, name_param, color_param, limbs_count_param):
        self.name = name_param
        self.color = color_param
        self.limbs_count = limbs_count_param
        Arthropod.arthropod_count += 1

    # returns the name
    def get_name(self):
        return self.name

    # returns the color
    def get_color(self):
        return self.color

    # returns the number of limbs
    def get_limbs_count(self):
        return self.limbs_count

    # sets the color to the new color provided
    def set_color(self, new_color):
        self.color = new_color

    # subtracts random number of limbs from those that arthropod has
    def lose_fight(self):
        lose = random.randint(0, self.limbs_count)
        self.limbs_count = self.limbs_count - lose

# main to run through and print out attributes for testing purposes
def main():
    carson = Arthropod('carson', 'green', 4)
    print(Arthropod.arthropod_count)
    print(carson.get_name(), carson.get_color(), carson.get_limbs_count())
    carson.set_color("blue")
    print(carson.get_name(), carson.get_color(), carson.get_limbs_count())
    carson.lose_fight()
    print(carson.get_name(), carson.get_color(), carson.get_limbs_count())
    c2 = Arthropod('carson', 'purple', 1)
    print(Arthropod.arthropod_count)


if __name__ == '__main__':
    main()