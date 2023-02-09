def get_quarter_345(month_345):
    """
    Returns the quarter of the year for a given month
    """
    # Check if the entered month is in the first quarter
    if month_345 in [1, 2, 3, 4]:
        return "first quarter"
    # Check if the entered month is in the second quarter
    elif month_345 in [5, 6, 7]:
        return "second quarter"
    # Check if the entered month is in the third quarter
    elif month_345 in [8, 9]:
        return "third quarter"
    # Check if the entered month is in the fourth quarter
    elif month_345 in [10, 11, 12]:
        return "fourth quarter"
    # Return None for invalid input
    else:
        return None


def main_345():
    """
    Main function to run the program
    """
    try:
        # Request user input for a month as a number between 1 and 12
        month_345 = int(input("Enter a month as a number between 1 and 12: "))
    except ValueError:
        print("Error: Please enter a valid number between 1 and 12.")
        return

    # Get the quarter of the year for the entered month
    quarter_345 = get_quarter_345(month_345)

    # Check if the quarter was found
    if quarter_345:
        print("The month is in the", quarter_345, "of the year.")
    else:
        print("Error: Please enter a valid number between 1 and 12.")

if __name__ == "__main__":
    main_345()
