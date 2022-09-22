# Carson Matz, cmatz@usc.edu
# ITP 216, Fall 2022
# Section: 32081
# Assigment 2 (there is no Assigment 1)
# Description:
# organize pet names by pet type and allow for user manipulation

def main():
    # given initial data with pet nams
    cats_names = ('Cassandra', 'Sir Whiskington', 'Truck')
    dogs_names = {'Barkey McBarkface', 'Leeloo Dallas', 'Taro'}
    parrots_names = ['Squawk', 'Squawk 2: the Squawkquel', 'Larry']

    # counter for number of pets
    pets = 0

    # goes through tuple of cats and converts to a list, adds one to pet counter each time
    cat_list = []
    for c in cats_names:
        s = str(c)
        cat_list.append(s)
        pets += 1
    # goes through map of dogs and converts to a list, adds one to pet counter each time
    dog_list = []
    for d in dogs_names:
        s = str(d)
        dog_list.append(s)
        pets += 1
    # parrots already in list, just adds to pet counter for each item
    for p in parrots_names:
        pets += 1

    # create a map where key is animal name and value is list of that animal's names
    # add in our newly converted initial data
    animals_map = {}
    animals_map['cat'] = cat_list
    animals_map['dog'] = dog_list
    animals_map['parrot'] = parrots_names

    # more given data
    names = ['peter', 'paul', 'mary']
    animals = ('cat', 'cat', 'hamster')
    i = 0
    # goes through given animals list to match and add to map, updating pets counter
    for a in animals:
        pets += 1
        s = str(a)
        n = names[i][0].upper() + names[i][1:]
        # if animal is not already in map, add it
        # otherwise just add name to its respective list
        if s not in animals_map:
            m = [n]
            animals_map[s] = m
        else:
            animals_map[s].append(n)
            i += 1

    # display menu
    print("Hello!")
    print("Please choose from the following options: ")
    print("\t1. See all your pets' names.")
    print("\t2. Add a pet.")
    print("\t3. Exit")
    choice = input("What would you like to do? (1, 2, 3): ")
    print()

    # list with possible options of user input
    options = ['1', '2', '3']

    # keep loop running until user decides to quit
    while choice != '3':
        # keep outputting an error message until they select a valid option
        while choice not in options:
            print("That's not an option.")
            choice = input("What would you like to do? (1, 2, 3): ")
            print()

        # print out number of pets and names organized by animal type
        if choice == '1':
            print("You have " + str(pets) + " pets.")
            for i in animals_map:
                s = i + ": " + animals_map[i][0]
                for j in animals_map[i][1:]:
                    s = s + ", " + j
                print(s)
            print()
        # get input for type of animal and name, add it to the map and count, print out the success message
        elif choice == '2':
            type = input("What kind of animal is this?: ")
            print()
            name = input("What is the name of the " + type + "?: ")
            print()
            pets += 1
            if type not in animals_map:
                m = [name]
                animals_map[type] = m
            else:
                animals_map[type].append(name)
            print("Great! " + name + " the " + type + " is now added to your pets.")
            print()
        # reprint menu
        print("Please choose from the following options: ")
        print("\t1. See all your pets' names.")
        print("\t2. Add a pet.")
        print("\t3. Exit")
        choice = input("What would you like to do? (1, 2, 3): ")
        print()

    print("Goodbye!")
if __name__ == '__main__':
    main()