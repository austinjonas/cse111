print()
#import the math module so we can call the math.ceil function
import math

#get the two numbers from the user
number_items = int(input("How many items will be manufactured? "))
items_per_box = int(input("How many items will be in each box? "))

#compute the number of boxes by dividing
#then use math.ceil function to make sure we don't have 1 less box
boxes_needed = math.ceil(number_items / items_per_box)

#print blank line
print()

#print the statement
print(f"for {number_items} items, packing {items_per_box}, you will need {boxes_needed} boxes.")

print()




##
#here's what I did originally. it used the math.ceil() function
#in a less efficient way.

# print(f"for {number_items} items, packing {items_per_box}, you will need ", end ="" )
# print(math.ceil(boxes_needed), end ="")
# print(" boxes.")