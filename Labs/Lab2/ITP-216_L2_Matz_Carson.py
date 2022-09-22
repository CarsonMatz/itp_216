# Carson Matz, cmatz@usc.edu
# ITP 216, Fall 2022
# Section: 32081
# Lab 2 (there is no lab 1)
# Description:
# ask for a user input, convert it to various data types

def main():
    # receive user input
    string = input("Please enter an input to be converted: ")

    # conversions to list and set are easiest
    stringL = list(string)
    stringS = set(string)

    # for loop to go through and add each letter to dictionary and tuple
    stringT = ()
    stringD = {}
    for l in string:
        stringT = stringT + (l,)
        if l in stringD:
            stringD[l] += 1
        else:
            stringD[l] = 1

    # iterate through string and print it out
    s = "string:"
    for l in string:
        s = s + " " + l + ","
    print(s)

    # iterate through list and print it out
    ls = "list:"
    for l in stringL:
        ls = ls + " " + l + ","
    print(ls)

    # iterate through tuple and print it out
    ts = "tuple:"
    for l in stringT:
        ts = ts + " " + l + ","
    print(ts)

    # iterate through set and print it out
    ss = "set:"
    for l in stringS:
        ss = ss + " " + l + ","
    print(ss)

    # iterate through dictionary and print it out
    print("dictionary:")
    for l in stringD:
        print(l + ": " + str(stringD[l]))

if __name__ == '__main__':
    main()