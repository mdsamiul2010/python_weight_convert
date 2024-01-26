def lbs():
    while True:
        try:
            user_weight = float(input("Enter amount: "))
            result = user_weight * 0.45
            print(f"Result is: {result}")
            print()
            break
        except ValueError:
            print("Please enter valid numbers!")
def kg():
    while True:
        try:
            user_weight = float(input("Enter amount: "))
            result = user_weight / 0.45
            print(f"Result is: {result}")
            print()
            break
        except ValueError:
            print("Please enter valid numbers!")


print("WEIGHT CONVERTER CONSOLE")
print("""Choose one option at a time
1. Convert to (L)bs
2. Convert to (K)g
3. Exit the program""")

while True:
    unit = input("Choose option: ")
    if unit == "1":
        lbs()
    elif unit == "2":
        kg()
    elif unit == "3":
        dialogue_box = str(input("Are you sure? (Y/n): ")).lower()
        if dialogue_box == "y":
            break
        elif dialogue_box == "n":
            continue
        else:
            print("INVALID COMMAND INSERTED!")
            continue
    else:
        print("Please choose valid option!")
        continue
