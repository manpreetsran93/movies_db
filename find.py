import printcol


def find(dict1):
    """Finds movie/s from collection based attribute searched by user

    :param dict1: dictionary contains movies as keys and their attributes in a nested dictionary
    :return:
    """
    if dict1 != {}:
        search = input("Which attribute would you like to search by? Enter: Year, Director, or Shelf\n\n")

        # if user is searching by year, print out movies by that year from the collection
        if search.lower() == "year":
            year = int(input("Enter Year: "))
            for i in dict1:
                if dict1[i]['Year'] == year:
                    printcol.print_collection(dict1, i)
                else:
                    print("No movies from the year {year} in collection\n".format(year=year))

        # if user is searching by director, print out movies by that director from the collection
        elif search.lower() == "director":
            director = input("Enter Director Name: ")
            for i in dict1:
                if dict1[i]['Director'] == director:
                    printcol.print_collection(dict1, i)
                else:
                    print("No movies from the director {director} in collection\n".format(director=director))

        # if user is searching by shelf number, print out movies from that shelf number from the collection
        elif search.lower() == "shelf":

            shelf = input("Enter shelf number: ")
            for i in dict1:
                if dict1[i]['Shelf'] == shelf:
                    printcol.print_collection(dict1, i)
                else:
                    print("No movies from the year {shelf} in collection\n".format(shelf=shelf))

        else:
            print("Not A Valid Attribute!\n")
    else:
        print("Collection is empty!\n")


