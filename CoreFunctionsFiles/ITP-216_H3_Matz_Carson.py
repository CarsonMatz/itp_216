# Carson Matz, cmatz@usc.edu
# ITP 216, Fall 2022
# Section: 32081
# Assigment 3
# Description:
# Organize Robert Deniro movies and print them out based on average rating

# function to read the file into a list line by line
def file_reader(filename):
    file = open(filename, 'r')
    h = file.readline()
    header = h.split(",", 2)
    header[1].strip()
    data = []
    while True:
        l = file.readline()
        if not l:
            break
        else:
            line = l.split(",", 2)
            line[1].strip()
            data.append(line)
    file.close()
    return header, data

def calculate_mean(nums):
    total = 0
    cnt = 0
    for n in nums:
        total += n
        cnt += 1
    mean = total / cnt
    return mean

def find_movies_above_score(movies, mean):
    above = []
    for m in movies:
        score = float(m[1])
        if score >= mean:
            above.append(m)
    return above

def main():
    header, data = file_reader("deniro.csv")
    print("I love Robert Deniro!")
    nums = []
    for m in data:
        #print(m)
        nums.append(int(m[1]))
    avg = calculate_mean(nums)
    print("The average Rotten Tomatoes score for his movies is " + str(avg) + ".")
    above = find_movies_above_score(data, avg)
    print("Of " + str(len(data)) + " movies, " + str(len(above)) + " are above average.")
    print("Here they are: ")
    print('%-10s' % header[0], '%-10s' % header[1], '%-20s' % header[2])
    for m in above:
        print('%-10s' % m[0], '%-10s' % m[1], '%-10s' % m[2])


if __name__ == '__main__':
    main()


