
import csv

def main():
    i_number_index = 0
    i_number = input("What is the students I-number?: ")
    student_dict = read_dict("students.csv", i_number_index)
    if i_number in student_dict:
        print(student_dict[i_number])
    else:
        print('No such student.')

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
        """
    student_name_index = 1
    students_dict = {}
    with open(filename, "rt") as students_file:
        reader = csv.reader(students_file)
        next(reader)

        for row_list in reader:
            # clean_line = row_list.strip()
            key = row_list[key_column_index]
            students_dict[key] = row_list[student_name_index]

        return students_dict

if __name__ == "__main__":
    main()
