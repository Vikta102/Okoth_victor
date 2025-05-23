# write a program to handle errors.program should ask for two numbers using input and then divide them. use an infinite loop to keep asking until a valid input is provided.

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        

        result = num1 / num2
        
        print(f"Result of division: {result}")
        break
        
    except ValueError:
        print("Error: Please enter valid numbers (no letters/symbols)!")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")