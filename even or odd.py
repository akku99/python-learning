"""
******* WITHOUT USING FUNCTION *******
"""

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


"""
********** USING FUNCTION **********
"""

def check_even_odd(number):
    
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
if __name__ == "__main__":
    try:
        # Prompt user for input and convert it to an integer
        user_input = int(input("Enter an integer: "))

         # Call the function and get the result
        result = check_even_odd(user_input)

        # Print the final result
        print(f"The Number{user_input} is {result}.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")