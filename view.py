import printcol


def view(dict1):
    """Loops through dictionary dict1
    and prints its content formatted.

    If collection is empty, print out error message

    :param dict1: dictionary contains movies as keys and their attributes in a nested dictionary
    :return:
    """
    if dict != {}:
        for i in dict1:
            printcol.print_collection(dict1, i)
    else:
        print("Error: Collection is empty!\n")
