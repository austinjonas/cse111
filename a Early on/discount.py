from datetime import datetime

discount = .1
Stx = 1.075

print()
subtotal = float(input("Please enter the subtotal for your order: "))

current_date = datetime.now()

weekday = current_date.weekday()

if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = subtotal * discount
    print(f"Discount amount: {discount}")
    subtotal -= discount

total = subtotal * Stx

print(f"Total (including sales tax): {total: .2f}")
print()

# from datetime import datetime, timedelta

# today = datetime.now()
# print('Today is: ' + str(today))

# one_day = timedelta(days=1)
# yesterday = today - one_day
# print('Yesterday was: ' + str(yesterday))