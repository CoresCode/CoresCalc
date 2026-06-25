print("Welcome to CoresCalc!")
print()

num1 = float(input("Enter first number: "))

print("Choose operation: (1-4)\n")
print("  1. Add")
print("  2. Subtract")
print("  3. Multiply")
print("  4. Divide")
print()

choice = input("Your choice: ")
num2 = float(input("Enter second number: "))
print("---------------------------------")

if choice == "1":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"Result: {num1} x {num2} = {result}")

elif choice == "4":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

else:
    print("Invalid choice. Please enter 1, 2, 3 or 4.")

print("---------------------------------")