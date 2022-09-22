# Carson Matz, cmatz@usc.edu
# ITP 216, Fall 2022
# Section: 32081
# Lab 3
# Description:
# Read content from a file and print out the data.

def file_read_header(filename):
    file = open(filename, 'r')
    string = file.readline()
    file.close()
    return string

def file_read_data(filename):
    file = open(filename, 'r')
    first = file.readline()
    lines = []
    while True:
        line = file.readline()
        if not line:
            break
        else:
            lines.append(line)
    return lines

def main():
    header = file_read_header("oscar_age_female.csv")
    data = file_read_data("oscar_age_female.csv")
    print("Header:")
    print("\t" + header)
    print("Data:")
    for i in data:
        print("\t" + i)


if __name__ == '__main__':
    main()