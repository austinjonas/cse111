# import math


# def get_user_radius():
#     user_string = input("Please enter a radius: ")
#     #if this isn't a number...don't convert it
#     return float(user_string)

# def compute_circle_area(radius):
#     return radius ** 2 * math.pi



# x = "25.6"

# x_num = compute_circle_area(25.6)

# print(x_num)

def kilometers_from_miles(miles):
    """Convert a value in miles to kilometers
    and return the kilometers value.
    """
    miles = float(input("Please enter a distance in miles: "))
    km = miles * 1.60934
    return km