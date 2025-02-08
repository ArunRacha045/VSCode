try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("No exceptions occurred!")
finally:
    print("This will always execute, regardless of exceptions.")