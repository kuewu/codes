# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Main program
def main():
    # Input: Ask the user for a number
    num = int(input("Enter a number to calculate its factorial: "))

    # Calculate factorial using the function
    fact = factorial(num)

    # Output: Display the factorial
    print(f"The factorial of {num} is {fact}")

# Execute the main program
if __name__ == "__main__":
    main()
