
def tip_calculator():
    # Use a breakpoint in the code line below to debug your script.
    total_bill = float(input('Welcome to the tip calculator!\nWhat was the total for the bill? '))
    tip = float(input('How much tip % would you like to give? '))
    people_amount = int(input('How many people to split the bill? '))

    tip = total_bill * (tip/100)
    split = round((total_bill + tip) / people_amount, 2)
    print(f'Each person should pay: ${split}')

if __name__ == '__main__':
    tip_calculator()

