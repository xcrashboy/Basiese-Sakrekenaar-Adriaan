# This command-line calculator repeatedly asks the user to choose addition,
# subtraction, multiplication, division, clearing the screen, or quitting.
# It calculates with two numbers, displays the result, handles invalid numbers
# and division by zero, and uses a sentinel variable to control the main loop.

# Import os so the program can clear the Windows Command Prompt screen.
import os

# Return the sum of two numbers.
def add(number1, number2):
    return number1 + number2


# Return the difference between two numbers.
def subtract(number1, number2):
    return number1 - number2


# Return the product of two numbers.
def multiply(number1, number2):
    return number1 * number2


# Return the quotient of two numbers.
def divide(number1, number2):
    return number1 / number2


# This sentinel stays True while the calculator should keep running.
keep_running = True

# Repeat the menu until the user chooses to quit.
while keep_running:
    # Display the operations and special commands available to the user.
    print("\nCalculator")
    print("Choose an operation:")
    print("+  Add")
    print("-  Subtract")
    print("*  Multiply")
    print("/  Divide")
    print("C  Clear the screen")
    print("Q  Quit")

    # Read the choice, remove surrounding spaces, and accept uppercase or lowercase.
    choice = input("Enter your choice: ").strip().lower()

    # Set the sentinel to False to finish the loop and exit the calculator.
    if choice == "q":
        keep_running = False
        print("Goodbye!")
    # Clear the Command Prompt without ending the calculator loop.
    elif choice == "c":
        os.system("cls")
    # Ask for numbers only when the user selects a valid arithmetic operation.
    elif choice in ("+", "-", "*", "/"):
        try:
            # Convert the user's text inputs into numbers for arithmetic.
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))

            # Call the function that matches the selected operation.
            if choice == "+":
                result = add(number1, number2)
            elif choice == "-":
                result = subtract(number1, number2)
            elif choice == "*":
                result = multiply(number1, number2)
            elif choice == "/":
                result = divide(number1, number2)

            # Show the calculated answer.
            print(f"Result: {result}")
        # Handle text that cannot be converted into a number.
        except ValueError:
            print("Please enter valid numbers.")
        # Handle division by zero, which is not a valid calculation.
        except ZeroDivisionError:
            print("Cannot divide by zero.")
    # Explain the valid choices if the user enters an unsupported command.
    else:
        print("Invalid choice. Choose +, -, *, /, C, or Q.")
