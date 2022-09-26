# Carson Matz, cmatz@usc.edu
# ITP 216, Fall 2022
# Section: 32081
# Assigment 5
# Description:
# System for holding Olympic swimmer and boxer information

class Athlete(object):
    """ class for athlete """
    # initialize athlete count
    athlete_count = 0

    # initializer
    def __init__(self, name_param, dob_param, origin_param, medals_param):
        self.name = name_param
        self.dob = dob_param
        self.origin = origin_param
        self.medals = medals_param
        Athlete.athlete_count += 1

    # getters
    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_origin(self):
        return self.origin

    def get_medals(self):
        return self.medals

    # add a medal to the list
    def add_medal(self, medal_param):
        self.medals.append(medal_param)