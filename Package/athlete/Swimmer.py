# Carson Matz, cmatz@usc.edu
# ITP 216, Fall 2022
# Section: 32081
# Assigment 5
# Description:
# System for holding Olympic swimmer and boxer information

from .Athlete import Athlete

class Swimmer(Athlete):
    """ class for swimmer """
    # initialize swimmer count
    swimmer_count = 0

    # initializer
    def __init__(self, name_param, dob_param, origin_param, medals_param, strokes):
        super().__init__(name_param, dob_param, origin_param, medals_param)
        self.strokes = strokes
        Swimmer.swimmer_count += 1

    # print out info on swimmer
    def __str__(self):
        return self.name + " is a swimmer from " + self.origin + " born on " + self.dob + ". " + \
               self.name + " knows " + str(self.strokes) + ", and has won " + str(len(self.medals)) + \
               " medals: " + str(self.medals) + "."

    # getter
    def get_strokes(self):
        return self.strokes

    # add new stroke
    def add_stroke(self, stroke):
        if stroke not in self.strokes:
            self.strokes.append(stroke)