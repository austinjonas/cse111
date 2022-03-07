import csv

product_code_index = 0
product_name_index = 1
product_price_index = 2


def main():
    products_list = read_compound_list("products.csv")
    print(products_list)

def read_compound_list(filename):
    
    compound_list = []
    
    with open(filename, "rt") as products_file:
        reader = csv.reader(products_file)
        
        #skips the first line of the .csv to avoid errors
        next(reader)

        for row_list in reader:
            compound_list.append(row_list)

    return compound_list

        
if __name__ == "__main__":
    main()