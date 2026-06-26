# CoresCalc - Day 2

while True:
    print("welcome to CoresCalc!")
    print()

    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("That's not a number! try again.")
        continue

    while True:
        print("Choose an operation:")
        print()
        print(" 1. Add (+)")
        print(" 2. Subtract (-)")
        print(" 3. Multiply (x)")
        print(" 4. Divide (/)")
        print(" 5. Done(get result)")
        print()

        choice = input("Your Choice: ")

        if choice == "5":
            break
        
        try:
            num2 = float(input("Enter next number: "))
        except ValueError:
            print("That's not number! Try again.")
            continue

        if choice == "1":
            num1 = num1 + num2
        elif choice =="2":
            num1 = num1 - num2
        elif choice == "3":
            num1 = num1 * num2
        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by 0")
            else:
                num1 = num1/num2
        else:
            print("Invalid Choice. Please enter 1 to 5")

    
    print()
    print("-------------------")
    print(f'Result: {num1}')
    print("-------------------")
    print()

    again = input("Calculate again? (yes/no)")
    if again.lower() != "yes":
        print()
        print("Thanks for using CoresCalc. Bye!")
        break
        
