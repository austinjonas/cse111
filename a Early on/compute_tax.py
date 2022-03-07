def prompt_for_income():
    income = float(input("please enter your annual income: "))
    return income

def compute_tax(amount):
    return amount * .06

def main():
    print(compute_tax(prompt_for_income()))

main()