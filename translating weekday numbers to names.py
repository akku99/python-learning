# given the day of the week and converting it to the corresponding name of the day

def day_of_week(day_number):

    if day_number == 1:
        return "Monday"
    elif day_number == 2:
        return "Tuesday"
    elif day_number == 3:
        return "Wednesday"
    elif day_number == 4:
        return "Thursday"
    elif day_number == 5:
        return "Friday"
    elif day_number == 6:
        return "Saturday"
    elif day_number == 7:
        return "Sunday"
    else:
        return "Invalid day number. Please enter a number between 1 and 7."

def main():
    # Read the day number from the user;;
    day_number = int(input("Enter the day number (1-7): "))
    result = day_of_week(day_number)
    print(result)

if __name__ == "__main__":
    main()