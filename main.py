from add import add
from view import view
from find import find

dict1 = {}


def main():
    """Get user input to either add movie to collection,
     view entire collection, find movie from collection,
     or enter 'Q' to quit program.

     object: dict1 is the dictionary the movie collection is stored in.

    :return:
    """

    user_command = (input("Enter 'A' to add a movie to collection\n"
                          "Enter 'V' to view entire collection\n"
                          "Enter 'F' to find a movie from collection\n"
                          "Enter 'Q' to quit\n")).lower()

    # Continue looping through until user quits program
    while user_command in {'v', 'a', 'f'}:
        # if user input is 'a' call add function from add module and pass in dict1
        if user_command == 'a':
            add(dict1)

        # if user input is 'v' call view function from view module and pass in dict1
        elif user_command == 'v':
            view(dict1)

        # if user input is 'f' call find function from find module and pass in dict1
        elif user_command == 'f':
            find(dict1)

        user_command = (input("Enter 'A' to add a movie to collection\n"
                              "Enter 'V' to view entire collection\n"
                              "Enter 'F' to find a movie from collection\n"
                              "Enter 'Q' to quit\n")).lower()


if __name__ == "__main__":
    main()






