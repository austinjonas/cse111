print()

def main():
    odo_start = float(input("How many miles did your odometer read at the start of your drive? "))
    odo_end = float(input("How many miles did your odometer read at the end of your drive? "))
    gallons = float(input("How many gallons of gas did you use during your drive? "))

    mpg = miles_per_gallon(odo_end, odo_start, gallons)
    lp100k = lp100k_from_mpg(mpg)


    print("Here are your results")
    print(f"Your car is getting {mpg: .1f} miles per gallon.")
    print(f"Your car is getting {lp100k: .1} liters per 100 kilometers.")



def miles_per_gallon(odo_end, odo_start, gallons):
    mpg = ((odo_end - odo_start) / (gallons))
    return mpg


def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k


# Call the main function so that
# this program will start executing.
main()