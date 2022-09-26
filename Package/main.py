# Carson Matz, cmatz@usc.edu
# ITP 216, Fall 2022
# Section: 32081
# Assigment 5
# Description:
# System for holding Olympic swimmer and boxer information

from athlete import Athlete
from athlete import Boxer
from athlete import Swimmer

def main():
    b = Boxer("Carson", "05/07/2002", "Colorado", ["Champion", "winner"], "heavy")
    print(b.__str__())
    b.win_fight()
    b.win_fight()
    print(b.lose_fight())
    print(b.lose_fight())
    print(b.lose_fight())
    print(b.lose_fight())
    print(b.lose_fight())
    print(b.lose_fight())
    print(b.lose_fight())
    print(b.lose_fight())
    print(b.lose_fight())
    print(b.lose_fight())
    print(b.__str__())
    s = Swimmer("Carson", "05/07/2002", "Colorado", ["Champion", "winner"], ["freestyle"])
    s.add_stroke("butterfly")
    print(s.__str__())

if __name__ == '__main__':
    main()