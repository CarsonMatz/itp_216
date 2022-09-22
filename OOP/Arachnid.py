# Carson Matz, cmatz@usc.edu
# ITP 216, Fall 2022
# Section: 32081
# Homework 4
# Description:
# Create a simplified pokemon battle using classes and inheritance.

from Arthropod import Arthropod


class Arachnid(Arthropod):
    """ class for Arachnids that inherits from Arthropods """
    # initializes arachnid count to 0
    arachnid_count = 0

    # initializes arachnid instance (uses name, color, and limbs paramaters from arthropod)
    def __init__(self, name_param, color_param, limbs_count_param, venomous_param):
        super().__init__(name_param, color_param, limbs_count_param)
        self.venomous = venomous_param
        Arachnid.arachnid_count += 1

    # retrieves arachnid data to be printed
    def __str__(self):
        v = ""
        if self.venomous:
            v = "venomous"
        else:
            v = "non-venomous"
        return "The", self.color, v, self.name, "has", str(self.limbs_count), "limbs."

    # returns whether arachnid is venomous
    def get_venomous(self):
        return self.venomous

    # returns power of arachnid depending on venom
    def get_power(self):
        if self.venomous:
            return self.limbs_count*2
        return self.limbs_count