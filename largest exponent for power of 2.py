def largest_power_of_two(n):
    """
    This function returns the largest exponent k such that 2^k <= n.
    
    """
    power = 0
    value = 1  # Start with 2^0 which is 1

    while value * 2 <= n:
        value *= 2
        power += 1

    print(power)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    largest_power_of_two(n)