import csv
from itertools import product

def main():
    product_number_index = 0

    product_number = input("what is the product number?: ")
    product_dict = read_dict("products.csv", product_number_index)
    request_dict = read_dict("request.csv", product_number_index)
    
    #print the product dictionary
    print(product_dict)

    # use the input to find a thing from the dictionary
    if product_number in product_dict:
        print(product_dict[product_number])
    else:
        print("no")

    


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    
    product_name_index = 1
    products_dict = {}
    with open(filename, "rt") as products_file:
        reader = csv.reader(products_file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            products_dict[key] = row_list[product_name_index]

        return products_dict
            

if __name__ == "__main__":
    main()