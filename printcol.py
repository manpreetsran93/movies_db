def print_collection(dict1, i):
    """Prints contents from dict1 formatted

    :param dict1: dictionary contains movies as keys and their attributes in a nested dictionary
    :param i: i is keys of the dictionary dict1
    :return:
    """
    print("Movie Title: {title}\n"
          "Movie Director: {director}\n"
          "Movie Release Date: {year}\n"
          "Movie Shelf: {shelf}\n"
          "Movie Location: {location}\n\n".format(title=i,
                                                  director=dict1[i]['Director'],
                                                  year=dict1[i]['Year'],
                                                  shelf=dict1[i]['Shelf'],
                                                  location=dict1[i]['Location']))