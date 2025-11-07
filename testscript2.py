import os



if os.name == 'nt':  # For Windows
    os.system('cls')
else:  # For macOS and Linux
    os.system('clear')

weight = float(input("what's your weight? "))
system_selection = input("is your weight in (K)g or (L)bs? ")
if system_selection.upper() == 'K':
    print("Your weight is " + str(2.20462 * weight) + 'lbs')
elif system_selection.upper() == 'L':
    print("Your weight is " + str(0.453592 * weight) + 'kg')