# Carson Matz, cmatz@usc.edu
# ITP 216, Fall 2022
# Section: 32081
# Homework 4
# Description:
# Create a simplified pokemon battle using classes and inheritance.
import random

from Arthropod import Arthropod

class Insect(Arthropod):
    """ class for Insects that inherits from Arthropods """
    # initializes insect count to 0
    insect_count = 0

    # initializes arachnid instance (uses name, color, and limbs paramaters from arthropod)
    def __init__(self, name_param, color_param, limbs_count_param, wings_count_param):
        super().__init__(name_param, color_param, limbs_count_param)
        self.wings_count = wings_count_param
        Insect.insect_count += 1

    # retrieves insect data to be printed
    def __str__(self):
        return "The", self.color, self.name, "has", str(self.limbs_count), "limbs and", str(self.wings_count), "wings."

    # returns the number of wings the insect has
    def get_wings_count(self):
        return self.wings_count

    # returns the power of the insect
    def get_power(self):
        return self.limbs_count + self.wings_count

    # adds the ability to lose wings to the arthropod lose fight function
    def lose_fight(self):
        Arthropod.lose_fight(self)
        l = random.randint(0, self.wings_count)
        self.wings_count = self.wings_count - l