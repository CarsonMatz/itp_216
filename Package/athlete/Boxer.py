# Carson Matz, cmatz@usc.edu
# ITP 216, Fall 2022
# Section: 32081
# Assigment 5
# Description:
# System for holding Olympic swimmer and boxer information

from .Athlete import Athlete


class Boxer(Athlete):
    """ class for boxer """
    # initialize boxer count
    boxer_count = 0

    # initializer
    def __init__(self, name_param, dob_param, origin_param, medals_param, weight_class):
        super().__init__(name_param, dob_param, origin_param, medals_param)
        self.weight_class = weight_class
        self.record = [0, 0]
        Boxer.boxer_count += 1

    # print out info on boxer
    def __str__(self):
        return self.name + " is a " + self.weight_class + " from " + self.origin + " born on " + self.dob + ". " + \
               self.name + " has a " + str(self.record[0]) + "-" + str(self.record[1]) + " record, and has won " + \
               str(len(self.medals)) + " medals: " + str(self.medals) + "."

    # getters
    def get_weight_class(self):
        return self.weight_class

    def get_record(self):
        return self.record

    # setter for weight class
    def set_weight_class(self, weight_class_param):
        self.weight_class = weight_class_param

    # function for winning fight
    def win_fight(self):
        self.record[0] += 1

    # function for losing fight
    def lose_fight(self):
        self.record[1] += 1
        if self.record[1] >= 10:
            return "This boxer has retired."
        return str(10 - self.record[1]) + " loss(es) remaining before retirement."
