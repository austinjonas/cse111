from cgitb import text


def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    text_list = read_list("provinces.txt")

    #removes the last item from the list
    text_list.pop()

    #removes the first item from the list
    text_list.remove(text_list[0])

    for i in range(len(text_list)):
        if text_list[i] == "AB":
            text_list[i] = "Alberta"
    # Print the entire list.

    print(text_list)

    count = text_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")
    print()

def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

    return text_list

if __name__ == "__main__":
    main()