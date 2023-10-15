num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

print("Select operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter Choice (1/2/3/4):")

if choice == '1':
    result = num1 + num2
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
    # Check for division by zero
    if num2 == 0:
        print("Error: Division by zero!")
    else:
        result = num1 / num2
else:
    print("Invalid input")
    print("Result:", result)

another_calculation = input("Do you want to perform another calculation? (yes/no):")
