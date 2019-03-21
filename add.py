def add(dict1):
    """Ask for user input for Movie Title, Director, Year, Shelf, and Location to store in dictionary

    :param dict1: dictionary contains movies as keys and their attributes in a nested dictionary
    :return:
    """
    add_or_exit = 'a'
    while add_or_exit.lower() == 'a':

        while True:
            try:
                title = input("\nEnter Movie Title: ")
            except ValueError:
                print("\nNot a Title")
            else:
                # If movie title is already in dictionary dict1, print error message
                if title in dict1:
                    print("\nError: Movie Already In Collection!")
                    break
                else:
                    # Store movie title as a key for dictionary dict1
                    dict1[title] = {}

                    # Retrieve user input for director and store in nested dictionary within dict1
                    dict1[title]["Director"] = input("\nEnter Movie Director: ")

                    while True:
                        try:
                            # Retrieve user input for year and test if its is a valid year
                            year = int(input("\nEnter Movie Release Date: "))
                        except ValueError:
                            print("\nError: Not A Year!")
                        else:
                            # Check to see if year is within the valid range 1888 - 2019
                            if year in range(1888, 2020):
                                dict1[title]["Year"] = str(year)
                                break
                            else:
                                print("\nError: Enter A Valid Year!")
                    # Retrieve user input for shelf and store in nested dictionary within dict1
                    dict1[title]["Shelf"] = input("\nEnter Movie Shelf: ")
                    # Retrieve user input for location and store in nested dictionary within dict1
                    dict1[title]["Location"] = input("\nEnter Movie Location: ")

                break

        add_or_exit = input("\nEnter 'A' to add another movie OR 'E' to exit\n")
