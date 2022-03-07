print()
#call for the width, aspect, diameter, and make sure to call as a float.
w = float(input("What is the width (first number) on the tire? (ex 205)"))
a = float(input("What is the aspect (second number) on the tire? (ex 60)"))
d = float(input("What is the diameter (third number) on the tire? (ex 15)"))

#call up the math library
import math

#calculate the tire volume
v = (math.pi * (w ** 2) * a * ((w * a) + (2540 * d))) / 10000000000

#blank space
print()

#print the result for the user
print(f"The volume of the inside of your tire is approximately {v: .2f} liters")

#access the datetime library
from datetime import datetime, timedelta

current_date = datetime.now()
# print('Today is: ' + str(current_date))


file = open("volumes.txt", "a")
width = [f" \n {current_date:%Y-%m-%d}, {w}, {a}, {d}, {v: .02f}"]
file.writelines(width)
file.close()


print()