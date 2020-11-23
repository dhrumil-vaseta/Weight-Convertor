weight = int(input('What is the weight: '))
unit = input("Select 'L' for (L)bs or 'K' for (K)g: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos.")
elif unit.upper() == "K":
    converted = weight / 0.45
    print(f"You are {converted} lbs.")
else:
    print("Invalid unit. Please select 'L' or 'K'. ")